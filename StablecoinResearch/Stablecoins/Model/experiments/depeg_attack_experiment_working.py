"""
Simple working de-peg attack experiment that avoids complex token interactions
"""
import os
import sys
sys.path.append(os.path.abspath('.'))

import numpy as np
import pandas as pd

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Simplified simulation parameters
POOL_DEPTHS = [100_000, 1_000_000, 5_000_000]
ATTACKER_SIZES = [0.005, 0.01, 0.025, 0.05]
USER_REGIMES = ['Normal', 'Panic']
ARBITRAGE_MODES = ['Fast', 'Moderate', 'Slow']
N_SEEDS = 10  # Reduced for faster execution
N_TICKS = 30  # Reduced for faster execution
ATTACK_TICK = 10

def simulate_price_series(pool_depth, delta_s_frac, user_regime, arb_mode, seed):
    """Simplified price simulation without complex token mechanics"""
    np.random.seed(seed)
    
    # Initial conditions
    price = 1.0
    prices = []
    
    # Regime parameters
    user_noise = {
        'Normal': lambda: np.random.normal(0, 0.001),
        'Panic': lambda: np.random.normal(-0.002, 0.005)
    }
    
    arb_strength = {
        'Fast': 0.8,
        'Moderate': 0.5,
        'Slow': 0.2
    }
    
    arb_frequency = {
        'Fast': 0.9,
        'Moderate': 0.5,
        'Slow': 0.2
    }
    
    for tick in range(N_TICKS):
        # Attack at specified tick
        if tick == ATTACK_TICK:
            attack_impact = delta_s_frac * 0.5  # Simplified attack impact
            price -= attack_impact
        
        # User trading impact
        user_impact = user_noise[user_regime]()
        price += user_impact
        
        # Arbitrage restoration
        if np.random.rand() < arb_frequency[arb_mode]:
            # Restore towards peg
            deviation = 1.0 - price
            price += deviation * arb_strength[arb_mode]
        
        # Add some market noise
        price += np.random.normal(0, 0.0005)
        
        # Ensure price stays positive
        price = max(price, 0.01)
        
        prices.append(price)
    
    return prices

def check_peg_breach(prices, threshold=0.98, consecutive_ticks=3):
    """Check if price stayed below threshold for consecutive ticks"""
    breach_count = 0
    for price in prices:
        if price < threshold:
            breach_count += 1
            if breach_count >= consecutive_ticks:
                return True
        else:
            breach_count = 0
    return False

def run_working_experiment():
    print("Starting simplified de-peg attack experiment...")
    results = []
    
    total_runs = len(POOL_DEPTHS) * len(ATTACKER_SIZES) * len(USER_REGIMES) * len(ARBITRAGE_MODES)
    run_count = 0
    
    for pool in POOL_DEPTHS:
        for delta_s in ATTACKER_SIZES:
            for user_regime in USER_REGIMES:
                for arb_mode in ARBITRAGE_MODES:
                    breaches = 0
                    for seed in range(N_SEEDS):
                        prices = simulate_price_series(pool, delta_s, user_regime, arb_mode, seed)
                        breached = check_peg_breach(prices)
                        breaches += int(breached)
                    
                    breach_prob = breaches / N_SEEDS
                    results.append({
                        'pool_depth': pool,
                        'delta_s_frac': delta_s,
                        'user_regime': user_regime,
                        'arb_mode': arb_mode,
                        'breach_prob': breach_prob
                    })
                    
                    run_count += 1
                    print(f"Completed run {run_count}/{total_runs}: Pool={pool}, ΔS={delta_s:.1%}, {user_regime}+{arb_mode}, Breach prob={breach_prob:.2%}")
    
    # Save results
    df = pd.DataFrame(results)
    output_file = os.path.join(OUTPUT_DIR, 'depeg_attack_results_working.csv')
    df.to_csv(output_file, index=False)
    print(f'Working experiment results saved to {output_file}')
    
    return df

if __name__ == "__main__":
    df = run_working_experiment()
    print(f"\nExperiment completed! Generated {len(df)} result rows.")
