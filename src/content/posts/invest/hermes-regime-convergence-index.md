---
title: 'Hermes Regime Convergence Index (HRCI)'
description: 'The HRCI is designed to filter "Noise" from "Signal" by quantifying the convergence between Structural Phase and Liquidity Distribution. It '
pubDate: 2026-04-30
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_Regime_Convergence_Index.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Regime Convergence Index (HRCI)
**Status:** PROPRIETARY / EXPERIMENTAL
**Version:** 1.0.0
**Last Updated:** 2026-04-30

## 🎯 Objective
The HRCI is designed to filter "Noise" from "Signal" by quantifying the convergence between **Structural Phase** and **Liquidity Distribution**. It answers: *"Is this move a structural shift or a liquidity trap?"*

## 🧬 The Logic
The index correlates three disparate variables into a single conviction score.

### The Variables
1. **Wave Strength ($\omega$):**
   - $1.0$ for Impulsive Waves (Wave 3, Wave 5).
   - $0.5$ for Complex Correctives (WXY).
   - $0.1$ for Terminal/Exhaustion patterns.
2. **Liquidity Delta ($\Delta L$):**
   - Measured by the rate of change in Open Interest (OI) relative to price move.
   - Positive if OI increases with price (Strong Trend).
   - Negative if OI decreases with price (Weakness/Liquidation).
3. **Volume Concentration ($\nu$):**
   - The distance of current price from the Point of Control (POC).
   - Low $\nu$ = Price is at POC (High Acceptance/Resistance).
   - High $\nu$ = Price is in a Low Volume Node (High Momentum/Vacuum).

## 🧮 The Heuristic
$HRCI = \frac{\omega \times \Delta L}{\nu}$

### Interpretation
- **High HRCI ($> 0.8$): High Conviction Trend.** 
  - *Condition:* Impulsive Wave + Rising OI + Price moving away from POC.
  - *Action:* Trend Following / Aggressive Entry.
- **Medium HRCI ($0.3 - 0.8$): Distribution/Range.**
  - *Condition:* Corrective Wave + Stagnant OI + Price hovering around POC.
  - *Action:* Mean Reversion / Scalping.
- **Low HRCI ($< 0.3$): Liquidity Trap / Imminent Reversal.**
  - *Condition:* Terminal Pattern + Extreme OI (Overcrowded) + Price hitting a major Volume Node.
  - *Action:* Contrarian Bet / Exit Positions.

## 🧪 Historical Pattern Validation
- **Case A (The Squeeze):** Price breaks resistance $\rightarrow$ $\omega=1$, $\Delta L \uparrow$, $\nu \uparrow$ $\rightarrow$ HRCI spikes $\rightarrow$ Parabolic move.
- **Case B (The Fake-out):** Price breaks resistance $\rightarrow$ $\omega=0.5$, $\Delta L \downarrow$, $\nu \downarrow$ $\rightarrow$ HRCI remains low $\rightarrow$ Immediate reversal to POC.

## 🔗 Integration
Cross-reference with [[Investment/Technical_Analysis/NEoWave_Confluence_Framework]] for structural validation.
