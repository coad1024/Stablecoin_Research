"""
Streamlined refined simulation - no pandas dependency
"""
import numpy as np
import os
import json

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parameters (reduced for quick testing)
POOL_DEPTHS = [1_000_000, 10_000_000]  # Just 2 pool sizes
ATTACK_SIZES = [0.05, 0.10]  # Just 2 attack sizes  
N_SEEDS = 5  # Reduced from 30 for quick test

USER_REGIMES = {
    'Panic': {
        'mu_factor': -0.005,
        'sigma_factor': 0.02
    }
}

ARBITRAGE_ARCHETYPES = {
    'Moderate': {
        'p_act': 0.5,
        'r_restore': 0.6
    }
}

SIMULATION_HORIZON = 50
ATTACK_TICK = 21
PEG_THRESHOLD = 0.98
CONSECUTIVE_TICKS = 3

class SimplifiedAMM:
    def __init__(self, pool_depth):
        self.initial_depth = pool_depth
        self.stablecoin_reserve = float(pool_depth)
        self.usd_reserve = float(pool_depth)
        self.k = pool_depth ** 2
        
    @property
    def price(self):
        return self.usd_reserve / self.stablecoin_reserve
    
    def execute_swap(self, stablecoin_amount):
        if stablecoin_amount == 0:
            return 0.0
            
        new_stablecoin_reserve = self.stablecoin_reserve + stablecoin_amount
        new_usd_reserve = self.k / new_stablecoin_reserve
        usd_received = self.usd_reserve - new_usd_reserve
        
        self.stablecoin_reserve = new_stablecoin_reserve
        self.usd_reserve = new_usd_reserve
        
        return usd_received

class StreamlinedDepegSim:
    def __init__(self, pool_depth, attack_size_frac, seed):
        self.pool_depth = pool_depth
        self.attack_size_frac = attack_size_frac
        self.attack_amount = pool_depth * attack_size_frac
        self.seed = seed
        
        self.amm = SimplifiedAMM(pool_depth)
        self.rng = np.random.RandomState(seed)
        self.price_history = []
        
    def generate_user_trade(self):
        mu = -0.005 * self.pool_depth  # Panic selling
        sigma = 0.02 * self.pool_depth
        return self.rng.normal(mu, sigma)
    
    def apply_arbitrage(self, current_price):
        price_gap = 1.0 - current_price
        
        if self.rng.random() < 0.5:  # 50% chance (Moderate)
            trade_size = -price_gap * 0.6 * self.amm.stablecoin_reserve  # 60% restoration
            self.amm.execute_swap(trade_size)
            return True
        return False
    
    def find_consecutive_periods(self, mask, min_length):
        periods = []
        start = None
        
        for i, value in enumerate(mask):
            if value and start is None:
                start = i
            elif not value and start is not None:
                if i - start >= min_length:
                    periods.append((start, i - 1))
                start = None
        
        if start is not None and len(mask) - start >= min_length:
            periods.append((start, len(mask) - 1))
        
        return periods
    
    def run_simulation(self):
        self.price_history.append(self.amm.price)
        attacker_proceeds = 0.0
        
        for tick in range(SIMULATION_HORIZON):
            if tick == ATTACK_TICK:
                attacker_proceeds = self.amm.execute_swap(self.attack_amount)
            
            user_trade = self.generate_user_trade()
            if abs(user_trade) > 1e-10:
                self.amm.execute_swap(user_trade)
            
            self.apply_arbitrage(self.amm.price)
            self.price_history.append(self.amm.price)
        
        # Analyze results
        prices = np.array(self.price_history)
        breach_mask = prices < PEG_THRESHOLD
        breach_periods = self.find_consecutive_periods(breach_mask, CONSECUTIVE_TICKS)
        
        return {
            'pool_depth': self.pool_depth,
            'attack_size_frac': self.attack_size_frac,
            'seed': self.seed,
            'peg_failure': len(breach_periods) > 0,
            'min_price': float(np.min(prices)),
            'profit': float(attacker_proceeds),
            'final_price': float(prices[-1])
        }

def run_streamlined_sweep():
    print("Starting streamlined parameter sweep...")
    
    results = []
    total_scenarios = len(POOL_DEPTHS) * len(ATTACK_SIZES) * N_SEEDS
    
    scenario_count = 0
    for pool_depth in POOL_DEPTHS:
        for attack_size_frac in ATTACK_SIZES:
            print(f"Testing Pool=${pool_depth:,}, Attack={attack_size_frac:.1%}")
            
            scenario_results = []
            for seed in range(N_SEEDS):
                sim = StreamlinedDepegSim(pool_depth, attack_size_frac, seed)
                result = sim.run_simulation()
                results.append(result)
                scenario_results.append(result)
                scenario_count += 1
                
                print(f"  Seed {seed}: Failure={result['peg_failure']}, "
                      f"Profit=${result['profit']:,.0f}, Min_Price=${result['min_price']:.3f}")
            
            # Calculate scenario summary
            failure_rate = sum(r['peg_failure'] for r in scenario_results) / len(scenario_results)
            avg_profit = sum(r['profit'] for r in scenario_results) / len(scenario_results)
            
            print(f"  Scenario Summary: {failure_rate:.1%} failure rate, ${avg_profit:,.0f} avg profit")
    
    return results

def save_results(results):
    print(f"\nSaving {len(results)} results...")
    
    # Save as JSON (no pandas needed)
    results_file = os.path.join(OUTPUT_DIR, 'streamlined_results.json')
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Saved to: {results_file}")
    
    # Calculate and save summary
    summary = {}
    
    for pool_depth in POOL_DEPTHS:
        for attack_size_frac in ATTACK_SIZES:
            scenario_key = f"pool_{pool_depth}_attack_{attack_size_frac}"
            scenario_results = [r for r in results 
                              if r['pool_depth'] == pool_depth and r['attack_size_frac'] == attack_size_frac]
            
            if scenario_results:
                failure_rate = sum(r['peg_failure'] for r in scenario_results) / len(scenario_results)
                avg_profit = sum(r['profit'] for r in scenario_results) / len(scenario_results)
                min_price_avg = sum(r['min_price'] for r in scenario_results) / len(scenario_results)
                
                summary[scenario_key] = {
                    'pool_depth': pool_depth,
                    'attack_size_frac': attack_size_frac,
                    'failure_rate': failure_rate,
                    'avg_profit': avg_profit,
                    'avg_min_price': min_price_avg,
                    'n_simulations': len(scenario_results)
                }
    
    summary_file = os.path.join(OUTPUT_DIR, 'streamlined_summary.json')
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Saved summary to: {summary_file}")
    
    return summary

if __name__ == "__main__":
    print("=== STREAMLINED REFINED SIMULATION ===")
    print("No pandas dependency version")
    print()
    
    results = run_streamlined_sweep()
    summary = save_results(results)
    
    print("\n=== KEY FINDINGS ===")
    for scenario_key, stats in summary.items():
        pool = stats['pool_depth']
        attack = stats['attack_size_frac']
        failure_rate = stats['failure_rate']
        avg_profit = stats['avg_profit']
        
        print(f"Pool ${pool:,}, Attack {attack:.1%}: "
              f"{failure_rate:.1%} failure rate, ${avg_profit:,.0f} avg profit")
    
    print(f"\nCompleted {len(results)} simulations successfully!")
    print("Results saved to outputs/ folder")
