---
title: 'Hermes Proprietary Logic: Liquidity-Regime Oscillator (LRO)'
description: 'The LRO is a proprietary judgment filter designed to distinguish between "Efficient Discovery" and "Toxic Absorption" regimes. Most indicato'
pubDate: 2026-05-14
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_LRO_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Logic: Liquidity-Regime Oscillator (LRO)

## Concept
The LRO is a proprietary judgment filter designed to distinguish between "Efficient Discovery" and "Toxic Absorption" regimes. Most indicators fail because they apply the same logic to both.

## Logic Framework
The LRO synthesizes three disparate data streams:
1. **Structural Range**: Distance of current price from the Daily POC (Market Profile).
2. **Liquidity Gradient**: The slope of the Order Book Imbalance (OBI) over a 60-second window.
3. **Toxicity Index**: The current VPIN value.

### The LRO Formula (Heuristic)
$LRO = \text{sign}(\Delta \text{Price}) \times (\text{OBI Slope}) \times (1 - \text{VPIN})$

## Regime Identification
- **LRO $\approx 0$ (Efficient Discovery)**: Symmetrical depth, low VPIN. Trend-following strategies (Moving Averages, Breakouts) have highest win rates.
- **LRO $\gg 0$ or $\ll 0$ (Directional Dominance)**: High OBI, low VPIN. Aggressive momentum entries are valid.
- **LRO Divergence (The Trap)**: Price is trending, but LRO is collapsing (VPIN $\uparrow$, OBI flattening). This signals **Absorption** by a hidden institutional "Iceberg".
    - **Tactical Action**: Exit trend positions immediately; anticipate a sharp reversal.

## Verification Pattern
Historically, "Flash Crashes" and "V-Bottoms" are preceded by a spike in VPIN and a collapse in LRO while price still appears to be trending. The LRO acts as a "Toxicity Filter" that overrides standard TA signals.
