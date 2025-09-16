"""
depeg_attack_experiment_modular.py

Runs de-peg attack experiments using the modular ThreePoolsSimulation class, sweeping user/arbitrage regimes.

IMPORTANT: Set PYTHONPATH to project root before running this script!
In PowerShell:
  $env:PYTHONPATH = (Resolve-Path .).Path
  python Stablecoins/Model/experiments/depeg_attack_experiment_modular.py

This ensures that 'from Stablecoins...' imports work correctly.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import os
import numpy as np
import pandas as pd
from Stablecoins.Simulations.DualTokenSim.source.Tokens.algorithmic_stablecoin import AlgorithmicStablecoin
from Stablecoins.Simulations.DualTokenSim.source.Tokens.collateral_token import CollateralToken
from Stablecoins.Simulations.DualTokenSim.source.Tokens.reference_token import ReferenceToken
from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.liquidity_pool import LiquidityPool
from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.constant_product_formula import ConstantProductFormula
from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.simple_virtual_liquidity_pool import SimpleVirtualLiquidityPool
from Stablecoins.Simulations.DualTokenSim.source.purchase_generators.seignorage_model_random_purchase_generator import SeignorageModelRandomPurchaseGenerator
from Stablecoins.Simulations.DualTokenSim.source.simulations.three_pools_simulation import ThreePoolsSimulation

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

POOL_DEPTHS = [100_000, 1_000_000, 5_000_000, 10_000_000]
ATTACKER_SIZES = [0.005, 0.01, 0.025, 0.05, 0.10]
N_SEEDS = 30
PEG_BREACH_THRESHOLD = 0.98
PEG_BREACH_TICKS = 3
N_TICKS = 50
ATTACK_TICK = 21

USER_REGIMES = {
    'Normal': lambda pool_depth: np.random.normal(0, pool_depth * 0.0005),
    'Panic': lambda pool_depth: np.random.normal(-pool_depth * 0.002, pool_depth * 0.002)
}
def fast_arbitrage(price_gap, pool):
    pool.quantity_token_b += price_gap * pool.quantity_token_a * 0.95

def moderate_arbitrage(price_gap, pool):
    if np.random.rand() < 0.5:
        pool.quantity_token_b += price_gap * pool.quantity_token_a * 0.6

def slow_arbitrage(price_gap, pool):
    if np.random.rand() < 0.2:
        pool.quantity_token_b += price_gap * pool.quantity_token_a * 0.3

ARBITRAGE_MODES = {
    'Fast': fast_arbitrage,
    'Moderate': moderate_arbitrage,
    'Slow': slow_arbitrage
}

def run_modular_experiment():
    results = []
    for pool_depth in POOL_DEPTHS:
        for delta_s in ATTACKER_SIZES:
            for user_regime_name, user_regime_fn in USER_REGIMES.items():
                for arb_mode_name, arb_fn in ARBITRAGE_MODES.items():
                    breaches = 0
                    for seed in range(N_SEEDS):
                        np.random.seed(seed)
                        # --- Initialize simulation ---
                        large_supply = pool_depth * 10  # Large supply to handle swaps
                        stable = AlgorithmicStablecoin('S', large_supply, large_supply * 0.95, 1.0, 1.0)  # 95% free supply
                        collat = CollateralToken('C', large_supply, large_supply * 0.95, 1.0, stable)
                        ref = ReferenceToken('R')  # ReferenceToken only needs name
                        formula = ConstantProductFormula()
                        stable_pool = LiquidityPool(stable, collat, pool_depth, pool_depth, 0.0, formula)
                        collat_pool = LiquidityPool(collat, ref, pool_depth, pool_depth, 0.0, formula)
                        virt_pool = SimpleVirtualLiquidityPool(stable, collat, pool_depth, 0.0, formula, 100)  # 100 tick recovery period
                        # Purchase generators
                        pg1 = SeignorageModelRandomPurchaseGenerator(stable)
                        pg2 = SeignorageModelRandomPurchaseGenerator(collat)
                        sim = ThreePoolsSimulation(stable, collat, ref, stable_pool, collat_pool, virt_pool, pg1, pg2, N_TICKS)
                        breached = sim.run_depeg_attack(ATTACK_TICK, delta_s, user_regime_fn, arb_fn, PEG_BREACH_THRESHOLD, PEG_BREACH_TICKS)
                        breaches += int(breached)
                    breach_prob = breaches / N_SEEDS
                    results.append({
                        'pool_depth': pool_depth,
                        'delta_s_frac': delta_s,
                        'user_regime': user_regime_name,
                        'arb_mode': arb_mode_name,
                        'breach_prob': breach_prob
                    })
    df = pd.DataFrame(results)
    df.to_csv(os.path.join(OUTPUT_DIR, 'depeg_attack_results_modular.csv'), index=False)
    print('Modular experiment results saved to outputs/depeg_attack_results_modular.csv')

if __name__ == "__main__":
    run_modular_experiment()
