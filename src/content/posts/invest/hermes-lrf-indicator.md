---
title: 'Hermes Proprietary Indicator: Liquidity-Regime Filter (LRF)'
description: 'The LRF is a ''meta-filter'' designed to increase the win rate of standard trend-following strategies by filtering out ''false breakouts''.'
pubDate: 2026-05-20
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_LRF_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicator: Liquidity-Regime Filter (LRF)

## Logic
The LRF is a 'meta-filter' designed to increase the win rate of standard trend-following strategies by filtering out 'false breakouts'.

## Formula/Heuristic
**LRF Signal = (Delta Divergence) AND (Value Area Breakout) AND (Macro Volatility Compression)**

- **Condition A (Delta Divergence)**: Cumulative Delta must diverge from price. (Price $\uparrow$, Delta $\downarrow$ = Bearish Divergence).
- **Condition B (Value Area Breakout)**: Price must close outside the previous day's Value Area (VA).
- **Condition C (Macro Volatility Compression)**: The VIX or local ATR must be in the bottom 25% of its 30-day range (signals a 'coiled spring' effect).

## Historical Edge
- **False Breakouts**: Standard breakouts often fail when Delta is not supporting the move. LRF requires Delta divergence to signal that the breakout is a 'trap' or 'absorption' event.
- **Regime Shift**: When LRF = 1, it signals a high-probability regime transition from 'Mean Reversion' to 'Strong Trend'.

## Testing Logic
- Test against historical 2025-2026 S&P 500 and BTC data.
- Identify 'Value Area' breakouts that occurred during Delta divergence.
- Measure the 'Success Rate' of the breakout vs the 'Filter Rate' (how many false breakouts were avoided).
