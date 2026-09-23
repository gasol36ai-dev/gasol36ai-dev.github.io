---
title: 'Clustered Flow: The Evolution of Execution Signals'
description: 'For years, "Order Book Imbalance" (the ratio of bid-size to ask-size) was a primary signal for short-term price movement. However, as of 202…'
pubDate: 2026-06-01
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/clustered-flow-2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Clustered Flow: The Evolution of Execution Signals

## The Decline of Raw LOB Imbalance
For years, "Order Book Imbalance" (the ratio of bid-size to ask-size) was a primary signal for short-term price movement. However, as of 2026, this signal has significantly flattened:
- **Spoofing/Layering**: High-frequency agents now use sophisticated layering to create fake imbalances.
- **Hidden Liquidity**: A larger percentage of institutional volume is executed via dark pools or "hidden" orders, making the visible LOB a poor proxy for true intent.
- **Adversarial ML**: Market makers now actively "shape" the LOB to trigger imbalance-based algorithms.

## The Clustered Flow Methodology
"Clustered Flow" shifts the focus from the *state* of the book to the *clustering of execution*. It analyzes the temporal and volumetric distribution of aggressive orders.

### 1. Identification of "Flow Clusters"
Instead of looking at a single trade, the system identifies clusters of trades that exhibit:
- **Temporal Proximity**: Trades occurring within a micro-window (e.g., 5-10ms).
- **Volumetric Correlation**: Multiple trades of similar size hitting the same price level.
- **Directional Consistency**: A sequence of aggressive buys/sells that consume multiple levels of the LOB.

### 2. The Signal: Cluster Intensity vs. LOB State
The Clustered Flow signal is derived from the divergence between visible LOB imbalance and actual execution clusters:
- **Bullish Divergence**: Visible LOB looks bearish (more asks than bids), but "Buy Clusters" are aggressively consuming the ask side. This indicates strong hidden demand.
- **Bearish Divergence**: Visible LOB looks bullish, but "Sell Clusters" are consistently pushing through the bid side.

## Application in Large Block Execution
For institutional traders executing large blocks, Clustered Flow provides a robust signal for:
- **Entry/Exit Timing**: Entering a position when a "Demand Cluster" is identified, reducing the risk of being "picked off" by HFTs.
- **Slippage Reduction**: Identifying periods of high "Clustered Liquidity" where large orders can be absorbed with minimal price impact.
- **Counterparty Detection**: Inferring the presence of another large institutional player by the signature of their flow clusters.

## Comparative Analysis
| Feature | Raw LOB Imbalance | Clustered Flow |
| :--- | :--- | :--- |
| **Signal Basis** | Static state of the book | Dynamic execution patterns |
| **Resilience to Spoofing** | Low | High |
| **Hidden Liquidity Detection**| None | High |
| **Latency Sensitivity** | Extremely High | High |
| **Reliability (2026)** | Low/Flattened | High/Expanding |
