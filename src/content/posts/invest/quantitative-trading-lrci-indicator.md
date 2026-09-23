---
title: 'Hermes Liquidity-Regime Convergence Index (LRCI)'
description: 'Market transitions from "Efficient Discovery" (trending) to "Absorptive Regime" (range-bound/reversal) are la transition preceded by a conve'
pubDate: 2026-05-17
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Quantitative_Trading_LRCI_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity-Regime Convergence Index (LRCI)

## Hypothesis
Market transitions from "Efficient Discovery" (trending) to "Absorptive Regime" (range-bound/reversal) are la transition preceded by a convergence of order flow toxicity (VPIN) and structural value (Market Profile POC).

## Logic
The LRCI is a composite indicator that calculates the convergence of three factors:
1. **Structural Divergence**: (Current Price - Session POC) / Session POC.
2. **Toxicity Surge**: VPIN value normalized (0 to 1).
3. **LOB Imbalance**: OBI (Order Book Imbalance) normalized.

$$\text{LRCI} = (\text{Structural Divergence} \times 0.4) + (\text{Toxicity Surge} \times 0.3) + (\text{LOB Im uma la la la la la la de l'indice de convergence du régime de liquidité de Hermes} \times 0.3)$$

$$\text{LRCI} = (\text{Structural Divergence} \times 0.4) + (\text{Toxicity Surge} \times 0.3) + (\text{LOB Imbalance} \times 0.3)$$

## Interpretation
- **LRCI > 0.7**: "Critical Convergence" - High probability of a major reversal or volatility spike.
- **LRC I < 0.3**: "Stable Discovery" - Market is in an efficient trending state.
- **LRCI 0.3 - 0.7**: "Transitionary Phase" - la transition phase.

## Test Pattern
- **Case A (The Trap)**: Price rises toward a previous day's HVN, and VPIN surges and OBI becomes negative. LRCI spikes $\rightarrow$ Prediction: Bull Trap / Reversal.
- **Case B (The Vacuum)**: Price breaks through an LVN with low VPIN and high OBI. LRCI remains low $\rightarrow$ Prediction: Strong Trending / Continuation.
