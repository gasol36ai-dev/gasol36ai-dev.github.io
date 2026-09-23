---
title: 'Proprietary Hermes Indicator: Order Flow Divergence (OFD)'
description: 'The Hermes Order Flow Divergence (OFD) is a regime-aware filter designed to increase the win rate of existing technical strategies by identi…'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_OFD_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Hermes Indicator: Order Flow Divergence (OFD)

## Concept
The **Hermes Order Flow Divergence (OFD)** is a regime-aware filter designed to increase the win rate of existing technical strategies by identifying "Fakeouts" and "True Breakouts" via a convergence/divergence lens.

## Logic Gate
The indicator monitors the relationship between the **Macro Regime** (Market Profile/Trend) and the **Micro-signal** (Order Flow Imbalance).

### 1. Convergence (Trend Confirmation)
- **Condition**: Macro Regime is Bullish (Price $> 20MA$ and within Value Area) AND Micro-signal is Positive (OBI $> 0.65$).
- **Judgment**: **Strong Trend Confirmation**. High probability of continuation.
- **Action**: Hold or Aggressively Add-on.

### 2. Divergence (Absorption/Trap)
- **Condition**: Price breaks out of Value Area (Macro) BUT Micro-signal is Neutral or Negative (OBI $\le 0.4$).
- **Judgment**: **Absorption/Trap**. The breakout is "hollow" and lacks institutional backing.
- **Action**: Anticipate Reversal / Tighten Stop-loss.

### 3. The "Vibe" Filter (Toxicity)
- **Condition**: VPIN $> 0.8$.
- **Judgment**: **Market Toxicity**. Informed flow is dominating.
- **Action**: Move to Neutral/Flat. Cancel all pending limit orders.

## Historical Edge
In traditional TA, a breakout is a "Buy" signal. OFD filters this by asking: *"Is there actual order flow supporting this move?"*
- **Example**: S&P 500 breakout above a key resistance $\rightarrow$ Price increases $\rightarrow$ Delta becomes negative $\rightarrow$ OFD flags **Divergence**.
- **Result**: Prevents entering a "Bull Trap".

## Formula/Heuristic
$\text{OFD Signal} = \begin{cases} \text{Bullish Confirmation} & \text{if } (\text{Macro} = \text{Bull} \land \text{OBI} > 0.65) \\ \text{Absorption Trap} & \text{if } (\text{Macro} = \text{Breakout} \land \text{OBI} \le 0.4) \\ \text{Toxicity Alert} & \text{if } \text{VPIN} > 0.8 \end{cases}$
