import os
import sys
sys.path.append(os.path.abspath('.'))

print("Starting simple experiment test...")

try:
    from Stablecoins.Simulations.DualTokenSim.source.Tokens.algorithmic_stablecoin import AlgorithmicStablecoin
    from Stablecoins.Simulations.DualTokenSim.source.Tokens.collateral_token import CollateralToken
    from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.liquidity_pool import LiquidityPool
    from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.constant_product_formula import ConstantProductFormula
    
    print("All imports successful!")
    
    # Test simple simulation setup
    pool_depth = 100_000
    stable = AlgorithmicStablecoin('S', pool_depth, pool_depth, 1.0, 1.0)
    collat = CollateralToken('C', pool_depth, pool_depth, 1.0, stable)
    formula = ConstantProductFormula()
    pool = LiquidityPool(stable, collat, pool_depth, pool_depth, 0.0, formula)
    
    print(f"Pool created: {pool}")
    print(f"Initial stablecoin price: {stable.price}")
    print(f"Initial pool ratio: {pool.quantity_token_b / pool.quantity_token_a}")
    
    # Test a simple swap
    pool.swap(stable, 1000)
    print(f"After swap - Pool ratio: {pool.quantity_token_b / pool.quantity_token_a}")
    
    print("Simple test completed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
