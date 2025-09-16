"""
Enhanced Cost-Benefit Analysis with Realistic Profit Mechanisms
===============================================================

This analysis includes more sophisticated profit mechanisms that real attackers might use:
1. Flash loans to reduce capital requirements
2. Options strategies (puts, calls) 
3. Leveraged shorting
4. Cross-platform arbitrage
5. MEV (Maximal Extractable Value) opportunities
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')

def enhanced_profit_analysis(pool_depth, attack_size_frac, breach_prob):
    """
    Enhanced profit calculation including sophisticated attack strategies.
    """
    if breach_prob == 0:
        return {'total_enhanced_profit': 0, 'breakdown': {}}
    
    attack_amount = pool_depth * attack_size_frac
    depeg_magnitude = 0.05  # 5% price drop
    
    profits = {}
    
    # 1. Flash Loan Arbitrage (no capital required)
    flash_arbitrage_volume = min(attack_amount * 2, pool_depth)  # Can arbitrage 2x attack amount
    profits['flash_arbitrage'] = flash_arbitrage_volume * depeg_magnitude * 0.7 * breach_prob
    
    # 2. Options Strategy Profits (put options bought before attack)
    options_notional = attack_amount * 0.5  # 50% of attack size in put options
    options_multiplier = 10  # Options provide 10x leverage on price movements
    profits['options_profit'] = options_notional * options_multiplier * depeg_magnitude * breach_prob
    
    # 3. Leveraged Short Selling (5x leverage)
    short_position = attack_amount * 0.3  # 30% of attack amount
    leverage = 5
    profits['leveraged_short'] = short_position * leverage * depeg_magnitude * breach_prob
    
    # 4. Cross-Platform Arbitrage
    # Profit from price differences across multiple DEXs/CEXs
    cross_platform_volume = pool_depth * 0.2
    profits['cross_platform_arb'] = cross_platform_volume * depeg_magnitude * 0.6 * breach_prob
    
    # 5. MEV Opportunities (sandwich attacks, front-running)
    mev_volume = attack_amount * 0.1
    profits['mev_extraction'] = mev_volume * 0.02 * breach_prob  # 2% MEV extraction rate
    
    # 6. Liquidity Pool Manipulation
    # Profit from providing/withdrawing liquidity at optimal times
    lp_manipulation_profit = pool_depth * 0.01 * breach_prob  # 1% of pool depth
    profits['lp_manipulation'] = lp_manipulation_profit
    
    total_enhanced_profit = sum(profits.values())
    
    return {
        'total_enhanced_profit': total_enhanced_profit,
        'breakdown': profits
    }

def enhanced_cost_analysis(pool_depth, attack_size_frac):
    """
    Enhanced cost calculation considering flash loans and leveraged strategies.
    """
    attack_amount = pool_depth * attack_size_frac
    
    # With flash loans, capital requirement is much lower
    flash_loan_fee = attack_amount * 0.0009  # 0.09% flash loan fee
    
    # Only need capital for:
    # 1. Options premiums (typically 2-5% of notional)
    options_premium = attack_amount * 0.5 * 0.03  # 3% premium on 50% of attack size
    
    # 2. Margin for leveraged short (20% margin requirement)
    short_margin = attack_amount * 0.3 * 0.2  # 20% margin on 30% short position
    
    # 3. Transaction fees and slippage
    transaction_costs = attack_amount * 0.005  # 0.5% total transaction costs
    
    # 4. Risk premium for sophisticated attack
    risk_premium = attack_amount * 0.01  # 1% risk premium
    
    total_capital_required = options_premium + short_margin + transaction_costs + risk_premium
    total_cost = total_capital_required + flash_loan_fee
    
    return {
        'capital_required': total_capital_required,
        'flash_loan_fee': flash_loan_fee,
        'total_cost': total_cost,
        'breakdown': {
            'options_premium': options_premium,
            'short_margin': short_margin,
            'transaction_costs': transaction_costs,
            'risk_premium': risk_premium
        }
    }

def run_enhanced_analysis():
    """
    Run enhanced cost-benefit analysis for all approaches.
    """
    print("Running enhanced cost-benefit analysis...")
    
    RESULT_FILES = [
        'depeg_attack_results_working.csv',
        'depeg_attack_results_custom.csv',
        'depeg_attack_results_demo.csv',
        'depeg_attack_results_modular.csv'
    ]
    
    enhanced_results = {}
    
    for results_file in RESULT_FILES:
        file_path = os.path.join(OUTPUT_DIR, results_file)
        if not os.path.exists(file_path):
            continue
            
        df = pd.read_csv(file_path)
        approach_name = results_file.replace('depeg_attack_results_', '').replace('.csv', '')
        
        enhanced_analysis = []
        
        for _, row in df.iterrows():
            pool_depth = row['pool_depth']
            attack_size_frac = row['delta_s_frac']
            breach_prob = row['breach_prob']
            
            # Enhanced calculations
            costs = enhanced_cost_analysis(pool_depth, attack_size_frac)
            profits = enhanced_profit_analysis(pool_depth, attack_size_frac, breach_prob)
            
            net_profit = profits['total_enhanced_profit'] - costs['total_cost']
            roi = (net_profit / costs['capital_required']) * 100 if costs['capital_required'] > 0 else 0
            
            enhanced_analysis.append({
                'pool_depth': pool_depth,
                'delta_s_frac': attack_size_frac,
                'user_regime': row['user_regime'],
                'arb_mode': row['arb_mode'],
                'breach_prob': breach_prob,
                'capital_required': costs['capital_required'],
                'total_cost': costs['total_cost'],
                'expected_profit': profits['total_enhanced_profit'],
                'net_profit': net_profit,
                'roi_percent': roi,
                'economically_viable': net_profit > 0,
                'profit_breakdown': profits['breakdown']
            })
        
        enhanced_df = pd.DataFrame(enhanced_analysis)
        enhanced_results[approach_name] = enhanced_df
        
        # Save results
        output_file = f"enhanced_cost_benefit_{approach_name}.csv"
        enhanced_df.to_csv(os.path.join(OUTPUT_DIR, output_file), index=False)
        print(f"Saved enhanced analysis to {output_file}")
    
    return enhanced_results

def create_enhanced_summary(enhanced_results):
    """
    Create summary of enhanced cost-benefit analysis.
    """
    print("Creating enhanced summary...")
    
    summary_stats = []
    
    for approach_name, df in enhanced_results.items():
        viable_attacks = df[df['economically_viable'] == True]
        
        stats = {
            'approach': approach_name,
            'total_scenarios': len(df),
            'viable_scenarios': len(viable_attacks),
            'viability_rate': len(viable_attacks) / len(df) * 100 if len(df) > 0 else 0,
            'avg_roi_all': df['roi_percent'].mean(),
            'avg_roi_viable': viable_attacks['roi_percent'].mean() if len(viable_attacks) > 0 else 0,
            'max_roi': df['roi_percent'].max(),
            'min_viable_attack_size': viable_attacks['delta_s_frac'].min() if len(viable_attacks) > 0 else np.nan,
            'max_viable_attack_size': viable_attacks['delta_s_frac'].max() if len(viable_attacks) > 0 else np.nan,
            'avg_capital_required': df['capital_required'].mean(),
            'max_profit': df['expected_profit'].max(),
            'avg_net_profit_viable': viable_attacks['net_profit'].mean() if len(viable_attacks) > 0 else 0
        }
        
        summary_stats.append(stats)
    
    summary_df = pd.DataFrame(summary_stats)
    summary_df.to_csv(os.path.join(OUTPUT_DIR, 'enhanced_cost_benefit_summary.csv'), index=False)
    
    return summary_df

def create_enhanced_visualizations(enhanced_results):
    """
    Create visualizations for enhanced cost-benefit analysis.
    """
    print("Creating enhanced visualizations...")
    
    for approach_name, df in enhanced_results.items():
        # ROI heatmap
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
            fmt='.0f', 
            cmap='RdYlGn', 
            center=0,
            cbar_kws={'label': 'ROI (%)'}
        )
        plt.title(f'Enhanced Attack ROI - {approach_name.title()} Approach')
        plt.xlabel('Pool Depth ($)')
        plt.ylabel('Attack Size (fraction of pool)')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, f'enhanced_roi_heatmap_{approach_name}.png'), dpi=300, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    # Run enhanced analysis
    enhanced_results = run_enhanced_analysis()
    
    # Create summary and visualizations
    summary_df = create_enhanced_summary(enhanced_results)
    create_enhanced_visualizations(enhanced_results)
    
    print("\n=== ENHANCED COST-BENEFIT ANALYSIS COMPLETE ===")
    print("Enhanced analysis considers:")
    print("- Flash loan arbitrage (minimal capital)")
    print("- Options strategies (10x leverage)")
    print("- Leveraged short selling (5x leverage)")
    print("- Cross-platform arbitrage")
    print("- MEV extraction")
    print("- Liquidity pool manipulation")
    
    print("\nEnhanced Economic Viability Summary:")
    for _, row in summary_df.iterrows():
        viable_rate = row['viability_rate']
        max_roi = row['max_roi']
        approach = row['approach'].title()
        
        if viable_rate > 0:
            min_attack = row['min_viable_attack_size']
            max_attack = row['max_viable_attack_size']
            print(f"{approach}: {viable_rate:.1f}% scenarios profitable, "
                  f"max ROI: {max_roi:.0f}%, viable attack range: {min_attack:.1%}-{max_attack:.1%}")
        else:
            print(f"{approach}: No economically viable attacks found")
