"""
depeg_attack_experiment_custom.py

Custom simulation loop for de-peg attack experiment using DualTokenSim primitives.

IMPORTANT: Set PYTHONPATH to project root before running this script!
In PowerShell:
  $env:PYTHONPATH = (Resolve-Path .).Path
  python Stablecoins/Model/experiments/depeg_attack_experiment_custom.py

This ensures that 'from Stablecoins...' imports work correctly.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import numpy as np
import pandas as pd
from tqdm import tqdm

from Stablecoins.Simulations.DualTokenSim.source.Tokens.algorithmic_stablecoin import AlgorithmicStablecoin
from Stablecoins.Simulations.DualTokenSim.source.Tokens.collateral_token import CollateralToken
from Stablecoins.Simulations.DualTokenSim.source.Tokens.reference_token import ReferenceToken
from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.liquidity_pool import LiquidityPool
from Stablecoins.Simulations.DualTokenSim.source.liquidity_pools.constant_product_formula import ConstantProductFormula
from Stablecoins.Simulations.DualTokenSim.source.market_simulators.market_simulator import MarketSimulator
from Stablecoins.Simulations.DualTokenSim.source.arbitrage_optimizer.three_pools_arbitrage_optimizer import ThreePoolsArbitrageOptimizer

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

POOL_DEPTHS = [100_000, 1_000_000, 5_000_000, 10_000_000]
ATTACKER_SIZES = [0.005, 0.01, 0.025, 0.05, 0.10]
N_SEEDS = 30
PEG_BREACH_THRESHOLD = 0.98
PEG_BREACH_TICKS = 3
N_TICKS = 50
ATTACK_TICK = 21

# --- User trade regimes ---
USER_REGIMES = {
    'Normal': lambda pool_depth: np.random.normal(0, pool_depth * 0.0005),
    'Panic': lambda pool_depth: np.random.normal(-pool_depth * 0.002, pool_depth * 0.002)
}

# --- Arbitrage regimes as functions ---
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

# --- Custom simulation loop ---
def run_single_custom_sim(pool_depth, delta_s_frac, user_regime, arb_mode, seed):
    np.random.seed(seed)
    # 1. Initialize tokens with LARGE free supplies to handle big swaps
    large_supply = pool_depth * 10  # 10x pool depth to handle large swaps
    stable = AlgorithmicStablecoin('S', large_supply, large_supply * 0.95, 1.0, 1.0)  # 95% free supply
    collat = CollateralToken('C', large_supply, large_supply * 0.95, 1.0, stable)
    ref = ReferenceToken('R')  # ReferenceToken only needs name
    # 2. Initialize pool (constant product, no fee)
    formula = ConstantProductFormula()
    pool = LiquidityPool(stable, collat, pool_depth, pool_depth, 0.0, formula)
    # 3. Arbitrage optimizer (stub)
    arb = ThreePoolsArbitrageOptimizer([pool], None)
    # 4. Market simulator (stub, not used)
    # 5. Run ticks
    price_hist = []
    peg_breach_count = 0
    for t in range(N_TICKS):
        # Attacker dumps at ATTACK_TICK
        if t == ATTACK_TICK:
            attacker_amt = pool_depth * delta_s_frac
            pool.swap(stable, attacker_amt)
        # User trade
        user_trade = USER_REGIMES[user_regime](pool_depth)
        pool.swap(stable, user_trade)
        # Arbitrage
        price_gap = 1.0 - (pool.quantity_token_b / pool.quantity_token_a)
        ARBITRAGE_MODES[arb_mode](price_gap, pool)
        # Record price
        price = pool.quantity_token_b / pool.quantity_token_a
        price_hist.append(price)
        # Peg breach logic
        if price < PEG_BREACH_THRESHOLD:
            peg_breach_count += 1
        else:
            peg_breach_count = 0
        if peg_breach_count >= PEG_BREACH_TICKS:
            return True  # Peg breached
    return False  # No breach

def run_custom_experiment():
    results = []
    for pool in POOL_DEPTHS:
        for delta_s in ATTACKER_SIZES:
            for user_regime in USER_REGIMES:
                for arb_mode in ARBITRAGE_MODES:
                    breaches = 0
                    for seed in range(N_SEEDS):
                        breached = run_single_custom_sim(pool, delta_s, user_regime, arb_mode, seed)
                        breaches += int(breached)
                    breach_prob = breaches / N_SEEDS
                    results.append({
                        'pool_depth': pool,
                        'delta_s_frac': delta_s,
                        'user_regime': user_regime,
                        'arb_mode': arb_mode,
                        'breach_prob': breach_prob
                    })
    df = pd.DataFrame(results)
    df.to_csv(os.path.join(OUTPUT_DIR, 'depeg_attack_results_custom.csv'), index=False)
    print('Custom experiment results saved to outputs/depeg_attack_results_custom.csv')

if __name__ == "__main__":
    print("Starting custom de-peg attack experiment...")
    run_custom_experiment()
    print("Experiment completed!")
