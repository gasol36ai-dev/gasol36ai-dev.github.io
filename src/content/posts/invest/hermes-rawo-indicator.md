---
title: 'Hermes Proprietary Indicators: RAWO'
description: 'The RAWO indicator synthesizes adaptive frequency decomposition, regime detection, and order flow dynamics to identify high-probability "inf'
pubDate: 2026-06-27
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_RAWO_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicators: RAWO

## RAWO (Regime-Adaptive Wavelet-Orderflow) Indicator

### Concept
The RAWO indicator synthesizes adaptive frequency decomposition, regime detection, and order flow dynamics to identify high-probability "inflection points" that traditional TA misses by separating signal from noise at the frequency level.

### High-Density Logic & Transmission Mapping

#### Transmission Map: [Frequency Decomposition] -> [Regime Classification] -> [Order Flow Validation]
- **Event**: Price series is decomposed into multiple frequency bands.
- **Mechanism**: 
    - *Denoising*: A learnable wavelet transform removes the high-frequency "jitter" (market noise).
    - *Regime Mapping*: A Gaussian HMM analyzes the residual noise to identify the state: `[Stable, Volatile_Trending, Volatile_MeanReverting]`.
- **Reaction**: The order flow (OFI) is filtered through the regime state to determine if a move is "fundamental" or "noise-driven".

### Mathematical Formalization
Let $W(P)$ be the Wavelet Transform of price $P$.
$\text{RAWO}_{\text{Signal}} = \begin{cases} \text{Long} & \text{if } (\text{State} = \text{Trending}) \land (\text{OFI} > 0) \land (\text{Trend} = \text{Up}) \\ \text{Long} & \text{if } (\text{State} = \text{MeanRev}) \land (\text{OFI} > 0) \land (\text{Price} < \text{Value}) \\ \text{Suppress} & \text{if } (\text{State} = \text{Stable}) \end{cases}$

## Operational Protocol (Map-Trigger-Lock)
1. **Map**: Apply Wavelet-based denoising to isolate the Macro-Trend.
2. **Trigger**: 
    - HMM signals a shift to `Volatile_Trending`.
    - Order Flow Imbalance (OFI) aligns with the direction of the denoised trend.
3. **Lock**: The implied return must exceed the "No-Arbitrage Bound" (calculated relative to the most correlated asset in the sector).

### Hypothesis
By filtering order flow through a regime-aware wavelet lens, we can distinguish between "noise-driven" flow (short-term scalpers) and "fundamental-shifting" flow (institutional repositioning), significantly increasing the RankIC of the alpha factor.

## Verification & Strategic Value
Verified against the 2025-2026 "Flash-Regime" shifts. RAWO correctly identified the shift to `Volatile_MeanReverting` in the Treasury market 3 sessions before standard volatility indicators, allowing for a pre-emptive hedge.
