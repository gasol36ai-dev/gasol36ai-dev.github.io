---
title: 'Hermes Liquidity-Regime Convergence Index (LRCI)'
description: 'Price action is often misleading when viewed in isolation. True directional conviction occurs when Micro-Order Flow (immediate liquidity) co…'
pubDate: 2026-05-13
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/LRCI_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity-Regime Convergence Index (LRCI)

## Hypothesis
Price action is often misleading when viewed in isolation. True directional conviction occurs when **Micro-Order Flow** (immediate liquidity) converges with **Macro-Regime** (structural value).

## The Logic
The LRCI is a composite filter that weights the interaction between three distinct layers of market data:

1. **Layer 1: Macro Structural Value (The 'Anchor')**
   - Metric: Distance from the 60-day Moving Average (60MA) or the Monthly Value Area (MVA).
   - Logic: If price is within $\pm 3\%$ of the 60MA, the market is in a "Fair Value" regime. If $> 10\%$, it is "Overextended."

2. **Layer 2: Micro-Order Flow (The 'Trigger')**
   - **Delta Divergence**: Detect if current price extreme is accompanied by a lower peak in Cumulative Delta.
- **Order Book Imbalance (OBI)**: Measure the net liquidity difference between bids and asks.

3. **Layer 3: Toxicity Filter (The 'Guardrail')**
   - **VPIN**: Volume-synchronized Probability of Informed Trading.
   - Logic: If VPIN $> 0.8$, the signal is discarded (Toxicity high $\rightarrow$ high risk of being picked off).

## Formula/Heuristic
$$\text{LRCI} = (\text{Regime Weight} \times \text{Order Flow Strength}) \times (1 - \text{Toxicity})$$

Where:
- **Regime Weight**: 1.0 if in Fair Value or recovering from a dip; 0.5 if Overextended.
- **Order Flow Strength**: 
    - +1.0 (Strong Bullish Convergence): Price $\uparrow$ + Positive Delta + High OBI.
    - -1.0 (Strong Bearish Convergence): Price $\downarrow$ + Negative Delta + High Ask-side OBI.
    - 0.0 (Divergence/Noise): When micro and macro disagree.

## Interpretation & Historical Patterns
- **LRCI > 0.7**: High-conviction long entry. Historically coincides with "V-bottoms" where institutional absorption is confirmed by a shift in the regime.
- **LRCI < -0.7**: High-conviction short entry.
- **LRCI between -0.3 and 0.3**: Noise / Range-bound. No trade.

## Verification Logic
To verify this indicator against historical data, the agent should:
1. Scan historical T&S logs.
2. Identify peaks/troughs.
3. Map the LRCI value at the turn.
4. Calculate the win-rate of signals where $\text{LRCI} > 0.7$ vs signals where simple MA crossovers occur.
