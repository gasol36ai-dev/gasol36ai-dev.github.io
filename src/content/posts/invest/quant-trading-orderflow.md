---
title: 'Frontier Quantitative Trading & Order Flow (2026)'
description: 'Modern Quant trading focuses on the "Footprint" of institutional activity rather than historical price patterns.'
pubDate: 2026-05-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Quant_Trading_OrderFlow.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Frontier Quantitative Trading & Order Flow (2026)

## 1. Market Microstructure & Order Flow
Modern Quant trading focuses on the "Footprint" of institutional activity rather than historical price patterns.

### Order Flow Imbalance (OFI)
- **Imbalance Ratio**: $\text{Ratio} = \frac{\text{Buy Volume} - \text{Sell Volume}}{\text{Total Volume}}$
- **Decomposition Formula**: $\text{Strategy Return} = \text{Alpha} + \text{Imbalance Impact} + \text{Execution Slippage}$
- **Key Signal**: *Delta Divergence* (e.g., price rising while Delta is negative) signals hidden selling pressure and potential reversal.

### Volume Profile (VP) vs. Market Profile (TPO)
- **Market Profile (TPO)**: Measures **TIME**. Reveals where the market achieved consensus (Acceptance).
- **Volume Profile (VP)**: Measures **CONTRACTS**. Reveals where the most aggressive trading occurred (Conviction).
- **VPOC (Volume Point of Control)**: The price level with maximum volume. Acts as a powerful magnet or rejection zone.

## 2. Spectral Analysis & Wavelets
Replacing fixed indicators with adaptive frequency decomposition.

### WaveLSFormer (Learnable Wavelet Transformers)
- **Logic**: Decomposes prices into low-frequency (trend) and high-frequency (noise) components using a learnable filter bank.
- **Cross-Frequency Injection**: High-frequency cues are injected into low-frequency representations via gated residuals to refine trend detection without adding noise.

## 3. Strategic Integration
The highest alpha is found at the intersection of:
$\text{Macro Regime} \rightarrow \text{Volume Profile (Structure)} \rightarrow \text{Order Flow (Timing)}$
