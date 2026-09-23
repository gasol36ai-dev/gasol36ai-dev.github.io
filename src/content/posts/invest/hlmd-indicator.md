---
title: 'Proprietary Indicator: Hermes Liquidity-Macro Divergence (HLMD)'
description: 'The HLMD indicator is designed to detect "Regime Shifts" by identifying divergences between high-level macroeconomic trends and low-level in'
pubDate: 2026-05-12
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HLMD_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Hermes Liquidity-Macro Divergence (HLMD)

## Concept
The HLMD indicator is designed to detect "Regime Shifts" by identifying divergences between high-level macroeconomic trends and low-level institutional order flow. It operates on the premise that while macro variables set the long-term direction, institutional "Smart Money" often signals a reversal through order flow before the macro trend officially shifts.

## Logic & Calculation
The indicator monitors two primary data streams:
1. **Macro Trend (MT)**: A filtered signal of a key macro driver (e.g., 20-day moving average of Interest Rates or a specific Sentiment Index).
    - $MT = 1$ (Bullish)
    - $MT = -1$ (Bearish)
2. **Order Flow Momentum (OFM)**: The cumulative Net Delta (Aggressive Buys - Aggressive Sells) over a short-term window (e.g., 1-hour or 4-hour).

### Signal Generation
- **Divergence Warning**: Triggered when $MT$ and $OFM$ maintain opposite signs for $N$ consecutive periods (e.g., $N \ge 3$).
    - *Bullish Divergence*: Macro is Bearish, but Order Flow is consistently positive.
    - *Bearish Divergence*: Macro is Bullish, but Order Flow is consistently negative.
- **Confirmation (The Trigger)**: A Divergence Warning becomes an actionable trade signal when:
    - The $OFM$ crosses back into alignment with $MT$ after a period of divergence.
    - **OR** Price creates a "Single Print" (Poor High/Low) at a Composite Value Area boundary.

## Historical Pattern Validation
- **Pattern A (Distribution)**: Macro trend remains bullish (market feels optimistic), but Net Delta becomes heavily negative (institutions are distributing). Result: HLMD triggers "Bearish Divergence Warning" $\rightarrow$ High probability of price top.
- **Pattern B (Accumulation)**: Macro trend is bearish (fear), but Net Delta is consistently positive. Result: HLMD triggers "Bullish Divergence Warning" $\rightarrow$ High probability of price bottom.

## Implementation Note
HLMD should be used as a filter for timing. The Macro Trend provides the "What", and the Order Flow Divergence provides the "When".
