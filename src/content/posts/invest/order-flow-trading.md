---
title: 'Order Flow Trading'
description: 'Order Flow analysis focuses on the micro-structure of the market, examining the actual buy and sell orders entering the limit order book (LO'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/investment/concepts/order-flow-trading.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow Trading

Order Flow analysis focuses on the micro-structure of the market, examining the actual buy and sell orders entering the limit order book (LOB) to understand the immediate supply/demand imbalance.

## Key Metrics
- **Delta**: The net difference between aggressive buyers (market buy) and aggressive sellers (market sell) over a given period.
- **Absorption**: Occurs when high volume is transacted at a price level, but the price fails to move. This indicates a large limit order ("iceberg") is absorbing all market aggression.
- **Exhaustion**: A sharp drop in volume as price reaches a new high or low, signaling that the aggressive move has run out of participants.
- **Footprint Charts**: Visual representations of volume at each price level within a candle, revealing where the "real" money is positioned.

## Quantitative Application
Order flow is not used for long-term forecasting but for **precise entry and exit**. It confirms whether a technical level (from Wave Theory or Market Profile) is actually being defended or broken.

[[market-profile]], [[hermes-regime-filter]]


## 2026 Evolution: From Delta to Clustered Flow
Recent research indicates a shift from monitoring raw bid-ask delta to analyzing **Clustered Flow**. While raw delta signals have flattened in highly efficient markets, clustered flow identifies liquidity-rich zones where institutional blocks are being executed, providing more robust signals.

[[clustered-flow]]
