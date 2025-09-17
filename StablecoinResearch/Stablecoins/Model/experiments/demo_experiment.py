import os
import numpy as np
import pandas as pd

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Starting minimal de-peg attack experiment...")

# Simulate results for demonstration
results = []
pool_depths = [100_000, 1_000_000, 5_000_000, 10_000_000]
attacker_sizes = [0.005, 0.01, 0.025, 0.05, 0.10]
user_regimes = ['Normal', 'Panic']
arb_modes = ['Fast', 'Moderate', 'Slow']

for pool in pool_depths:
    for delta_s in attacker_sizes:
        for user_regime in user_regimes:
            for arb_mode in arb_modes:
                # Simulate breach probability (higher for larger attacks, panic conditions, slower arbitrage)
                base_prob = delta_s * 2  # Base probability proportional to attack size
                if user_regime == 'Panic':
                    base_prob *= 1.5
                if arb_mode == 'Slow':
                    base_prob *= 1.3
                elif arb_mode == 'Fast':
                    base_prob *= 0.7
                
                # Add some randomness and cap at 1.0
                breach_prob = min(1.0, base_prob + np.random.normal(0, 0.1))
                breach_prob = max(0.0, breach_prob)
                
                results.append({
                    'pool_depth': pool,
                    'delta_s_frac': delta_s,
                    'user_regime': user_regime,
                    'arb_mode': arb_mode,
                    'breach_prob': breach_prob
                })

df = pd.DataFrame(results)
df.to_csv(os.path.join(OUTPUT_DIR, 'depeg_attack_results_demo.csv'), index=False)
print(f"Results saved to {os.path.join(OUTPUT_DIR, 'depeg_attack_results_demo.csv')}")
print(f"Generated {len(results)} simulation results")
print("\nSample results:")
print(df.head(10))
