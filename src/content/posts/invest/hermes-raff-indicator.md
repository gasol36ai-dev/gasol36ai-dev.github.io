---
title: 'Hermes Proprietary Indicator: Regime-Aware Flow Filter (RAFF)'
description: 'Traditional Order Flow (Delta/Imbalance) is misleading in different volatility regimes.'
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_RAFF_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicator: Regime-Aware Flow Filter (RAFF)

## 1. The Hypothesis
Traditional Order Flow (Delta/Imbalance) is misleading in different volatility regimes.
- **Low Volatility (Range)**: Order flow imbalances often represent "noise" or retail-driven churn.
- **High Volatility (Stress)**: Order flow imbalances represent institutional "panic" or "aggressive accumulation," providing high-conviction signals.

## 2. Logic & Formula
The **Regime-Aware Flow Filter (RAFF)** acts as a multiplier for the Order Flow Imbalance (OFI) ratio.

### The Formula
$\text{RAFF} = \text{OFI} \times (1 + \sigma_{\text{macro}} \times K)$

Where:
- $\text{OFI} = \frac{\text{Buy Volume} - \text{Sell Volume}}{\text{Total Volume}}$
- $\sigma_{\text{macro}}$: A macro-volatility index (e.g., VIX or a rolling 30-day standard deviation of a lead macro variable like 10Y Yields).
- $K$: A scaling constant (calibration constant) based on the asset's historical volatility.

## 3. Decision Logic
- **RAFF > Threshold (High Confidence)**: When high macro-volatility aligns with a strong order flow imbalance $\rightarrow$ High probability trend continuation.
- **RAFF < Threshold (Low Confidence)**: When low macro-volatility masks a strong order flow imbalance $\rightarrow$ High probability of a "trap" or mean-reversion.

## 4. Verification Pattern
- **Historical Pattern**: In the 2022 rate-hike cycle, many "bullish" order flow signals in calm markets were trapped. However, during "volatility spikes" (CPI prints), the flow signals aligned with the macro-regime and provided the highest alpha.
- **Edge**: This filter removes "false positives" by requiring macro-regime confirmation for high-conviction flow trades.
