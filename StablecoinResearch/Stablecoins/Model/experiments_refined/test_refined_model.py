"""
Quick test of the refined model to verify functionality
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

# Import and test the classes
exec(open('refined_depeg_attack_simulation.py').read())

print("Testing SimplifiedAMM...")
amm = SimplifiedAMM(1_000_000)
print(f"Initial price: ${amm.price:.4f}")
print(f"Initial reserves: S={amm.stablecoin_reserve:,.0f}, USD=${amm.usd_reserve:,.0f}")

# Test a swap
usd_received = amm.execute_swap(50_000)  # Sell 50K stablecoin
print(f"After selling 50K stablecoin: Price=${amm.price:.4f}, USD received=${usd_received:,.0f}")

print("\nTesting RefinedDepegSimulation...")
sim = RefinedDepegSimulation(
    pool_depth=1_000_000,
    attack_size_frac=0.05,
    user_regime='Panic',
    arbitrage_mode='Moderate',
    seed=42
)

print("Running single simulation...")
result = sim.run_simulation()

print("Results:")
print(f"- Peg failure: {result['peg_failure']}")
print(f"- Min price: ${result['min_price']:.4f}")
print(f"- Attacker profit: ${result['profit']:,.0f}")
print(f"- Final price: ${result['final_price']:.4f}")

print("\nTest completed successfully!")
