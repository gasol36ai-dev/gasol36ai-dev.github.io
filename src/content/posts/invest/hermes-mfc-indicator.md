---
title: 'Hermes Proprietary Indicators: Macro-Flow Convergence (MFC)'
description: 'Based on the observation that macroeconomic news often creates a "first-wave" price move, but the sustainability of that move is determined …'
pubDate: 2026-05-17
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Hermes_MFC_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Proprietary Indicators: Macro-Flow Convergence (MFC)

## Indicator: Hermes Macro-Flow Convergence (MFC)
**Objective**: Detect high-probability reversals by identifying "Exhaustion Divergence" between Macro Sentiment and Microstructure Order Flow.

### Theoretical Foundation
Based on the observation that macroeconomic news often creates a "first-wave" price move, but the sustainability of that move is determined by the *Order Flow Imbalance (OFI)*.

### Logic & Calculation
1. **Macro Sentiment Signal ($S_{macro}$)**: Aggregated sentiment from the War Room reports (Positive/Negative/Neutral).
2. **Order Flow Momentum ($M_{flow}$)**: 3-period rolling Z-score of Cumulative Delta.
3. **Convergence State**:
    - **Bullish Convergence**: $S_{macro}$ is positive AND $M_{flow}$ is rising. (Strong Trend)
    - **Bearish Convergence**: $S_{macro}$ is negative AND $M_{flow}$ is falling. (Strong Trend)
    - **Exhaustion Divergence (The Signal)**: 
        - $S_{macro}$ is positive BUT $M_{flow}$ has turned sharply negative for $\ge 3$ periods.
        - $S_{macro}$ is negative BUT $M_{flow}$ has turned sharply positive for $\ge 3$ periods.

### Judgment Heuristic
- When **Exhaustion Divergence** occurs, the "Macro-Driven" move is no longer supported by institutional aggressive flow. 
- **Action**: Trigger "Counter-Trend Alert." The probability of a mean-reversion or reversal increases significantly as the market has "priced in" the macro news but is now seeing institutional distribution/accumulation in the opposite direction.

### Validation Pattern
This mirrors the US Treasury turbulence of April 2025, where high volume without commensurate OFI led to tighter price ranges despite macro surprises.
