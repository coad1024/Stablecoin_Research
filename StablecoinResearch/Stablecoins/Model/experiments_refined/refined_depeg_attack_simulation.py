"""
refined_depeg_attack_simulation.py

Simplified de-peg attack simulation implementing the academically refined framework.
Based on SoK paper guidelines and systematic research methodology.

IMPORTANT: Set PYTHONPATH to project root before running this script!
In PowerShell:
  $env:PYTHONPATH = (Resolve-Path .).Path
  python Stablecoins/Model/experiments_refined/refined_depeg_attack_simulation.py

This ensures that imports work correctly.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === REFINED MODEL PARAMETERS (Academic Specification) ===

# Core simulation parameters
POOL_DEPTHS = [100_000, 1_000_000, 5_000_000, 10_000_000]  # Pool liquidity levels
ATTACK_SIZES = [0.005, 0.01, 0.025, 0.05, 0.10]  # Attack sizes as fraction of pool
N_SEEDS = 30  # Monte Carlo seeds per scenario (N=100 for robustness checks)
N_ROBUSTNESS_SEEDS = 100  # For final validation

# Simulation structure
SIMULATION_HORIZON = 50  # Total ticks per simulation
ATTACK_TICK = 21  # Middle of simulation (tick 21 out of 50)
TIME_UNIT = "1_hour"  # Each tick represents 1 hour

# Peg failure criteria (from SoK paper)
PEG_THRESHOLD = 0.98  # Price below this is considered "broken"
CONSECUTIVE_TICKS = 3  # Must persist for this many ticks

# Background user behavior regimes
USER_REGIMES = {
    'Normal': {
        'mu_factor': 0.0,      # Mean-zero noise
        'sigma_factor': 0.001  # σ = 0.001 × L (0.1% of pool per tick)
    },
    'Panic': {
        'mu_factor': -0.005,   # Net selling pressure μ = -0.005 × L  
        'sigma_factor': 0.02   # Higher volatility σ = 0.02 × L
    }
}

# Arbitrage response archetypes (stochastic restoration)
ARBITRAGE_ARCHETYPES = {
    'Fast': {
        'p_act': 1.0,    # Always acts (100% probability)
        'r_restore': 0.9  # Restores 90% of price gap
    },
    'Moderate': {
        'p_act': 0.5,    # Acts 50% of the time  
        'r_restore': 0.6  # Restores 60% of price gap
    },
    'Slow': {
        'p_act': 0.1,    # Acts 10% of the time
        'r_restore': 0.3  # Restores 30% of price gap
    }
}

class SimplifiedAMM:
    """
    Simplified constant-product AMM implementation for refined model.
    
    Assumptions:
    - No fees (fee = 0)
    - Symmetric initial pools (S_reserve = U_reserve = L)
    - Constant product formula: x * y = k
    """
    
    def __init__(self, pool_depth):
        """Initialize symmetric pool with given depth."""
        self.initial_depth = pool_depth
        self.stablecoin_reserve = float(pool_depth)  # S reserves
        self.usd_reserve = float(pool_depth)         # USD reserves  
        self.k = pool_depth ** 2                    # Constant product
        
    @property
    def price(self):
        """Current stablecoin price (USD per stablecoin)."""
        return self.usd_reserve / self.stablecoin_reserve
    
    def execute_swap(self, stablecoin_amount):
        """
        Execute swap: sell stablecoin_amount for USD.
        
        Args:
            stablecoin_amount (float): Amount of stablecoin to sell (positive = sell)
        
        Returns:
            float: USD received (negative if buying stablecoin)
        """
        if stablecoin_amount == 0:
            return 0.0
            
        # Constant product: (x + Δx)(y - Δy) = k
        # Solve for Δy given Δx
        new_stablecoin_reserve = self.stablecoin_reserve + stablecoin_amount
        new_usd_reserve = self.k / new_stablecoin_reserve
        
        usd_received = self.usd_reserve - new_usd_reserve
        
        # Update reserves
        self.stablecoin_reserve = new_stablecoin_reserve
        self.usd_reserve = new_usd_reserve
        
        return usd_received

class RefinedDepegSimulation:
    """
    Refined de-peg attack simulation implementing academic specifications.
    """
    
    def __init__(self, pool_depth, attack_size_frac, user_regime, arbitrage_mode, seed):
        """Initialize simulation with specified parameters."""
        self.pool_depth = pool_depth
        self.attack_size_frac = attack_size_frac
        self.attack_amount = pool_depth * attack_size_frac
        self.user_regime = USER_REGIMES[user_regime]
        self.arbitrage = ARBITRAGE_ARCHETYPES[arbitrage_mode]
        self.seed = seed
        
        # Initialize AMM
        self.amm = SimplifiedAMM(pool_depth)
        
        # Initialize random number generator
        self.rng = np.random.RandomState(seed)
        
        # Tracking variables
        self.price_history = []
        self.reserves_history = []
        self.user_trades = []
        self.arbitrage_actions = []
        
    def generate_user_trade(self, tick):
        """Generate background user trade for given tick."""
        mu = self.user_regime['mu_factor'] * self.pool_depth
        sigma = self.user_regime['sigma_factor'] * self.pool_depth
        
        # Generate trade size (positive = sell stablecoin, negative = buy stablecoin)
        trade_size = self.rng.normal(mu, sigma)
        return trade_size
    
    def apply_arbitrage(self, current_price):
        """Apply stochastic arbitrage restoration."""
        price_gap = 1.0 - current_price  # Gap from peg (positive = undervalued)
        
        # Check if arbitrage acts this tick
        if self.rng.random() < self.arbitrage['p_act']:
            # Calculate restoration amount
            restoration_fraction = self.arbitrage['r_restore']
            target_price_change = price_gap * restoration_fraction
            
            # Convert price change to trade size
            # For small price changes: Δp ≈ -Δx / x (where x = stablecoin reserves)
            trade_size = -target_price_change * self.amm.stablecoin_reserve
            
            # Execute arbitrage trade
            self.amm.execute_swap(trade_size)
            
            self.arbitrage_actions.append({
                'tick': len(self.price_history),
                'price_gap': price_gap,
                'trade_size': trade_size,
                'restoration_frac': restoration_fraction
            })
            
            return True
        
        return False
    
    def run_simulation(self):
        """Run complete simulation and return results."""
        
        # Record initial state
        self.price_history.append(self.amm.price)
        self.reserves_history.append({
            'stablecoin': self.amm.stablecoin_reserve,
            'usd': self.amm.usd_reserve
        })
        
        attacker_proceeds = 0.0
        
        # Run simulation ticks
        for tick in range(SIMULATION_HORIZON):
            
            # Execute attack at specified tick
            if tick == ATTACK_TICK:
                attacker_proceeds = self.amm.execute_swap(self.attack_amount)
            
            # Generate and execute user trade
            user_trade = self.generate_user_trade(tick)
            if abs(user_trade) > 1e-10:  # Avoid tiny trades
                self.amm.execute_swap(user_trade)
                self.user_trades.append({
                    'tick': tick,
                    'trade_size': user_trade
                })
            
            # Apply arbitrage
            self.apply_arbitrage(self.amm.price)
            
            # Record state
            self.price_history.append(self.amm.price)
            self.reserves_history.append({
                'stablecoin': self.amm.stablecoin_reserve,
                'usd': self.amm.usd_reserve
            })
        
        # Analyze results
        results = self.analyze_results(attacker_proceeds)
        
        return results
    
    def analyze_results(self, attacker_proceeds):
        """Analyze simulation results and extract key metrics."""
        
        prices = np.array(self.price_history)
        
        # Find peg breach periods
        breach_mask = prices < PEG_THRESHOLD
        breach_periods = self.find_consecutive_periods(breach_mask, CONSECUTIVE_TICKS)
        
        # Determine if peg failure occurred
        peg_failure = len(breach_periods) > 0
        
        # Calculate metrics
        min_price = np.min(prices)
        max_price_drop = 1.0 - min_price
        
        # Find first breach and recovery times
        first_breach_tick = None
        recovery_tick = None
        
        if peg_failure:
            first_breach_tick = breach_periods[0][0]
            
            # Look for recovery (price > PEG_THRESHOLD for CONSECUTIVE_TICKS)
            recovery_mask = prices >= PEG_THRESHOLD
            recovery_periods = self.find_consecutive_periods(recovery_mask, CONSECUTIVE_TICKS)
            
            # Find first recovery after first breach
            for start, end in recovery_periods:
                if start > first_breach_tick:
                    recovery_tick = start
                    break
        
        # Attacker profit analysis (cost = 0 by assumption)
        profit = attacker_proceeds  # No acquisition cost
        profit_per_pool = profit / self.pool_depth if self.pool_depth > 0 else 0
        
        return {
            'pool_depth': self.pool_depth,
            'attack_size_frac': self.attack_size_frac,
            'attack_amount': self.attack_amount,
            'seed': self.seed,
            'peg_failure': peg_failure,
            'min_price': min_price,
            'max_price_drop': max_price_drop,
            'first_breach_tick': first_breach_tick,
            'recovery_tick': recovery_tick,
            'attacker_proceeds': attacker_proceeds,
            'profit': profit,
            'profit_per_pool': profit_per_pool,
            'breach_periods': breach_periods,
            'price_history': prices.tolist(),
            'final_price': prices[-1]
        }
    
    def find_consecutive_periods(self, mask, min_length):
        """Find periods where mask is True for at least min_length consecutive steps."""
        periods = []
        start = None
        
        for i, value in enumerate(mask):
            if value and start is None:
                start = i
            elif not value and start is not None:
                if i - start >= min_length:
                    periods.append((start, i - 1))
                start = None
        
        # Check if period extends to end
        if start is not None and len(mask) - start >= min_length:
            periods.append((start, len(mask) - 1))
        
        return periods

def run_parameter_sweep():
    """Run systematic parameter sweep according to refined specification."""
    
    print("Starting refined de-peg attack parameter sweep...")
    print(f"Time unit: {TIME_UNIT} per tick")
    print(f"Simulation horizon: {SIMULATION_HORIZON} ticks")
    print(f"Attack occurs at tick: {ATTACK_TICK}")
    print(f"Monte Carlo seeds: {N_SEEDS} per scenario")
    print()
    
    results = []
    total_scenarios = len(POOL_DEPTHS) * len(ATTACK_SIZES) * len(USER_REGIMES) * len(ARBITRAGE_ARCHETYPES)
    
    with tqdm(total=total_scenarios * N_SEEDS, desc="Running simulations") as pbar:
        
        for pool_depth in POOL_DEPTHS:
            for attack_size_frac in ATTACK_SIZES:
                for user_regime_name in USER_REGIMES.keys():
                    for arb_mode_name in ARBITRAGE_ARCHETYPES.keys():
                        
                        # Run Monte Carlo seeds for this scenario
                        scenario_results = []
                        
                        for seed in range(N_SEEDS):
                            sim = RefinedDepegSimulation(
                                pool_depth=pool_depth,
                                attack_size_frac=attack_size_frac,
                                user_regime=user_regime_name,
                                arbitrage_mode=arb_mode_name,
                                seed=seed
                            )
                            
                            result = sim.run_simulation()
                            result['user_regime'] = user_regime_name
                            result['arbitrage_mode'] = arb_mode_name
                            
                            scenario_results.append(result)
                            results.append(result)
                            pbar.update(1)
                        
                        # Calculate scenario summary statistics
                        failure_rate = np.mean([r['peg_failure'] for r in scenario_results])
                        avg_profit = np.mean([r['profit'] for r in scenario_results])
                        avg_min_price = np.mean([r['min_price'] for r in scenario_results])
                        
                        print(f"Scenario: Pool=${pool_depth:,}, Attack={attack_size_frac:.1%}, "
                              f"Regime={user_regime_name}, Arb={arb_mode_name}")
                        print(f"  Failure rate: {failure_rate:.1%}, Avg profit: ${avg_profit:.0f}, "
                              f"Avg min price: ${avg_min_price:.3f}")
    
    return results

def analyze_and_save_results(results):
    """Analyze results and save outputs."""
    
    df = pd.DataFrame(results)
    
    # Save detailed results
    output_file = os.path.join(OUTPUT_DIR, 'refined_depeg_attack_results.csv')
    df.to_csv(output_file, index=False)
    print(f"Saved detailed results to: {output_file}")
    
    # Calculate summary statistics by scenario
    summary_stats = df.groupby(['pool_depth', 'attack_size_frac', 'user_regime', 'arbitrage_mode']).agg({
        'peg_failure': ['mean', 'std'],
        'profit': ['mean', 'std', 'min', 'max'],
        'min_price': ['mean', 'std'],
        'max_price_drop': ['mean', 'std']
    }).round(4)
    
    summary_stats.columns = ['_'.join(col).strip() for col in summary_stats.columns]
    summary_stats = summary_stats.reset_index()
    
    # Save summary statistics
    summary_file = os.path.join(OUTPUT_DIR, 'refined_summary_statistics.csv')
    summary_stats.to_csv(summary_file, index=False)
    print(f"Saved summary statistics to: {summary_file}")
    
    # Generate key findings for baseline scenario (Moderate + Panic)
    baseline_results = df[(df['arbitrage_mode'] == 'Moderate') & (df['user_regime'] == 'Panic')]
    
    # Find minimum attack size for 50% failure probability
    min_attack_thresholds = []
    
    for pool_depth in POOL_DEPTHS:
        pool_data = baseline_results[baseline_results['pool_depth'] == pool_depth]
        
        # Calculate failure rate by attack size
        failure_rates = pool_data.groupby('attack_size_frac')['peg_failure'].mean()
        
        # Find minimum attack size with >= 50% failure rate
        viable_attacks = failure_rates[failure_rates >= 0.5]
        
        if len(viable_attacks) > 0:
            min_attack_size = viable_attacks.index.min()
        else:
            min_attack_size = np.nan
        
        min_attack_thresholds.append({
            'pool_depth': pool_depth,
            'min_attack_size_50pct': min_attack_size
        })
    
    # Save minimum attack thresholds
    threshold_df = pd.DataFrame(min_attack_thresholds)
    threshold_file = os.path.join(OUTPUT_DIR, 'refined_min_attack_thresholds.csv')
    threshold_df.to_csv(threshold_file, index=False)
    print(f"Saved minimum attack thresholds to: {threshold_file}")
    
    return df, summary_stats, threshold_df

def create_visualizations(df):
    """Create heatmaps and visualizations."""
    
    print("Creating visualizations...")
    
    # Create failure probability heatmap for baseline scenario
    baseline_data = df[(df['arbitrage_mode'] == 'Moderate') & (df['user_regime'] == 'Panic')]
    
    # Calculate failure rates
    heatmap_data = baseline_data.groupby(['pool_depth', 'attack_size_frac'])['peg_failure'].mean().unstack()
    
    # Create heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        heatmap_data, 
        annot=True, 
        fmt='.2f', 
        cmap='Reds',
        cbar_kws={'label': 'Failure Probability'},
        xticklabels=[f"${x:,.0f}" for x in heatmap_data.columns],
        yticklabels=[f"{y:.1%}" for y in heatmap_data.index]
    )
    plt.title('Peg Failure Probability - Refined Model\n(Moderate Arbitrage + Panic Regime)')
    plt.xlabel('Pool Depth')
    plt.ylabel('Attack Size (% of Pool)')
    plt.tight_layout()
    
    heatmap_file = os.path.join(OUTPUT_DIR, 'refined_failure_probability_heatmap.png')
    plt.savefig(heatmap_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved heatmap to: {heatmap_file}")
    
    # Create arbitrage sensitivity comparison
    arb_comparison = df[df['user_regime'] == 'Panic'].groupby(['pool_depth', 'attack_size_frac', 'arbitrage_mode'])['peg_failure'].mean().unstack()
    
    plt.figure(figsize=(15, 5))
    
    for i, arb_mode in enumerate(['Fast', 'Moderate', 'Slow']):
        plt.subplot(1, 3, i+1)
        mode_data = arb_comparison[arb_mode].unstack()
        
        sns.heatmap(
            mode_data,
            annot=True,
            fmt='.2f',
            cmap='Reds',
            vmin=0,
            vmax=1,
            cbar_kws={'label': 'Failure Probability'},
            xticklabels=[f"${x:,.0f}" for x in mode_data.columns],
            yticklabels=[f"{y:.1%}" for y in mode_data.index]
        )
        plt.title(f'{arb_mode} Arbitrage')
        plt.xlabel('Pool Depth')
        if i == 0:
            plt.ylabel('Attack Size (% of Pool)')
    
    plt.suptitle('Arbitrage Speed Sensitivity Analysis - Refined Model\n(Panic Regime)', fontsize=14)
    plt.tight_layout()
    
    arb_file = os.path.join(OUTPUT_DIR, 'refined_arbitrage_sensitivity.png')
    plt.savefig(arb_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved arbitrage sensitivity plot to: {arb_file}")

if __name__ == "__main__":
    print("=== REFINED DE-PEG ATTACK SIMULATION ===")
    print("Academic specification implementation")
    print("Based on SoK paper methodology")
    print()
    
    # Run parameter sweep
    results = run_parameter_sweep()
    
    # Analyze and save results
    df, summary_stats, thresholds = analyze_and_save_results(results)
    
    # Create visualizations
    create_visualizations(df)
    
    print("\n=== REFINED SIMULATION COMPLETE ===")
    print(f"Total simulations run: {len(results)}")
    print(f"Parameter combinations: {len(POOL_DEPTHS)} pools × {len(ATTACK_SIZES)} attacks × {len(USER_REGIMES)} regimes × {len(ARBITRAGE_ARCHETYPES)} arbitrage")
    print(f"Seeds per combination: {N_SEEDS}")
    print()
    
    # Display key findings
    print("KEY FINDINGS (Moderate Arbitrage + Panic Regime):")
    baseline_df = df[(df['arbitrage_mode'] == 'Moderate') & (df['user_regime'] == 'Panic')]
    
    for pool_depth in POOL_DEPTHS:
        pool_data = baseline_df[baseline_df['pool_depth'] == pool_depth]
        failure_rates = pool_data.groupby('attack_size_frac')['peg_failure'].mean()
        
        print(f"Pool ${pool_depth:,}:")
        for attack_size, failure_rate in failure_rates.items():
            print(f"  {attack_size:.1%} attack → {failure_rate:.1%} failure rate")
    
    print("\nFiles generated in outputs/ folder:")
    print("- refined_depeg_attack_results.csv (detailed results)")
    print("- refined_summary_statistics.csv (scenario summaries)")
    print("- refined_min_attack_thresholds.csv (50% failure thresholds)")
    print("- refined_failure_probability_heatmap.png (main heatmap)")
    print("- refined_arbitrage_sensitivity.png (arbitrage comparison)")
