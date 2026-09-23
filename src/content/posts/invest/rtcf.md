---
title: 'Proprietary Indicator: Regime-Toxicity Convergence Filter (RTCF)'
description: 'The RTCF is a regime-aware filter designed to eliminate false breakouts by cross-referencing Macro Regimes with Micro Order Flow Toxicity.'
pubDate: 2026-05-15
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/RTCF.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Regime-Toxicity Convergence Filter (RTCF)

## Concept
The RTCF is a regime-aware filter designed to eliminate false breakouts by cross-referencing Macro Regimes with Micro Order Flow Toxicity.

## Logic Framework
### 1. Input Variables
- **Macro Trend ($\mathcal{M}$)**: Derived from lead indicators (e.g., Real Yields, Dollar Index). $\mathcal{M} \in \{-1, 0, 1\}$.
- **Micro Toxicity ($\mathcal{T}$)**: Derived from Directional VPIN. $\mathcal{T} \in \{-1, 0, 1\}$.
- **Absorption Strength ($\mathcal{A}$)**: Magnitude of volume spikes at the level without price movement (normalized 0-1).

### 2. The Convergence Logic
- **Trend Confirmation**: $\mathcal{M} = \mathcal{T}$. When macro regime and informed order flow align, conviction is maximized.
- **Regime Divergence**: $\mathcal{M} 
eq \mathcal{T}$. When price trends with macro but informed flow diverges, a "Trap" is likely.

### 3. Judgment Score Formula
$$Score = (\mathcal{M} 	imes \mathcal{T}) 	imes (1 + \mathcal{A})$$

- **Score $> 1.0$**: High-conviction trend continuation.
- **Score $< 0$**: High-probability reversal/trap. The more negative the score, the stronger the divergence.

## Operational Application
- **Filter**: Do not enter "Breakout" trades if $Score < 0$, regardless of candlestick patterns.
- **Entry**: Enter on $\mathcal{M} 	imes \mathcal{T} = 1$ and $\mathcal{A} pprox 0$ (clean move).
- **Exit/Fade**: Fade positions when $\mathcal{M} 	imes \mathcal{T}$ flips sign, especially if $\mathcal{A}$ spikes.
