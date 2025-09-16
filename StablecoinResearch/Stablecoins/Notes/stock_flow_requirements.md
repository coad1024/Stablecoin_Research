# Stock and Flow Diagram: Formal Requirements

## Purpose
Stock and flow diagrams bridge intuition and formal mathematical specification by introducing explicit mechanisms and conservation properties. They are foundational for system dynamics modeling, enabling clear representation of how quantities change over time and how external factors interact with the system.

## Key Concepts
- **Stock:** A quantity that accumulates or depletes over time (e.g., UST supply, LUNA market cap, system confidence). Measured at a specific point in time.
- **Flow:** The rate of change (increase or decrease) in a stock (e.g., minting, burning, arbitrage, staking, panic selling). Measured over an interval of time.
- **External Factors:** Environmental impacts or parties outside the system's control (e.g., market conditions, regulatory changes, yield protocols) that can influence stocks and flows.
- **Conservation Laws:** Mathematical relationships that assert how stocks and flows interact, ensuring system structure and integrity even under external influence.

## Requirements for Diagram Development
1. **Explicit Representation:** Clearly distinguish stocks, flows, and external factors in the diagram.
2. **Conservation Structure:** Show how flows affect stocks and how conservation laws (e.g., total supply, market cap) are maintained.
3. **Parameter Assertion:** Define parameters (e.g., rates, thresholds) and structure for the system, supporting future mathematical modeling.
4. **External Influence:** Indicate how external factors impact stocks and flows, and how the system responds.
5. **Iterative Refinement:** Use the diagram as a basis for further formalization, simulation, and empirical calibration.

## Example References
- **Simple Physical Capital Example:** Illustrates basic stock/flow relationships (see cadCAD Edu).
- **Complex Two-Phase System:** Shows multi-layered feedback and conservation (see Bosch TE Workshop #1).

## Application to Stablecoin System
- Stocks: UST supply, LUNA market cap, system confidence
- Flows: mint/burn, arbitrage, seigniorage, staking, panic selling
- External Factors: market conditions, regulatory changes, yield protocol
- Conservation: Ensure total supply and market cap are tracked and respond to flows and external shocks

## Further Study
- Bosch TE Workshop #1: https://drive.google.com/drive/u/1/folders/1O2s5RYO10My3c6qWXHZG5f6MUMtcIeyR
- cadCAD Edu: System dynamics modeling resources

---
This document formalizes the requirements for stock and flow diagrams in your stablecoin research, supporting rigorous system modeling and future simulation work.
