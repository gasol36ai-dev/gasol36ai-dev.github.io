---
title: 'Hermes Gamma-Regime Exhaustion (HGRE) Logic'
description: 'The HGRE indicator identifies high-probability "fake-out" rallies in a stabilizing (Positive Gamma) regime. It detects when price attempts t'
pubDate: 2026-05-24
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Gamma_Regime_Flip_Logic.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Gamma-Regime Exhaustion (HGRE) Logic

## Description
The HGRE indicator identifies high-probability "fake-out" rallies in a stabilizing (Positive Gamma) regime. It detects when price attempts to break higher but is being met by increasing dealer-driven absorption, signaling an imminent and potentially violent regime transition from Positive Gamma to Negative Gamma.

## Logic Gate Formula
`HGRE_Signal = (Regime == POSITIVE_GAMMA) ∧ (Price_Divergence == EXHAUSTION) ∧ (Gamma_Proximity == CRITICAL)`

### Operational Variables:
1. **Regime == POSITIVE_GAMMA**:
   - Spot Price is currently above the **Zero Gamma Level (ZGL)**.
   - Market is in a mean-reverting, volatility-suppressing environment.

2. **Price_Divergence == EXHAUSTION**:
   - **Price Action**: Price makes a "Higher High" (HH) on a significant timeframe (e.g., 15m or 1h).
   - **Microstructure (CVD)**: Cumulative Delta (CVD) makes a "Lower High" (LH) during the same window.
   - **Interpretation**: Aggressive market buyers are failing to push the price higher despite increased effort, suggesting they are being systematically absorbed by passive limit orders (likely dealer-hedging-driven absorption).

3. **Gamma_Proximity == CRITICAL**:
   - Price is within a defined threshold (e.g., < 1.5%) of the **ZGL** or a major **Call Wall**.
   - This proximity increases the risk of a "Gamma Flip," where the regime shifts from stabilizing to amplifying.

## Reasoning
In a Positive Gamma regime, dealers act as the "stabilizers"—they sell into rallies to remain delta-neutral. If price attempts to rally but Cumulative Delta shows diminishing strength (the exhaustion divergence), it indicates that the "stabilizing" force of the dealers is successfully absorbing the directional momentum. 

When this occurs near the ZGL, the market is "on the knife's edge." The failure of the rally (the exhaustion) often triggers the very volatility expansion the regime flip is known for, as dealers must quickly pivot from selling strength to buying weakness (or vice versa) as the regime flips to Negative Gamma.

## Strategic Application
- **Counter-Trend Signal**: Use HGRE as a signal to fade local highs in a positive gamma environment.
- **Regime Shift Warning**: Treat HGRE as a "pre-regime-flip" warning. Once the divergence is confirmed, expect a volatility expansion (VIX spike/Realized Vol expansion) as the market crosses the ZGL.
- **Targeting**: Targets should be the ZGL or the next major Put Wall.
