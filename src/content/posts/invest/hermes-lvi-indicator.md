---
title: 'Hermes Liquidity Vacuum Index (LVI)'
description: 'The LVI is designed to identify "Sling-shot" reversals that occur when price enters a structural "vacuum" (extreme LVN) while simultaneously…'
pubDate: 2026-05-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_LVI_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity Vacuum Index (LVI)

## 💡 Conceptual Origin
The LVI is designed to identify "Sling-shot" reversals that occur when price enters a structural "vacuum" (extreme LVN) while simultaneously experiencing a climax in order flow delta and macro volatility.

## ⚙️ Logic & Heuristic
The LVI monitors the convergence of three disparate signals:

1. **Structural Vacuum (S)**: Price is currently within a $\pm 0.5\%$ range of a verified **Extreme Low Volume Node (LVN)** (from Volume Profile).
2. **Delta Exhaustion (D)**: The 1-minute Delta reaches $\pm 3\sigma$ (statistical extreme) but price fails to make a new local high/low (Absorption).
3. **Volatility Spike (V)**: The Macro Volatility Index (e.g., VIX or asset-specific ATR) is in the top 10% of its 30-day range.

### Formula (Heuristic):
$$\text{LVI Score} = \frac{(\text{Delta Magnitude} \times \text{Vol Spike})}{\text{Volume Density at Price}}$$

**Signal Condition**: 
- **LVI $\uparrow$ (Extreme)** $+$ **Price in LVN** $\rightarrow$ **Sling-shot Reversal Trigger**.

## 📈 Historical Pattern
- **The "Vacuum Snap"**: Price aggressively pushes into an LVN (where there are no limit orders to slow it down). As it hits the "far wall" of the vacuum, it encounters a massive institutional block (Absorption) during a volatility spike. The resulting "snap back" is typically violent and rapid as price returns to the nearest HVN.

## 🛠️ Application in TJB
`LVI Extreme $\rightarrow$ Price in LVN + Delta Exhaustion $\rightarrow$ High-probability contrarian reversal; Target nearest HVN.`
