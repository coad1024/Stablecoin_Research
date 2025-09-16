# Stock and Flow Diagram for Stablecoin System (Copy)

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
