# Stock and Flow Diagram for Stablecoin System

```mermaid
flowchart TD
    %% Stocks (accumulations)
    S1["UST Supply<br>(Stablecoin Outstanding)"]:::stock
    S2["LUNA Market Cap<br>(Share Token Value)"]:::stock
    S3["System Confidence"]:::stock

    %% Flows (processes)
    F1["Mint/Burn Mechanism"]:::flow
    F2["Arbitrage (Above/Below Peg)"]:::flow
    F3["Seigniorage Distribution"]:::flow
    F4["Staking/Validator Participation"]:::flow
    F5["Flight to Safety (Panic Selling)"]:::flow

    %% External Inputs
    E1["External Market Conditions"]:::external
    E2["Anchor Protocol Yield"]:::external

    %% Relationships
    E1 -- "Affects" --> S3
    E2 -- "Drives" --> S1
    E2 -- "Influences" --> S3

    S1 -- "Price deviation" --> F2
    F2 -- "Arbitrage" --> F1
    F1 -- "Regulates" --> S1
    F1 -- "Impacts" --> S2
    F3 -- "Rewards" --> F4
    F4 -- "Participation" --> S2
    S2 -- "Confidence" --> S3
    S3 -- "Loss of confidence" --> F5
    F5 -- "Reduces" --> S1
    F5 -- "Reduces" --> S2

    %% Class definitions
    classDef stock fill:#FFD54F,stroke:#E65100,stroke-width:2px
    classDef flow fill:#81C784,stroke:#1B5E20,stroke-width:2px
    classDef external fill:#BA68C8,stroke:#4A148C,stroke-width:2px
```

---

**Summary:**
This diagram is a flowchart explaining the feedback dynamics of a stablecoin system (like Terra UST/LUNA). It includes:

- Stocks (UST supply, LUNA market cap, system confidence)
- Flows (mint/burn, arbitrage, seigniorage, staking, panic selling)
- External Inputs (market conditions, yield protocol)

Relationships between these elements are shown with directional and labeled arrows, modeling how confidence, supply, and market forces interact.

## Algorithmic Stablecoin Fragility & Safeguards

```mermaid
flowchart LR
    %% Core Stability Concept
    SC[("Stablecoin Peg / Stability")]:::core

    %% Reliance Factors (Fragility Sources)
    DMD["Support Level of <br/>User Demand"]:::frag
    ARB["Independent Arbitrage <br/>Actors (Incentivized)"]:::frag
    PRICE["Reliable Price <br/>Information (Oracles / Feeds)"]:::frag

    %% Amplifiers / Stressors
    CRISIS["Financial Crisis / <br/>Extreme Volatility"]:::stressor
    OPAQ["Information Opaqueness <br/>& Noise"]:::stressor

    %% Failure Dynamics
    RUN["Loss of Confidence / <br/>Redemptions / Run"]:::failure
    DEPEG["De-Peg / Spiral"]:::failure

    %% Regulatory Safeguards Cluster
    subgraph REG[Regulatory Guidelines & Safeguards]
        IR[Issuer Registration]:::reg
        TAX[Defined Taxonomy <br/>Clarifying Forms]:::reg
        PRUD[Prudential / <br/>Capital Rules]:::reg
        CUST[Collateral Custody <br/>& Segregation]:::reg
        TRANS[Transparency & <br/>Reporting]:::reg
        RISKD[Risk Disclosure]:::reg
        CONTAIN[Containment / <br/>Resolution Measures]:::reg
    end

    %% Relationships
    DMD -->|Required for| SC
    ARB -->|Maintains Peg via| SC
    PRICE -->|Feeds Fair Value to| SC

    CRISIS -->|Reduces| DMD
    CRISIS -->|Disincentivizes| ARB
    CRISIS -->|Disrupts| PRICE
    OPAQ -->|Obscures Signals| PRICE
    OPAQ -->|Erodes| ARB

    DMD -. uncertainty .-> RUN
    ARB -. insufficient incentives .-> RUN
    PRICE -. delays/errors .-> RUN

    RUN -->|Accelerates| DEPEG
    DEPEG -->|Further Deteriorates| DMD
    DEPEG -->|Shrinks| ARB

    %% Safeguards Mitigation Paths
    IR --> TRANS
    TAX --> TRANS
    PRUD --> DMD
    CUST --> DMD
    TRANS --> ARB
    RISKD --> DMD
    CONTAIN --> RUN
    CONTAIN --> DEPEG

    %% Aggregate Mitigation
    REG -->|Strengthens Confidence| SC

    %% Classes
    classDef core fill:#FFE082,stroke:#E65100,stroke-width:2px
    classDef frag fill:#FFAB91,stroke:#BF360C,stroke-width:2px
    classDef stressor fill:#CE93D8,stroke:#6A1B9A,stroke-width:2px
    classDef failure fill:#EF9A9A,stroke:#B71C1C,stroke-width:2px
    classDef reg fill:#90CAF9,stroke:#0D47A1,stroke-width:2px
```

**Explanation:** This diagram encodes the passage: stability depends on (1) demand support, (2) incentivized arbitrage actors, (3) reliable price information. Crisis conditions and opacity weaken these, triggering runs and de-pegs. Regulatory safeguards mitigate root fragility channels to bolster peg stability.
