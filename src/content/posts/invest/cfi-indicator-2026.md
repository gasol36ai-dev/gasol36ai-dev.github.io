---
title: 'Proprietary Indicator: The Coherence-Fragility Index (CFI)'
description: 'The CFI maps the intersection of Algorithmic Coherence (from Swarm intelligence) and Fractal Liquidity Dimension (from Macro-Financial Fract…'
pubDate: 2026-06-12
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/Proprietary_Indicators/cfi_indicator_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: The Coherence-Fragility Index (CFI)
## Framework: Map-Trigger-Lock

### 1. Map (The Terrain)
The CFI maps the intersection of **Algorithmic Coherence** (from Swarm intelligence) and **Fractal Liquidity Dimension** (from Macro-Financial Fractals).
- **X-Axis: Coherence Score ($\mathcal{C}$)** - Measured by the cross-correlation of order-flow signatures across the top 50 AI-driven trading swarms.
- **Y-Axis: Fractal Dimension ($D$)** - The box-counting dimension of the LOB (Limit Order Book) depth.

### 2. Trigger (The Signal)
The trigger occurs when a **"Phase-Squeeze"** is detected:
- **Condition:** $\mathcal{C} \to 1.0$ (High Coherence) AND $D \to 1.0$ (Low Fractal Dimension).
- **Signal:** When the CFI exceeds a threshold $\Theta$ (calculated as the 95th percentile of the 30-day rolling mean), it triggers a **"Synthetic Herd Warning"**.

### 3. Lock (The Execution)
The lock defines the definitive action to mitigate the fragility:
- **Action:** Immediate transition to **"Asymmetric Liquidity Provision"**.
- **Execution:** Close all high-gamma positions and move to a long-volatility / wide-spread market-making strategy.
- **Exit Lock:** When $D$ recovers to $> 1.5$ or $\mathcal{C}$ drops below $0.6$.

### Synthesis Formula
$$CFI = \frac{\mathcal{C}}{(D - 1.0) + \epsilon}$$
*(Where $\epsilon$ is a smoothing constant to prevent division by zero at the critical point $D=1$)*

### Strategic Value
The CFI provides a leading indicator of "flash-fragility," allowing the system to exit positions *before* the liquidity void manifests in price action.
