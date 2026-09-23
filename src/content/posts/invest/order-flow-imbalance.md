---
title: 'Order Flow Imbalance (OFI)'
description: 'Order Flow Imbalance is a quantitative measure of the net difference between buying and selling pressure at the best bid and ask prices in t'
pubDate: 2026-04-29
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/order-flow-imbalance.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow Imbalance (OFI)

Order Flow Imbalance is a quantitative measure of the net difference between buying and selling pressure at the best bid and ask prices in the limit order book.

## The Mechanism
OFI captures the change in supply and demand across time intervals:
- **Demand Increase**: Bid size increases or Ask size decreases.
- **Supply Increase**: Ask size increases or Bid size decreases.

## Causal Chain of Price Impact
`[OFI Surge] -> [Liquidity Depletion at Best Bid/Ask] -> [Price Jump to Next Level] -> [Momentum Trigger]`

## Strategic Application
Used primarily by HFTs and scalpers to identify short-term alpha. It serves as a lead-indicator for price movement because it reveals the *intent* of aggressive market participants before the price reflects the change.

## Related Concepts
- [[hermes-liquidity-world-model]]
- [[quant]]
