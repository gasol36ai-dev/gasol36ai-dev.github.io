---
title: 'Hermes SIF Logic: Proprietary Judgment Indicators'
description: 'This document defines the proprietary logic gates used by the Hermes Digital Organization to to synthesize macro, technical, and microstruct…'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_SIF_Logic.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes SIF Logic: Proprietary Judgment Indicators

This document defines the proprietary logic gates used by the Hermes Digital Organization to to synthesize macro, technical, and microstructure data into high-probability judgment signals.

## Indicator: Hermes Macro-Micro Convergence (HMMC)

### Description
The HMMC indicator identifies "Liquidity Traps" where macro headwinds (rising real yields) are countered by structural rejection (LVN) and microstructure absorption (Delta Divergence), signaling a high-probability trend reversal.

### Logic Gate Formula
`HMMC_Signal = (Macro_Stress_State == HIGH) ∧ (Structure_State == REJECTION) ∧ (Micro_State == ABSORPTION)`

**Operational Variables:**
- **Macro_Stress_State (HIGH):** US 10Y Real Yields showing a positive slope over 5 trading days (Bearish pressure on risk assets).
- **Structure_State (REJECTION):** Price entering a significant Low Volume Node (LVN) or Value Area Low (VAL) on the Market Profile.
- **Micro_State (ABSORPTION):** Price making a new local low while Cumulative Delta (CVD) makes a higher low (Bullish Divergence).

### Reasoning
Standard TA often fails during macro regime shifts. By requiring a macro "stress" condition to be present, the HMMC filters out low-conviction reversals. The convergence of an LVN (where liquidity is thin and price tends to snap) and Order Flow absorption (where aggressive sellers are absorbed by limit buyers) creates a deterministic "spring" effect.
