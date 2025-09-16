# Model Comparison: Original vs Refined Framework
## De-peg Attack Simulation Model Evolution

### Executive Summary

This document compares our **original sophisticated model** (implemented earlier today) with the **refined simplified framework** (based on SoK paper insights and academic requirements).

---

## 📊 **Side-by-Side Comparison**

| **Aspect** | **Original Model (Complex)** | **Refined Model (Simplified)** | **Rationale for Change** |
|------------|------------------------------|--------------------------------|---------------------------|
| **Attack Strategy** | Multi-vector: AMM dump + flash loans + options + leverage + MEV | Single vector: AMM dump only | Academic clarity; focus on core dynamics |
| **Capital Requirements** | 9% of attack amount (flash loans) | 0% (attacker already owns tokens) | Conservative lower-bound analysis |
| **Profit Mechanisms** | 6 channels: flash arbitrage, options (10x), leverage (5x), cross-platform, MEV, LP manipulation | 1 channel: AMM swap proceeds only | Simplicity; non-sophisticated attacker |
| **Cost Structure** | Complex: options premiums, margin, fees, risk premium | None (cost = 0) | Focus on threshold analysis |
| **Time Scale** | Abstract ticks | 1 hour per tick | Interpretability for publication |
| **Arbitrage Model** | Fixed efficiency rates (Fast/Moderate/Slow) | Stochastic restoration: probability + fraction | More realistic market dynamics |
| **User Behavior** | Simple regime functions | Parameterized distributions with volatility | Calibrated to real market conditions |
| **Pool Parameters** | No fees, basic depths | No fees, systematic depth testing | Controlled experiment design |
| **Monte Carlo** | 30 seeds per scenario | 30 seeds (+ 100 for robustness) | Statistical rigor maintained |
| **Failure Definition** | Price < 0.98 for 3 ticks | Price < 0.98 for 3 ticks | Consistent (from SoK paper) |

---

## 🎯 **Key Differences in Approach**

### **Original Model Philosophy**
- **"How sophisticated can attackers be?"**
- Maximum realism in financial engineering
- Multiple profit vectors simultaneously
- Capital efficiency optimization
- Real-world attack complexity

### **Refined Model Philosophy**  
- **"What is the minimum threshold for system failure?"**
- Conservative assumptions for lower bounds
- Single attack vector clarity
- Policy-relevant parameters
- Academic defensibility

---

## 📈 **Expected Results Comparison**

### **Original Model Results (Actual)**
| Approach | Viable Scenarios | Max ROI | Min Attack Size | Capital Required |
|----------|-----------------|---------|-----------------|------------------|
| Working | 45.8% | 3,496% | 0.5% | $45 |
| Custom | 40.0% | 1,051% | 1.0% | $13,766 |
| Demo | 51.7% | 537% | 0.5% | $13,766 |
| Modular | 0.0% | -101% | N/A | $13,766 |

### **Refined Model Predictions (Expected)**
- **Higher attack thresholds** (cost = 0 but no leverage/options)
- **Lower success rates** (single vector vs multi-vector)
- **Clearer pool depth effects** (systematic liquidity testing)
- **More interpretable results** (1 hour ticks, simple metrics)

---

## 🔄 **Parameter Evolution**

### **Pool Depths**
- **Original**: [$100k, $1M, $5M, $10M] ✓ *Same*
- **Refined**: [$100k, $1M, $5M, $10M] ✓ *Same*

### **Attack Sizes**  
- **Original**: [0.5%, 1%, 2.5%, 5%, 10%] ✓ *Same*
- **Refined**: [0.5%, 1%, 2.5%, 5%, 10%] ✓ *Same*

### **User Regimes**
- **Original**: Normal (small random), Panic (net selling)
- **Refined**: Normal N(μ=0, σ=0.001×L), Panic N(μ=-0.005×L, σ=0.02×L)
- **Change**: Quantified with specific distributions

### **Arbitrage Modeling**
- **Original**: Fixed efficiency (95%, 60%, 30%)
- **Refined**: Stochastic (p_act, restoration_fraction)
- **Change**: More realistic market response

---

## 🎓 **Academic Improvements**

### **Methodological Rigor**
1. **Time scale defined**: 1 hour per tick (was abstract)
2. **Stochastic processes specified**: Normal distributions with parameters
3. **Arbitrage modeling enhanced**: Probability-based restoration
4. **Failure criterion justified**: SoK paper threshold validation
5. **Assumptions documented**: Clear limitations and scope

### **Reproducibility** 
1. **Fixed seed protocols**: Specified N=30 with robustness N=100
2. **Parameter transparency**: All values explicitly defined
3. **Simulation horizon**: 50 ticks with attack at tick 21
4. **Output metrics**: Standardized reporting format

### **Policy Relevance**
1. **Mitigation focus**: Pool depth as controllable parameter
2. **Conservative bounds**: Lower-bound analysis with cost=0
3. **Interpretable results**: Clear threshold recommendations
4. **Sensitivity analysis**: Systematic arbitrage speed testing

---

## 🔍 **Validation Opportunities**

### **Cross-Model Validation**
1. **Threshold comparison**: Do both models identify similar critical pool sizes?
2. **Arbitrage sensitivity**: How do efficiency vs probability models compare?
3. **Regime effects**: Normal vs Panic impact consistency?
4. **Scaling relationships**: Pool depth effects validation?

### **Expected Alignment**
- **Qualitative trends**: Both should show larger pools = more resilient
- **Arbitrage importance**: Both should show fast arbitrage = more stable
- **Attack size scaling**: Similar minimum threshold patterns expected

### **Expected Differences**
- **Absolute thresholds**: Simplified model likely shows higher requirements
- **Success rates**: Complex model enables more attack scenarios
- **Profit margins**: Zero-cost assumption changes economic calculus

---

## 🚀 **Implementation Strategy**

### **Phase 1: Direct Comparison**
1. Run refined model with exact same parameter grid
2. Compare threshold results side-by-side
3. Validate qualitative trend consistency
4. Document quantitative differences

### **Phase 2: Model Synthesis**
1. Use complex model insights to validate simplified assumptions
2. Use simplified model for clear policy recommendations  
3. Present both as complementary analyses
4. Demonstrate robustness across modeling approaches

### **Phase 3: Publication Preparation**
1. Use simplified model for main paper methodology
2. Reference complex model for robustness and sophistication
3. Highlight policy implications from both approaches
4. Document modeling trade-offs and assumptions

---

## 📝 **Conclusion**

The **refined model represents a strategic simplification** that:

✅ **Maintains core insights** while improving academic rigor  
✅ **Provides clearer policy guidance** with interpretable parameters  
✅ **Enables robust validation** against our sophisticated analysis  
✅ **Supports publication requirements** with defensible methodology  

The **original complex model remains valuable** for:
- Understanding real-world attack sophistication
- Demonstrating economic incentives and profit mechanisms  
- Showing impact of financial engineering on attack feasibility
- Providing upper-bound estimates of attack capabilities

Together, they provide **comprehensive coverage** of the attack landscape from conservative academic bounds to realistic financial engineering scenarios.
