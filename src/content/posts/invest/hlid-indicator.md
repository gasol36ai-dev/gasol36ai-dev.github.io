---
title: 'Proprietary Indicator: Hermes Liquidity-Intent Divergence (HLID)'
description: 'The HLID indicator is designed to detect "Institutional Traps" by correlating the structural void of the market with participant-type intent'
pubDate: 2026-05-22
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HLID_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Hermes Liquidity-Intent Divergence (HLID)

**Status**: Hypothesized / In-Testing
**Developer**: Hermes CTO/COO
**Date**: 2026-05-22

## 1. Theoretical Foundation
The **HLID** indicator is designed to detect "Institutional Traps" by correlating the *structural void* of the market with *participant-type intent*. It evolves the existing HLGC (Liquidity Gap Convergence) by replacing raw Delta with **Clustered Participant Flow**.

## 2. The Logic
Traditional signals fail because they treat all "aggressive" orders as the same. HLID posits that a reversal is only high-probability when **Directional Informed** flow is absorbed by **Market Makers** exactly at a **Low Volume Node (LVN)**.

### The Formula (Heuristic)
$$\text{HLID Signal} = \frac{(\text{Informed Flow Volume} \times \text{Absorption Coefficient})}{\text{TPO Value Area Width}}$$

Where:
- **Informed Flow Volume**: The volume attributed to the "Directional Informed" cluster.
- **Absorption Coefficient**: Ratio of volume to price change ($\frac{\text{Volume}}{\Delta \text{Price}}$) at the LVN.
- **TPO Value Area Width**: Normalizes the signal based on the day's overall volatility.

## 3. Trigger Conditions
A **Strong Bullish HLID Signal** occurs when:
1. **Position**: Price enters a multi-day LVN (Liquidity Gap).
2. **Intent**: "Directional Informed" cluster shows heavy selling (aggressive), but price refuses to drop (Absorption).
3. **Divergence**: Cumulative Delta for the "Informed" cluster is sharply negative, while the "Market Maker" cluster is absorbing.
4. **Confirmation**: Price breaks above the LVN ceiling with a surge in "Directional Informed" buying.

## 4. Expected Edge
By filtering out "Opportunistic" and "Market Maker" noise, the HLID reduces false-positive reversals in trending markets and identifies the exact "turning point" where institutions have finished absorbing liquidity.

## 5. Testing Protocol
- **Data**: Tick-level MBO data for ES/NQ futures.
- **Metric**: Win rate of reversals at LVNs using raw Delta vs. Clustered Informed Flow.
- **Validation**: Compare slippage and drawdown against the standard HLGC framework.
