"""
Convert streamlined JSON results to CSV format for comparison
"""
import json
import os

# Read JSON results
with open('outputs/streamlined_results.json', 'r') as f:
    results = json.load(f)

# Create CSV content
csv_lines = ['pool_depth,attack_size_frac,seed,peg_failure,min_price,profit,final_price,user_regime,arbitrage_mode']

for result in results:
    # Add missing columns for compatibility
    result['user_regime'] = 'Panic'
    result['arbitrage_mode'] = 'Moderate'
    
    csv_line = f"{result['pool_depth']},{result['attack_size_frac']},{result['seed']}," \
               f"{result['peg_failure']},{result['min_price']},{result['profit']}," \
               f"{result['final_price']},{result['user_regime']},{result['arbitrage_mode']}"
    csv_lines.append(csv_line)

# Write CSV
with open('outputs/refined_depeg_attack_results_streamlined.csv', 'w') as f:
    f.write('\n'.join(csv_lines))

print("Converted JSON to CSV format")
print(f"Created: outputs/refined_depeg_attack_results_streamlined.csv")
print(f"Records: {len(results)}")
