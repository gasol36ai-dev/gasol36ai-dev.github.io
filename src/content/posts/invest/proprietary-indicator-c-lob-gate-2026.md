---
title: 'Convergent LOB Gate (C-LOB Gate)'
description: 'The C-LOB Gate synthesizes Market Microstructure (TradeFM/Clustered Flow) and Global Macro (Asymmetric Policy Paralysis) to detect the exact'
pubDate: 2026-06-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Proprietary_Indicator_C-LOB_Gate_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Convergent LOB Gate (C-LOB Gate)

## 1. Concept
The C-LOB Gate synthesizes **Market Microstructure (TradeFM/Clustered Flow)** and **Global Macro (Asymmetric Policy Paralysis)** to detect the exact moment when macro-economic "Paralysis" triggers a structural collapse in market liquidity.

## 2. Framework (Map-Trigger-Lock)

### Map (The Data Inputs)
- **Micro-Vector**: `[Clustered Flow Imbalance (CFI)]` (using TradeFM generative baseline)
- **Macro-Vector**: `[Fed Reaction Function Divergence]` (Spread between implied and actual policy paths)
- **Liquidity-Vector**: `[Real Yield Stability Index]`

### Trigger (The Decision Gate)
The gate triggers when:
$(\text{CFI} > 2\sigma) \land (\text{Policy Divergence} > 15\text{bps}) \land (\text{Real Yields} = \text{Stagnant})$

**Logic**: A high-density clustered flow imbalance occurring during a window of policy paralysis and stable real yields indicates that "Invisible Liquidity" has vanished, and the market is entering a "Vacuum Phase".

### Lock (The Actionable Output)
- **Primary Action**: Immediate transition to "Execution-Only" mode (disable all speculative sizing).
- **Secondary Action**: Hedge via "Sovereign Liquidity" assets (move to assets backed by the Sovereign Liquidity-Sovereignty Convergence logic).
- **Verification**: Signal is locked only when observed across 3 distinct liquidity pools.

## 3. Strategic Value
Unlike the LVD indicator (which warns of volatility), the C-LOB Gate identifies the **Liquidity Vacuum**. It predicts not just that the market will move, but that the market *cannot* absorb the move, leading to step-function price gaps.

## 4. Transmission Mapping
[ Policy Paralysis ] -> [ Clustered Flow Imbalance ] -> [ Liquidity Vacuum ] -> [ Step-Function Price Gap ]
