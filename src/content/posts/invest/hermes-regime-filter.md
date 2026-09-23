---
title: 'Hermes Regime-Filter (HRF)'
description: 'The Hermes Regime-Filter (HRF) is a proprietary judgment indicator designed to filter high-frequency Order Flow signals using a macro-econom'
pubDate: 2026-05-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Regime_Filter.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime-Filter (HRF)

The **Hermes Regime-Filter (HRF)** is a proprietary judgment indicator designed to filter high-frequency Order Flow signals using a macro-economic regime layer.

## The Hypothesis
Order flow imbalances are not equally valid across all market regimes. The "meaning" of an imbalance changes based on systemic trust and volatility.

## Logic Framework

### 1. The Regime Layer (Macro)
We define two primary regimes based on **Real Yields** and **VIX/Volatility**:
- **Regime: Systemic Trust (ST)**
  - *Characteristics*: Low volatility, stable or declining real yields, positive risk sentiment.
  - *Context*: Market is driven by fundamental growth and trend-following.
- **Regime: Systemic Stress (SS)**
  - *Characteristics*: High volatility, spiking real yields, "flight to safety".
  - *Context*: Market is driven by liquidity needs, margin calls, and panic.

### 2. The Signal Layer (Micro)
- **Signal**: Order Flow Imbalance (OFI) $\uparrow$ (Aggressive Buying).

### 3. The Integration (Filter)

| Macro Regime | Micro Signal (OFI $\uparrow$) | HRF Verdict | Market Behavior |
| :--- | :--- | :--- | :--- |
| **Systemic Trust** | Aggressive Buying | **CONFIRM** | Healthy trend continuation. |
| **Systemic Stress** | Aggressive Buying | **DIVERGE** | Potential Absorption/Trap. Likely a "Bull Trap" into institutional liquidity. |

## Edge Description
The HRF prevents the "Naive Quant" error of buying every aggressive imbalance during a crisis. In **Systemic Stress**, aggressive buying is often the *last* gasp of retail before a liquidity flush. By filtering for **Systemic Trust**, we increase the win rate of trend-following strategies.

## Testing Logic
- **Historical Pattern**: During the 2020 Oil Crash or 2022 Rate Hikes, many "buy" imbalances occurred at local tops during high-volatility regimes. The HRF would have flagged these as "Diverge", avoiding the trade.

See also: [[Order_Flow]], [[Market_Profile]].
