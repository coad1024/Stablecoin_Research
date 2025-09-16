# Fetch UST hourly price data from CoinGecko for May 7–12, 2022
# Usage: python fetch_ust_prices.py

import requests
import pandas as pd
from datetime import datetime, timedelta

# CoinGecko API endpoint for historical market chart
COINGECKO_API = "https://api.coingecko.com/api/v3/coins/terrausd/market_chart/range"

# Define time window: May 7, 2022 00:00 UTC to May 12, 2022 23:59 UTC
start_dt = datetime(2022, 5, 7)
end_dt = datetime(2022, 5, 12, 23, 59)

# Convert to UNIX timestamps (milliseconds)
start_ts = int(start_dt.timestamp())
end_ts = int(end_dt.timestamp())

params = {
    'vs_currency': 'usd',
    'from': start_ts,
    'to': end_ts
}

print(f"Fetching UST price data from {start_dt} to {end_dt}...")
resp = requests.get(COINGECKO_API, params=params)
data = resp.json()

# Extract hourly prices (timestamp, price)
prices = data['prices']  # Each entry: [timestamp_ms, price]

# Convert to DataFrame
price_df = pd.DataFrame(prices, columns=['timestamp_ms', 'price'])
price_df['datetime'] = pd.to_datetime(price_df['timestamp_ms'], unit='ms')
price_df = price_df.set_index('datetime').resample('1H').mean().reset_index()

# Save to CSV
price_df[['datetime', 'price']].to_csv('ust_hourly_prices_may2022.csv', index=False)
print("Saved: ust_hourly_prices_may2022.csv")
