---
title: 'Multi-Scale Order Flow & Adaptive Granularity Attention (AGA)'
description: 'Traditional order flow analysis often suffers from the "resolution conflict": tick-level data provides microstructure detail but is noisy; m…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/adaptive-granularity-flow.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Multi-Scale Order Flow & Adaptive Granularity Attention (AGA)

Traditional order flow analysis often suffers from the "resolution conflict": tick-level data provides microstructure detail but is noisy; minute-level data captures trends but misses the "toxic" liquidity shocks that precede price moves.

## 1. The AGA-Neural HMM Framework
The recent introduction of **Adaptive Granularity Attention (AGA)** allows a model to dynamically shift its focus between different temporal resolutions based on market conditions.

### Architectural Logic
- **Parallel Multi-Resolution Encoders**:
    - **Dilated Causal CNNs**: Capture high-frequency microstructure details (tick-level).
    - **Wavelet-LSTM**: Capture longer-term trends and aggregated flow (minute-level).
- **Dynamic Gating Mechanism**: Conditioned on **local volatility** and **transaction frequency**, the model decides which resolution to prioritize.
- **Conditional Normalizing Flows**: Replace static emission models in the HMM, allowing the model to capture non-Gaussian, heavy-tailed distributions of order flow imbalances.

## 2. Transmission Mapping: Liquidity Shocks
The AGA framework explicitly maps how microstructure anomalies translate into price action:
**[Tick-Level Order Flow Imbalance] $\rightarrow$ [Volatility-Triggered Resolution Shift] $\rightarrow$ [Liquidity Shock Detection] $\rightarrow$ [Price Impact]**.

## 3. Strategic Value
By autonomously adapting granularity, the agent can detect "informed" flow (which often manifests as specific tick-patterns) while ignoring "noise" flow, significantly reducing false positives in divergence signals.
