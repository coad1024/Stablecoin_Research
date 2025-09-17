# Diagram Iteration Journal

## 2025-09-11 – Initial Stock & Flow Diagram
- Created `mermaid_syntax_stock_flow.md` capturing core system dynamics (UST supply, LUNA market cap, system confidence).
- Distinguished element categories: stocks, flows, external inputs.
- Established primary feedback paths (arbitrage → mint/burn → supply; confidence → panic selling).

## 2025-09-11 – Copy for Experimentation
- Added `mermaid_syntax_stock_flow_copy.md` as a sandbox for future stylistic or structural experiments.
- Maintains identical content to baseline for diff-based evolution tracking.

## 2025-09-11 – Fragility & Regulatory Layer Added
- Appended new section "Algorithmic Stablecoin Fragility & Safeguards" to `mermaid_syntax_stock_flow.md`.
- Modeled three core fragility dependencies explicitly:
  1. Demand support
  2. Incentivized arbitrage actors
  3. Reliable price/oracle information
- Added stressor nodes (Financial Crisis / Extreme Volatility, Information Opaqueness) and failure states (Run, De-Peg Spiral).
- Introduced regulatory mitigation cluster (registration, taxonomy, prudential, custody, transparency, disclosure, containment) with causal mitigation edges.
- Clarified systemic deterioration loop (Run → De-Peg → weakened demand/arbitrage → deeper instability).

## Rationale for Extensions
- Evolves from structural representation → systemic fragility mapping → policy/control surfaces.
- Supports future addition of quantitative annotations (e.g., thresholds, elasticity coefficients) if modeling advances.

## Potential Next Iterations
- Add balancing vs reinforcing loop annotations (B / R markers) to highlight dynamic polarity.
- Layer oracle failure modes (latency, manipulation risk, divergence metric).
- Attach estimated sensitivity weights once empirical calibration data gathered.
- Consider exporting canonical SVG snapshots per major revision for citation stability.

## File References
- Core + extended diagram: `Stablecoins/Tools/mermaid_syntax_stock_flow.md`
- Working copy: `Stablecoins/Tools/mermaid_syntax_stock_flow_copy.md`
- Journal: `Stablecoins/Notes/diagram_iteration_journal.md`

End of current iteration log.
