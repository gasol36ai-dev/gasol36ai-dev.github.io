---
title: 'Hermes Proprietary Indicator: The "Regime-Aware Liquidity Filter" (RALF)'
description: 'Most technical indicators fail because they are "regime-blind." A bullish divergence on a lagging oscillator is meaningless in a high-volati'
pubDate: 2026-05-04
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/RALF_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicator: The "Regime-Aware Liquidity Filter" (RALF)

## Logic & Hypothesis
Most technical indicators fail because they are "regime-blind." A bullish divergence on a lagging oscillator is meaningless in a high-volatility, low-liquidity crash regime.

The **Regime-Aware Liquidity Filter (RALF)** is a proprietary Hermes logic gate designed to filter out "false" signals by crossing Market Profile (Micro) with Macro Volatility regimes.

## The Formula / Heuristic
**Signal = (Technical Signal) $\times$ (Liquidity Score) $\times$ (Regime Alignment)**

### 1. Liquidity Score (Micro)
- Calculated via **Market Profile Value Area**.
- **High Liquidity**: Price is inside the Value Area (Balanced).
- **Low Liquidity**: Price is outside the VA (Imbalanced/Trending).
- *Logic*: High-probability reversals occur at the edges of the VA; trend-following signals are only valid when price stays outside the VA.

### 2. Regime Alignment (Macro)
- Defined by the **Hermes Macro State** (e.g., "Systemic Trust Deficit" or "Growth-Driven").
- **Bullish Regime**: High alignment for long signals.
- **Bearish/Crisis Regime**: Long signals are automatically filtered (capped at 0.2 multiplier) unless the Technical Signal is an "Extreme Exhaustion" pattern.

### 3. Final Filter Output
- **Score $\ge 0.8$**: High Conviction Trade.
- **Score $0.4 - 0.7$**: Low Conviction/Speculative.
- **Score $< 0.4$**: Signal Ignored (Noise).

## Historical Pattern Testing
- **Hypothesis**: RALF would have filtered the "bull traps" of the 2026 Q1 volatility spikes by recognizing that while oscillators showed "oversold," the Macro Regime was in a "Systemic Trust Deficit" phase, and price was far outside the Value Area (imbalanced), meaning the "value" was shifting lower, not reverting.

## Implementation Plan
1. Integrate `Macro_State` variable from the Investment Wiki.
2. Map `Value_Area` boundaries from Market Profile tools.
3. Create a Python-based scoring engine to weight the signals.

## Related Concepts
- [[Hermes_Regime_Filter]]
- [[Market_Profile]]
- [[Macro_Economics]]
