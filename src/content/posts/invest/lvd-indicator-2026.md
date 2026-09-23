---
title: 'Proprietary Judgment Indicator: Liquidity-Volatility Divergence (LVD)'
description: 'An LVD Signal is triggered when:'
pubDate: 2026-05-25
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/LVD_Indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Judgment Indicator: Liquidity-Volatility Divergence (LVD)

## Framework: Map-Trigger-Lock

### 1. Map (Input Variables)
- **Component A**: `Macro Volatility Index (MVI)` — A measure of broad market uncertainty.
- **Component B**: `Exchange Order Flow Imbalance (EOFI)` — A measure of the net direction and intensity of aggressive orders at the micro-level.

### 2. Trigger (Activation Conditions)
An **LVD Signal** is triggered when:
- `[MVI increase > 2σ]` (Volatility spike) **AND**
- `[Liquidity/Depth in top 5 liquid assets decreases > 20%]` (Liquidity drain) **AND**
- `[Aggressive hitting of bid/ask shows high volume but no consistent price direction]` (Directional uncertainty).

### 3. Lock (Actionable Response)
Upon an LVD Signal:
- **Risk Budget Adjustment**: Automatically reduce the maximum risk exposure in all VIP and institutional reports by **30%**.
- **Protocol Shift**: Transition from "Trend Following" to "Capital Preservation" mode.
- **Alerting**: Issue an immediate "Liquidity Alert" to the CEO and COO.

## Strategic Value
Provides an early warning for structural liquidity crises and sudden regime changes in high-leverage environments, allowing for proactive risk reduction before "flash crash" events occur.
