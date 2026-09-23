---
title: 'Market Microstructure & Order Flow'
description: 'Traditional "Raw LOB Imbalance" signals have largely flattened. The frontier has moved toward Clustered Flow Analysis and Regime-Permissive …'
pubDate: 2026-05-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/microstructure-signals.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Market Microstructure & Order Flow

## Current State (May 2026)
Traditional "Raw LOB Imbalance" signals have largely flattened. The frontier has moved toward **Clustered Flow Analysis** and **Regime-Permissive Execution**.

## Key Frameworks

### 1. Clustered Flow vs. Raw Imbalance
- **The Shift**: Moving away from simple bid-ask delta to "Clustered Flow"—the simultaneous confirmation of four signals across different bar clocks:
    1. **Price Velocity**
    2. **Volume Surge**
    3. **Flow Direction**
    4. **Depth Vacuum**
- **Theoretical Basis**: Pulido et al. (2026) derived predictive imbalance endogenously from an optimal market-making problem, providing a formal mathematical basis for why LOB imbalance predicts mid-price moves.

### 2. Volatility Operating System (VOS)
- **Concept**: A regime-based "Air Traffic Controller" for execution.
- **Regimes**:
    - **Neutral**: Mean-reversion dominance.
    - **Expansion**: Feedback loops (Gamma Squeezes/Slides).
    - **Exhaustion**: Market Maker absorption of one-sided flow.
- **Execution Permissive**: A trade is only authorized if the VOS classifies the regime as compatible with the strategy (e.g., avoiding "Steamroller" effects during short-gamma expansion).

### 3. Dealer Gamma & Structural Friction
- **GEX Mapping**: Pinpointing "invisible walls" where Dealers are forced to hedge, creating mechanical friction.
- **VIX Proxy**: Measuring real-time structural displacement (RVOL vs HVOL) to identify mathematical tension rather than relying on implied volatility guesses.

## Transmission Mapping
`[Microstructure Signals (Velocity/Flow/Depth)]` $\rightarrow$ `[Regime Classification (VOS)]` $\rightarrow$ `[Execution Permissive]` $\rightarrow$ `[Trade Execution]`
