---
title: 'Proprietary Indicator: Neuro-Symbolic Liquidity Pulse (NSLP)'
description: 'The Neuro-Symbolic Liquidity Pulse (NSLP) is a hybrid indicator designed to detect high-conviction regime shifts by combining statistical or'
pubDate: 2026-05-28
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/NSLP_Indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Neuro-Symbolic Liquidity Pulse (NSLP)

## Overview
The **Neuro-Symbolic Liquidity Pulse (NSLP)** is a hybrid indicator designed to detect high-conviction regime shifts by combining statistical order flow patterns with formal logical verification of market structural constraints.

## Framework (Map-Trigger-Lock)

### 1. Map (The Multi-Domain Synthesis)
The NSLP synthesizes three distinct data streams:
- **[Neural] Order Flow Entropy (OFE)**: A statistical measure (via LLM/Neural model) of the randomness/predictability in recent transaction sequences.
- **[Symbolic] Structural Liquidity Constraint (SLC)**: A deterministic check (via Formal Logic) against historical limit order book (LOB) depth and exchange-mandated liquidity requirements.
- **[Macro] Volatility Regime (VR)**: The current macro-economic volatility state (e.g., High/Low, Trending/Mean-reverting).

### 2. Trigger (The Convergence Event)
The NSLP signal is triggered when:
- **`[Low OFE (High Predictability)]`** AND **`[High SLC Violation (Rapid Thinning)]`** AND **`[Volatility Regime Transition]`**
- *Specifically*: When order flow becomes highly predictable (pattern-based) just as the structural liquidity floor (SLC) is breached during a macro volatility shift.

### 3. Lock (The Actionable Response)
- **`[Immediate Scaling of Directional Liquidity-Taking Orders]`**
- **`[Auto-Reduction of Risk-Budget by 50% for Market-Making Roles]`**
- **`[Trigger High-Priority 'Volatility Alert' for VIP Summary]`**

## Strategic Value
Unlike single-domain indicators (e.g., just VPIN or just Volatility), the NSLP identifies the **convergence** of predictable, non-random order flow with a breakdown in the deterministic "safety rails" of market liquidity. This provides a high-fidelity early warning for liquidity-driven "Flash Crashes" and high-conviction directional breakouts.

---
*Codified: 2026-05-28*
*Status: Unverified (Awaiting Historical Backtest)*
