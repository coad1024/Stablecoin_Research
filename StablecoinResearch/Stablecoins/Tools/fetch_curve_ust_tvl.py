# Fetch historical TVL (liquidity) for Curve UST-3pool from DeFiLlama
# Usage: python fetch_curve_ust_tvl.py

import requests
import pandas as pd
from datetime import datetime

# DeFiLlama API endpoint for Curve pool TVL
POOL_ID = 'curve'  # Protocol slug
CHAIN = 'ethereum'  # Chain name
POOL_ADDRESS = '0x45dda9cb7c25131df268515131f647d726f50608'  # Curve UST-3pool (UST-3CRV) address

# DeFiLlama API for pool TVL history
API_URL = f"https://api.llama.fi/v2/historicalChainTvl/{CHAIN}/{POOL_ID}/{POOL_ADDRESS}"

print(f"Fetching TVL data for Curve UST-3pool from DeFiLlama...")
resp = requests.get(API_URL)
data = resp.json()

# Parse data
records = data['tvl'] if 'tvl' in data else data

tvl_df = pd.DataFrame(records)
tvl_df['date'] = pd.to_datetime(tvl_df['date'], unit='s')

# Only keep relevant columns
if 'totalLiquidityUSD' in tvl_df.columns:
    tvl_df = tvl_df[['date', 'totalLiquidityUSD']]
    tvl_df = tvl_df.rename(columns={'totalLiquidityUSD': 'tvl_usd'})
else:
    # Fallback: try 'tvl'
    tvl_df = tvl_df[['date', 'tvl']]
    tvl_df = tvl_df.rename(columns={'tvl': 'tvl_usd'})

# Save to CSV
out_csv = 'curve_ust3pool_tvl.csv'
tvl_df.to_csv(out_csv, index=False)
print(f"Saved: {out_csv}")
