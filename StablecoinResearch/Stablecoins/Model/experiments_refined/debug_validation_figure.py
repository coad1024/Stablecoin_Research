"""
Debug and fix the model validation figure
"""
import json
import numpy as np
import matplotlib.pyplot as plt

# Load data
with open('outputs/streamlined_results.json', 'r') as f:
    results = json.load(f)

print("Debugging the validation figure...")

# Check what data we actually have
pool_1m_data = [r for r in results if r['pool_depth'] == 1_000_000]
pool_10m_data = [r for r in results if r['pool_depth'] == 10_000_000]

print(f"$1M pool data points: {len(pool_1m_data)}")
print(f"$10M pool data points: {len(pool_10m_data)}")

if pool_1m_data:
    print("$1M pool attacks:", [r['attack_size_frac'] for r in pool_1m_data])
    print("$1M pool min prices:", [r['min_price'] for r in pool_1m_data])

if pool_10m_data:
    print("$10M pool attacks:", [r['attack_size_frac'] for r in pool_10m_data])
    print("$10M pool min prices:", [r['min_price'] for r in pool_10m_data])

# Let's recreate the figure with better debugging
fig, ax = plt.subplots(figsize=(10, 7))

# Generate analytic curves
attack_fractions = np.linspace(0.01, 0.15, 100)

# $1M pool analytic (blue)
pool_1m = 1_000_000
analytic_1m = []
for attack_frac in attack_fractions:
    attack_amount = pool_1m * attack_frac
    new_stablecoin = pool_1m + attack_amount
    new_usd = (pool_1m ** 2) / new_stablecoin
    new_price = new_usd / new_stablecoin
    analytic_1m.append(new_price)

ax.plot(attack_fractions * 100, analytic_1m, 
        color='blue', linewidth=3, label='Analytic ($1M pool)', alpha=0.8)

# $10M pool analytic (red)
pool_10m = 10_000_000
analytic_10m = []
for attack_frac in attack_fractions:
    attack_amount = pool_10m * attack_frac
    new_stablecoin = pool_10m + attack_amount
    new_usd = (pool_10m ** 2) / new_stablecoin
    new_price = new_usd / new_stablecoin
    analytic_10m.append(new_price)

ax.plot(attack_fractions * 100, analytic_10m, 
        color='red', linewidth=3, label='Analytic ($10M pool)', alpha=0.8)

# Add simulation points
if pool_1m_data:
    sim_attacks_1m = [r['attack_size_frac'] * 100 for r in pool_1m_data]
    sim_prices_1m = [r['min_price'] for r in pool_1m_data]
    ax.scatter(sim_attacks_1m, sim_prices_1m, 
              color='blue', s=100, alpha=0.8, marker='o',
              label='Simulated ($1M pool)', edgecolors='darkblue', linewidth=2)
    print(f"Plotted {len(sim_attacks_1m)} blue points for $1M pool")

if pool_10m_data:
    sim_attacks_10m = [r['attack_size_frac'] * 100 for r in pool_10m_data]
    sim_prices_10m = [r['min_price'] for r in pool_10m_data]
    ax.scatter(sim_attacks_10m, sim_prices_10m, 
              color='red', s=100, alpha=0.8, marker='s',
              label='Simulated ($10M pool)', edgecolors='darkred', linewidth=2)
    print(f"Plotted {len(sim_attacks_10m)} red points for $10M pool")

# Add peg threshold
ax.axhline(y=0.98, color='orange', linestyle='--', linewidth=2, alpha=0.8,
           label='Peg Threshold ($0.98)')

# Formatting
ax.set_xlabel('Attack Size (% of Pool Depth)', fontsize=12)
ax.set_ylabel('Minimum Price Achieved ($)', fontsize=12)
ax.set_title('Model Validation: Analytic vs Simulated Price Impact\n' +
            'Debugging Version - Should Show Both Blue and Red', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 12)
ax.set_ylim(0.85, 1.05)

plt.tight_layout()
plt.savefig('outputs/Figure3_Debug.png', dpi=300, bbox_inches='tight')
plt.show()

print("Debug figure saved as Figure3_Debug.png")
