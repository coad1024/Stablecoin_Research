print("Script starting...")
try:
    import os
    import sys
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Test imports
    print("Testing imports...")
    from Stablecoins.Simulations.DualTokenSim.source.Tokens.algorithmic_stablecoin import AlgorithmicStablecoin
    print("AlgorithmicStablecoin import successful")
    
    from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.constant_product_formula import ConstantProductFormula
    print("ConstantProductFormula import successful")
    
    # Test outputs directory
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
    print(f"Output directory: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Output directory created successfully")
    
    print("All tests passed!")
    
except Exception as e:
    print(f"Error occurred: {e}")
    import traceback
    traceback.print_exc()
