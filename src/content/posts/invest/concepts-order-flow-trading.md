---
title: 'Order Flow Trading'
description: 'Order flow trading analyzes the interaction between buyers and sellers at the microstructure level to identify institutional positioning.'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/order-flow-trading.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Order Flow Trading

Order flow trading analyzes the interaction between buyers and sellers at the microstructure level to identify institutional positioning.

## The 2026 Frontier: Beyond Raw Imbalance
Traditional bid-ask delta and raw Limit Order Book (LOB) imbalance signals have significantly flattened in predictive power.
- **Clustered Flow**: The new standard for large-block execution. Instead of raw delta, traders analyze "clustered" flow patterns that reveal institutional absorption.
- **TradeFM (Foundation Models)**: The introduction of generative Transformers for microstructure. TradeFM uses scale-invariant representations and universal tokenization, allowing a single model to generalize across different assets and liquidity regimes without per-asset calibration.

## Microstructure Indicators
- **Lambda ($\lambda$)**: The price impact coefficient. It captures the market maker's estimate of how much information is embedded in the current flow.
- **VPIN (Volume-Synchronized Probability of Informed Trading)**: Measures toxicity by analyzing volume-synchronized imbalances. High VPIN often precedes liquidity crashes.

[[market-profile]], [[neowave]]
