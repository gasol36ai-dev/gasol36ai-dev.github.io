---
title: 'TradeFM: Generative Microstructure'
description: 'Synthesis of the TradeFM framework for trade-flow and market microstructure.'
pubDate: 2026-07-06
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/tradefm_generative_microstructure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# TradeFM: Generative Microstructure
Synthesis of the TradeFM framework for trade-flow and market microstructure.

## Core Architecture
TradeFM is a **Generative Foundation Model** designed to treat market microstructure as a language. Instead of predicting price (regression), it models the *distribution of trade-flow sequences* (generation).

### Key Innovations:
1. **Scale-Invariant Representations**: The model represents trade-flows in a way that is independent of the specific asset's volatility or absolute price, allowing it to generalize across different symbols (e.g., from BTC to Gold).
2. **Universal Tokenization**: Trade events (bid, ask, cancel, fill) are tokenized into a universal sequence, enabling the use of Transformer-based architectures to predict the "next most likely" microstructure state.
3. **Regime Generalization**: Because it learns the *underlying physics* of liquidity and flow rather than asset-specific patterns, it does not require recalibration when moving between high-liquidity and low-liquidity regimes.

## Transmission Mapping
- **[Asset-Specific Calibration] $\rightarrow$ [Model Overfitting] $\rightarrow$ [Regime Failure]**: Traditional models fail during "Black Swan" events because they are overfit to a specific asset's historical volatility.
- **[Universal Tokenization] $\rightarrow$ [Cross-Asset Generalization] $\rightarrow$ [Robust Microstructure Prediction]**: TradeFM's ability to recognize "flow signatures" regardless of the asset allows it to predict liquidity crashes before they manifest in price.

## Strategic Significance
TradeFM moves the industry from "Statistical Arbitrage" to "Structural Arbitrage," where the model understands the generative process of the market itself.
