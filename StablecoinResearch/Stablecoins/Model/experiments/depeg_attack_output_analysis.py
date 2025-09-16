"""
depeg_attack_output_analysis.py

Analyze and visualize results from de-peg attack experiments (custom and modular).
Generates heatmaps and extracts minimum attack size for 50% peg breach probability.

IMPORTANT: Set PYTHONPATH to project root before running this script!
In PowerShell:
  $env:PYTHONPATH = (Resolve-Path .).Path
  python Stablecoins/Model/experiments/depeg_attack_output_analysis.py

This ensures that 'from Stablecoins...' imports work correctly.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')

RESULT_FILES = [
    'depeg_attack_results_working.csv',
    'depeg_attack_results_demo.csv',
    'depeg_attack_results_custom.csv',
    'depeg_attack_results_modular.csv'
]

SCENARIO = {'user_regime': 'Panic', 'arb_mode': 'Moderate'}

for result_file in RESULT_FILES:
    path = os.path.join(OUTPUT_DIR, result_file)
    if not os.path.exists(path):
        print(f"File not found: {result_file}")
        continue
    df = pd.read_csv(path)
    print(f"\nLoaded {result_file} with {len(df)} rows.")

    # Filter for scenario of interest
    df_scenario = df[(df['user_regime'] == SCENARIO['user_regime']) & (df['arb_mode'] == SCENARIO['arb_mode'])]
    if df_scenario.empty:
        print(f"No rows for scenario {SCENARIO} in {result_file}")
        continue

    # Pivot for heatmap: rows=pool_depth, cols=delta_s_frac, values=breach_prob
    heatmap_data = df_scenario.pivot(index='pool_depth', columns='delta_s_frac', values='breach_prob')
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='YlOrRd', cbar_kws={'label': 'Peg Breach Probability'})
    plt.title(f"Peg Breach Probability\n{result_file.replace('_', ' ').replace('.csv', '')}\nScenario: {SCENARIO}")
    plt.ylabel('Pool Depth')
    plt.xlabel('Attacker Size (ΔS, fraction of pool)')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"heatmap_{result_file.replace('.csv', '')}.png"))
    plt.close()
    print(f"Saved heatmap for {result_file}.")

    # Extract minimum ΔS for ≥50% breach probability for each pool depth
    min_attack = []
    for pool in sorted(df_scenario['pool_depth'].unique()):
        sub = df_scenario[df_scenario['pool_depth'] == pool]
        candidates = sub[sub['breach_prob'] >= 0.5]
        if not candidates.empty:
            min_ds = candidates.sort_values('delta_s_frac').iloc[0]['delta_s_frac']
        else:
            min_ds = np.nan
        min_attack.append({'pool_depth': pool, 'min_delta_s_50pct': min_ds})
    min_attack_df = pd.DataFrame(min_attack)
    min_attack_df.to_csv(os.path.join(OUTPUT_DIR, f"min_attack_{result_file.replace('.csv', '')}.csv"), index=False)
    print(f"Saved minimum attack size summary for {result_file}.")
