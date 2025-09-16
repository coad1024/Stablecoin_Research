"""
depeg_attack_cost_benefit_analysis.py

Economic analysis of de-peg attack costs vs potential profits.
Calculates the financial incentives and break-even points for attackers.

IMPORTANT: Set PYTHONPATH to project root before running this script!
In PowerShell:
  $env:PYTHONPATH = (Resolve-Path .).Path
  python Stablecoins/Model/experiments/depeg_attack_cost_benefit_analysis.py
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')

# Load all experiment results
RESULT_FILES = [
    'depeg_attack_results_working.csv',
    'depeg_attack_results_custom.csv',
    'depeg_attack_results_demo.csv',
    'depeg_attack_results_modular.csv'
]

# Economic parameters for cost-benefit analysis
STABLECOIN_PRICE = 1.0  # Initial peg price
DEPEG_TARGET_PRICE = 0.95  # Target price after attack (5% depeg)
TRANSACTION_FEE_RATE = 0.003  # 0.3% transaction fees
BORROWING_COST_RATE = 0.05  # 5% annual borrowing cost for attack capital
ATTACK_DURATION_DAYS = 1  # Assume attack lasts 1 day

# Profit mechanisms
PROFIT_MECHANISMS = {
    'arbitrage': 'Profit from price difference between pools',
    'short_selling': 'Profit from shorting stablecoin before attack',
    'liquidity_withdrawal': 'Profit from asymmetric liquidity withdrawal',
    'options_trading': 'Profit from put options on stablecoin'
}

def calculate_attack_costs(pool_depth, attack_size_frac):
    """
    Calculate the total cost of executing a de-peg attack.
    
    Args:
        pool_depth (float): Total liquidity in the target pool
        attack_size_frac (float): Attack size as fraction of pool depth
    
    Returns:
        dict: Breakdown of attack costs
    """
    attack_amount = pool_depth * attack_size_frac
    
    # Direct costs
    capital_required = attack_amount * STABLECOIN_PRICE
    transaction_fees = capital_required * TRANSACTION_FEE_RATE
    borrowing_costs = capital_required * BORROWING_COST_RATE * (ATTACK_DURATION_DAYS / 365)
    
    # Opportunity costs
    opportunity_cost = capital_required * 0.04 * (ATTACK_DURATION_DAYS / 365)  # 4% annual opportunity cost
    
    # Risk premium (higher for larger attacks)
    risk_premium = capital_required * (0.02 + attack_size_frac * 0.1) * (ATTACK_DURATION_DAYS / 365)
    
    total_cost = capital_required + transaction_fees + borrowing_costs + opportunity_cost + risk_premium
    
    return {
        'capital_required': capital_required,
        'transaction_fees': transaction_fees,
        'borrowing_costs': borrowing_costs,
        'opportunity_cost': opportunity_cost,
        'risk_premium': risk_premium,
        'total_cost': total_cost
    }

def calculate_arbitrage_profits(pool_depth, attack_size_frac, breach_prob):
    """
    Calculate potential arbitrage profits from successful de-peg attack.
    
    Args:
        pool_depth (float): Total liquidity in the target pool
        attack_size_frac (float): Attack size as fraction of pool depth
        breach_prob (float): Probability of successful peg breach
    
    Returns:
        dict: Potential profit calculations
    """
    attack_amount = pool_depth * attack_size_frac
    
    if breach_prob == 0:
        return {
            'arbitrage_profit': 0,
            'short_profit': 0,
            'expected_arbitrage': 0,
            'expected_short': 0,
            'total_expected_profit': 0
        }
    
    # Arbitrage profit: buy low after depeg, sell at fair value
    price_drop = STABLECOIN_PRICE - DEPEG_TARGET_PRICE  # 0.05 for 5% depeg
    arbitrage_volume = min(attack_amount, pool_depth * 0.5)  # Limited by available volume
    arbitrage_profit = arbitrage_volume * price_drop * 0.8  # 80% efficiency due to slippage
    
    # Short selling profit: sell high before attack, buy back low after
    short_position = attack_amount * 0.3  # Assume 30% of attack amount as short position
    short_profit = short_position * price_drop * 0.9  # 90% efficiency
    
    # Expected profits (adjusted for breach probability)
    expected_arbitrage = arbitrage_profit * breach_prob
    expected_short = short_profit * breach_prob
    total_expected_profit = expected_arbitrage + expected_short
    
    return {
        'arbitrage_profit': arbitrage_profit,
        'short_profit': short_profit,
        'expected_arbitrage': expected_arbitrage,
        'expected_short': expected_short,
        'total_expected_profit': total_expected_profit
    }

def calculate_liquidity_withdrawal_profits(pool_depth, attack_size_frac, breach_prob):
    """
    Calculate profits from asymmetric liquidity withdrawal during depeg.
    """
    if breach_prob == 0:
        return 0
    
    # Profit from withdrawing liquidity at unfavorable prices for the pool
    withdrawal_amount = pool_depth * 0.1  # Withdraw 10% of pool
    price_advantage = 0.02  # 2% price advantage during chaos
    withdrawal_profit = withdrawal_amount * price_advantage * breach_prob
    
    return withdrawal_profit

def analyze_cost_benefit_for_results(results_file):
    """
    Perform cost-benefit analysis for a specific results file.
    """
    df = pd.read_csv(os.path.join(OUTPUT_DIR, results_file))
    
    analysis_results = []
    
    for _, row in df.iterrows():
        pool_depth = row['pool_depth']
        attack_size_frac = row['delta_s_frac']
        breach_prob = row['breach_prob']
        
        # Calculate costs
        costs = calculate_attack_costs(pool_depth, attack_size_frac)
        
        # Calculate profits
        arbitrage_profits = calculate_arbitrage_profits(pool_depth, attack_size_frac, breach_prob)
        liquidity_profit = calculate_liquidity_withdrawal_profits(pool_depth, attack_size_frac, breach_prob)
        
        total_expected_profit = arbitrage_profits['total_expected_profit'] + liquidity_profit
        
        # Calculate metrics
        net_expected_profit = total_expected_profit - costs['total_cost']
        roi = (net_expected_profit / costs['capital_required']) * 100 if costs['capital_required'] > 0 else 0
        profit_margin = (net_expected_profit / total_expected_profit) * 100 if total_expected_profit > 0 else -100
        
        analysis_results.append({
            'pool_depth': pool_depth,
            'delta_s_frac': attack_size_frac,
            'user_regime': row['user_regime'],
            'arb_mode': row['arb_mode'],
            'breach_prob': breach_prob,
            'capital_required': costs['capital_required'],
            'total_cost': costs['total_cost'],
            'expected_profit': total_expected_profit,
            'net_profit': net_expected_profit,
            'roi_percent': roi,
            'profit_margin_percent': profit_margin,
            'economically_viable': net_expected_profit > 0
        })
    
    return pd.DataFrame(analysis_results)

def generate_cost_benefit_summary():
    """
    Generate cost-benefit analysis for all experiment results.
    """
    print("Starting cost-benefit analysis for de-peg attacks...")
    
    all_analyses = {}
    
    for results_file in RESULT_FILES:
        file_path = os.path.join(OUTPUT_DIR, results_file)
        if os.path.exists(file_path):
            print(f"Analyzing {results_file}...")
            approach_name = results_file.replace('depeg_attack_results_', '').replace('.csv', '')
            analysis_df = analyze_cost_benefit_for_results(results_file)
            
            # Save detailed analysis
            output_file = f"cost_benefit_analysis_{approach_name}.csv"
            analysis_df.to_csv(os.path.join(OUTPUT_DIR, output_file), index=False)
            print(f"Saved detailed analysis to {output_file}")
            
            all_analyses[approach_name] = analysis_df
        else:
            print(f"File not found: {results_file}")
    
    return all_analyses

def create_economic_viability_heatmaps(all_analyses):
    """
    Create heatmaps showing economic viability of attacks.
    """
    print("Creating economic viability heatmaps...")
    
    for approach_name, df in all_analyses.items():
        # Create heatmap for ROI
        pivot_roi = df.pivot_table(
            values='roi_percent', 
            index='delta_s_frac', 
            columns='pool_depth', 
            aggfunc='mean'
        )
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            pivot_roi, 
            annot=True, 
            fmt='.1f', 
            cmap='RdYlGn', 
            center=0,
            cbar_kws={'label': 'ROI (%)'}
        )
        plt.title(f'Attack ROI Heatmap - {approach_name.title()} Approach')
        plt.xlabel('Pool Depth ($)')
        plt.ylabel('Attack Size (fraction of pool)')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, f'roi_heatmap_{approach_name}.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Create heatmap for economic viability
        pivot_viable = df.pivot_table(
            values='economically_viable', 
            index='delta_s_frac', 
            columns='pool_depth', 
            aggfunc='mean'
        )
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            pivot_viable, 
            annot=True, 
            fmt='.2f', 
            cmap='RdYlGn', 
            vmin=0, 
            vmax=1,
            cbar_kws={'label': 'Economic Viability (0-1)'}
        )
        plt.title(f'Economic Viability Heatmap - {approach_name.title()} Approach')
        plt.xlabel('Pool Depth ($)')
        plt.ylabel('Attack Size (fraction of pool)')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, f'viability_heatmap_{approach_name}.png'), dpi=300, bbox_inches='tight')
        plt.close()

def generate_summary_statistics(all_analyses):
    """
    Generate summary statistics across all approaches.
    """
    print("Generating summary statistics...")
    
    summary_stats = []
    
    for approach_name, df in all_analyses.items():
        viable_attacks = df[df['economically_viable'] == True]
        
        stats = {
            'approach': approach_name,
            'total_scenarios': len(df),
            'viable_scenarios': len(viable_attacks),
            'viability_rate': len(viable_attacks) / len(df) * 100,
            'avg_roi_all': df['roi_percent'].mean(),
            'avg_roi_viable': viable_attacks['roi_percent'].mean() if len(viable_attacks) > 0 else 0,
            'max_roi': df['roi_percent'].max(),
            'min_attack_size_viable': viable_attacks['delta_s_frac'].min() if len(viable_attacks) > 0 else np.nan,
            'avg_capital_required': df['capital_required'].mean(),
            'max_profit': df['expected_profit'].max()
        }
        
        summary_stats.append(stats)
    
    summary_df = pd.DataFrame(summary_stats)
    summary_df.to_csv(os.path.join(OUTPUT_DIR, 'cost_benefit_summary.csv'), index=False)
    print("Saved summary statistics to cost_benefit_summary.csv")
    
    return summary_df

if __name__ == "__main__":
    # Perform cost-benefit analysis
    all_analyses = generate_cost_benefit_summary()
    
    # Create visualizations
    create_economic_viability_heatmaps(all_analyses)
    
    # Generate summary statistics
    summary_df = generate_summary_statistics(all_analyses)
    
    print("\n=== COST-BENEFIT ANALYSIS COMPLETE ===")
    print(f"Generated analysis for {len(all_analyses)} approaches")
    print("Files created:")
    print("- cost_benefit_analysis_[approach].csv (detailed analysis)")
    print("- roi_heatmap_[approach].png (ROI heatmaps)")
    print("- viability_heatmap_[approach].png (economic viability)")
    print("- cost_benefit_summary.csv (summary statistics)")
    
    print("\nSummary of Economic Viability:")
    for _, row in summary_df.iterrows():
        print(f"{row['approach'].title()}: {row['viability_rate']:.1f}% scenarios profitable, "
              f"avg ROI: {row['avg_roi_all']:.1f}%")
