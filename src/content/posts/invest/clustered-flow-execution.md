---
title: 'Clustered Flow & Execution'
description: 'Synthesis of shift from raw Limit Order Book (LOB) signals to Clustered Flow analysis.'
pubDate: 2026-07-06
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/clustered_flow_execution.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Clustered Flow & Execution
Synthesis of shift from raw Limit Order Book (LOB) signals to Clustered Flow analysis.

## Technical Mechanism
Traditional market microstructure relied on **LOB Imbalance** (the ratio of bids to asks at the top of the book). However, as high-frequency traders (HFTs) and AI-driven execution algorithms evolved, they began "spoofing" or layering the book, flattening the edge of raw bid-ask delta.

**Clustered Flow** is a higher-order signal that analyzes:
1. **Temporal Clustering**: Groups of trades occurring within micro-bursts.
2. **Volume Aggregation**: The concentration of liquidity at specific "hidden" levels rather than the visible top-of-book.
3. **Flow Toxicity**: The probability that the current flow is "informed" (leading to a price move) vs. "noise" (mean-reverting).

## Transmission Mapping
- **[LOB Signal Flattening] $\rightarrow$ [Edge Decay] $\rightarrow$ [Execution Slippage]**: When raw delta edges flatten, relying on top-of-book signals leads to poor entries and high slippage for large blocks.
- **[Clustered Flow Detection] $\rightarrow$ [Informed Liquidity Identification] $\rightarrow$ [Optimized Block Entry]**: By identifying clusters of informed flow, execution algorithms can "hide" their orders within the noise or front-run the cluster, significantly reducing market impact.

## Strategic Value
Clustered flow represents the "new alpha" in execution. In fragmented markets, the ability to distinguish a "cluster" from "random noise" is the difference between institutional-grade execution and retail-level slippage.
