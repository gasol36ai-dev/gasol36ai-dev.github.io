---
title: 'Proprietary Indicator: Cross-Venue Liquidity Divergence (CVLD)'
description: 'The Cross-Venue Liquidity Divergence (CVLD) indicator identifies high-risk liquidity "traps" where global order flow signals are decoupled f…'
pubDate: 2026-05-28
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/CVLD_Indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Cross-Venue Liquidity Divergence (CVLD)

## Executive Summary
The **Cross-Venue Liquidity Divergence (CVLD)** indicator identifies high-risk liquidity "traps" where global order flow signals are decoupled from local market depth, often preceding flash crashes or extreme volatility events in specific venues.

## 1. Framework (Map-Trigger-Lock)

### 🗺️ Map (The Inputs)
* **Input A: Aggregate Global Exchange Order Flow Imbalance (GF-OFI):** A high-frequency signal measuring the net directionality of orders across all major centralized and decentralized exchanges.
* **Input B: Local Venue Spread Volatility (LV-SV):** The standard deviation of bid-ask spreads within a specific target venue over a rolling 5-minute window.

### ⚡ Trigger (The Signal)
The CVLD signal is triggered when:
1. **Spread Widening:** `LV-SV` exceeds its 24-hour moving average by > 3 standard deviations.
2. **Imbalance Divergence:** The `GF-OFI` shows a strong directional bias (e.g., heavy selling), but the target venue's local liquidity depth remains deceptively stable or shows contradictory order flow.

### 🔒 Lock (The Action)
Upon a confirmed CVLD signal:
* **Automated Capital Reduction:** Reduce all active limit/market orders and total capital allocation to the divergent venue by **50%** immediately.
* **Risk-Budget Reallocation:** Shift remaining liquidity to "Safe Haven" venues (as identified by the Macro-Volatility module) until the spread volatility stabilizes.

## 2. Strategic Value
CVLD provides a critical defense mechanism against **"Liquidity Mirage"** events, where a venue appears deep enough for execution but suffers from extreme slippage or "ghost liquidity" during periods of systemic stress. It bridges the gap between global macro trends and local market microstructure.

## 3. Implementation Notes
* **Frequency:** Requires sub-second latency for data ingestion.
* **Data Sources:** Requires direct WebSocket feeds from all major exchange venues.
* **Complexity:** High. Requires robust handling of asynchronous data streams and cross-exchange synchronization.
