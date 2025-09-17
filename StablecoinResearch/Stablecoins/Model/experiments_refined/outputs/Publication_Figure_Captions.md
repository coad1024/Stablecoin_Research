# Publication-Ready Figure Captions

## Figure1
**Figure 1. Peg Failure Probability Under Coordinated Attack.** 
Heatmap showing failure probability (color intensity) as a function of pool depth (y-axis) and attack size (x-axis) under panic market conditions with moderate arbitrage response. Each cell represents the proportion of 5 Monte Carlo simulations where the stablecoin price remained below $0.98 for at least 3 consecutive hours following the attack. Results demonstrate that relatively modest attacks (5-10% of pool depth) can achieve 40% failure probability regardless of pool size, indicating that larger liquidity pools do not provide proportional protection against coordinated de-peg attacks.

## Figure2
**Figure 2. Representative Attack Dynamics: Failure vs Recovery Scenarios.** 
Time-series traces showing stablecoin price evolution over 50 hours for two representative simulation runs with identical parameters but different stochastic outcomes. (A) Peg failure scenario where the attack at hour 21 triggers a persistent de-peg below the $0.98 threshold despite arbitrage attempts. (B) Recovery scenario where arbitrage successfully restores the peg within hours of the attack. The grey band indicates the acceptable peg range ($0.98-$1.02). These traces illustrate the binary nature of attack outcomes and the critical role of arbitrage timing in determining whether temporary price disruptions become sustained peg failures.

## Figure3
**Figure 3. Model Validation: Analytic vs Simulated Price Impact.** 
Comparison between theoretical constant-product AMM price impact (solid lines) and simulated minimum prices achieved (scatter points) across different attack sizes and pool depths. The close agreement validates that our stochastic simulation accurately captures the underlying AMM mechanics when arbitrage effects are removed. Deviations between theory and simulation primarily reflect the influence of user behavior and arbitrage response modeled in the simulation. The horizontal dashed line indicates the peg failure threshold ($0.98), showing that attacks exceeding ~8-10% of pool depth are sufficient to breach the peg through direct price impact alone, before considering amplifying effects from user panic.

