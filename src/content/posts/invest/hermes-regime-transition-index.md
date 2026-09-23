---
title: 'Hermes Regime Transition Index (HRTI)'
description: 'The Hermes Regime Transition Index (HRTI) is a proprietary synthetic indicator designed to filter technical signals based on the underlying '
pubDate: 2026-04-30
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes-Regime-Transition-Index.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime Transition Index (HRTI)

The **Hermes Regime Transition Index (HRTI)** is a proprietary synthetic indicator designed to filter technical signals based on the underlying macro-volatility regime. It prevents "Trend Following" in balanced markets and "Mean Reversion" in trending markets.

## The Logic: Macro-Technical Convergence
The HRTI correlates three disparate data streams to determine the market "State":
1. **Macro Volatility**: MOVE Index (Bonds) and VIX (Equities).
2. **Market Structure**: TPO Profile Shape (Value Area distribution).
3. **Micro Flow**: Cumulative Delta (CVD) Divergence.

## The HRTI Framework

### Regime A: Stable Efficiency (Low HRTI)
- **Conditions**: $\text{MOVE} < \text{Threshold}_1$, TPO = Normal Distribution, Delta Div $\approx 0$.
- **Market State**: High consensus, low uncertainty.
- **Hermes Judgment**: **Mean Reversion**. Trade the VAL $\rightarrow$ VAH range. Ignore breakouts.

### Regime B: Informed Transition (Medium HRTI)
- **Conditions**: $\text{Threshold}_1 < \text{MOVE} < \text{Threshold}_2$, TPO = Double Distribution, Delta Div $=$ High.
- **Market State**: Value is migrating. Institutional repositioning is occurring.
- **Hermes Judgment**: **Momentum**. Trade the IB extension and Value Area migration.

### Regime C: Chaotic Exhaustion (High HRTI)
- **Conditions**: $\text{MOVE} > \text{Threshold}_2$, TPO = Poor High/Low, Delta Div $=$ Extreme.
- **Market State**: Panic or Euphoria. Order flow is exhausted.
- **Hermes Judgment**: **Contrarian**. Look for "Absorption" at extremes and trade the reversal back to the POC.

## Implementation Heuristic
$$\text{HRTI} = \text{Normalize}(\text{Macro\_Vol}) \times \text{TPO\_Skew} \times \text{CVD\_Divergence}$$

- **TPO\_Skew**: $0$ for Normal, $1$ for Double Dist, $2$ for Poor High/Low.
- **CVD\_Divergence**: $\text{Abs}(\text{Price\_Trend} - \text{CVD\_Trend})$.

## Historical Edge
The HRTI provides an edge by identifying **"False Breakouts"**. A break of the Value Area in Regime A is usually a trap; a break in Regime B is a high-conviction trend.

[[Market-Profile]], [[Order-Flow]], [[quant]]
