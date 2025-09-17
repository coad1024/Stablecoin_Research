"""
Super minimal test
"""
print("Starting test...")

# Simple AMM calculation
pool_size = 1_000_000
stablecoin_reserves = pool_size
usd_reserves = pool_size
k = pool_size ** 2

print(f"Initial reserves: S={stablecoin_reserves}, USD={usd_reserves}")
print(f"Initial price: {usd_reserves / stablecoin_reserves}")

# Simulate selling 50k stablecoin
sell_amount = 50_000
new_stablecoin = stablecoin_reserves + sell_amount
new_usd = k / new_stablecoin
usd_received = usd_reserves - new_usd

print(f"After selling {sell_amount} stablecoin:")
print(f"New reserves: S={new_stablecoin}, USD={new_usd}")
print(f"New price: {new_usd / new_stablecoin}")
print(f"USD received: {usd_received}")

print("Test completed!")
