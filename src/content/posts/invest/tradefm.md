---
title: 'TradeFM (Generative Foundation Model for Trade-flow)'
description: 'TradeFM is a 524M-parameter generative Transformer designed to capture the universal dynamics of market microstructure by learning from bill'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/tradefm.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# TradeFM (Generative Foundation Model for Trade-flow)

TradeFM is a 524M-parameter generative Transformer designed to capture the universal dynamics of market microstructure by learning from billions of trade events across thousands of equities.

## Technical Breakthroughs
- **Partial Observability**: Unlike traditional LOB models that require full book snapshots, TradeFM learns directly from the **event stream** available to any single market participant.
- **Scale-Invariant Representation**: Uses a universal tokenization scheme and scale-invariant features, allowing the model to generalize across different assets and liquidity regimes without asset-specific calibration.
- **Zero-Shot Generalization**: Demonstrates the ability to generalize to geographically out-of-distribution markets (e.g., APAC) with minimal degradation.

## Strategic Value
TradeFM moves microstructure analysis from "asset-specific calibration" to "universal structural learning." It enables:
1. **Synthetic Data Generation**: Producing realistic rollouts that reproduce stylized facts (heavy tails, volatility clustering).
2. **Stress Testing**: Simulating rare but impactful trade-flow patterns.
3. **General-Purpose Microstructure Agents**: Creating trading agents that understand the "language" of order flow across the entire market.

[[order-flow-trading]], [[generative-lob-models]]
