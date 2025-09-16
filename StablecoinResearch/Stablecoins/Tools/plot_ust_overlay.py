import pandas as pd
import matplotlib.pyplot as plt

# --- User: Set your simulation CSV path here ---
sim_csv = "your_simulation_output.csv"  # <-- update this to your sim output file
real_csv = "ust_hourly_prices_may2022.csv"  # from fetch_ust_prices.py

# --- Try common column names, prompt if not found ---
def get_column(df, options, prompt):
    for col in options:
        if col in df.columns:
            return col
    print(f"Columns found: {list(df.columns)}")
    return input(f"Enter the column name for {prompt}: ")

# --- Load simulation data ---
sim_df = pd.read_csv(sim_csv)
sim_x = get_column(sim_df, ['tick', 'step', 'hour', 'datetime'], 'simulation time (tick or datetime)')
sim_y = get_column(sim_df, ['sim_price', 'price', 'peg', 'stablecoin_price'], 'simulation price')

# --- Load real UST price data ---
real_df = pd.read_csv(real_csv)
real_x = get_column(real_df, ['datetime', 'hour', 'tick'], 'real data time (datetime or tick)')
real_y = get_column(real_df, ['price', 'ust_price'], 'real UST price')

# --- Convert datetimes if needed ---
if 'datetime' in [sim_x, real_x]:
    if sim_x == 'datetime':
        sim_df[sim_x] = pd.to_datetime(sim_df[sim_x])
    if real_x == 'datetime':
        real_df[real_x] = pd.to_datetime(real_df[real_x])

# --- Plot overlay ---
plt.figure(figsize=(12,6))
plt.plot(real_df[real_x], real_df[real_y], label='Real UST Price (CoinGecko)', color='black', linewidth=2)
plt.plot(sim_df[sim_x], sim_df[sim_y], label='Simulated Price', color='red', linestyle='--', linewidth=2)
plt.xlabel('Time (tick or datetime)')
plt.ylabel('UST Price')
plt.title('UST Price: Real vs. Simulated (Terra May 2022)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot to the Diagrams folder
import os
diagram_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Diagrams'))
os.makedirs(diagram_dir, exist_ok=True)
output_path = os.path.join(diagram_dir, 'ust_overlay.png')
plt.savefig(output_path)
print(f"Plot saved to: {output_path}")

plt.show()
