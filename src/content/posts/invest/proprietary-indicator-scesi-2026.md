---
title: 'Proprietary Indicator: Sovereign Compute-Energy Synchrony Index (SCESI)'
description: 'The Sovereign Compute-Energy Synchrony Index (SCESI) is a multi-domain composite indicator designed to measure the structural stability of a'
pubDate: 2026-06-07
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Proprietary_Indicator_SCESI_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Sovereign Compute-Energy Synchrony Index (SCESI)

## 1. Overview
The **Sovereign Compute-Energy Synchrony Index (SCESI)** is a multi-domain composite indicator designed to measure the structural stability of a nation's or enterprise's AI compute capacity relative to its energy and thermal management infrastructure. It identifies inflection points where the demand for AI inference/training exceeds the physical "anchors" of energy and cooling, signaling either a massive scaling opportunity or a critical sovereign risk.

## 2. Component Metrics (The Triple Anchor)

### A. Baseload-to-Peak Energy Ratio (BPER)
- **Definition**: The ratio of reliable, constant-power sources (e.g., Nuclear SMRs, Hydro, Geothermal) to intermittent sources (e.g., Solar, Wind) within the targeted compute cluster's local grid.
- **Significance**: A high BPER ensures that AI workloads (especially long-running training jobs) can be sustained without catastrophic interruption or massive energy-cost volatility.
- **Target Regime**: $BPER \ge 0.7$ for "Stable Sovereign Compute".

### B. Thermal Sink Efficiency Delta (TSED)
- **Definition**: The deviation of current Power Usage Effectiveness (PUE) from the theoretical minimum allowed by the local environment (e.g., subsea, arctic, or advanced liquid cooling).
- **Significance**: As AI compute scales, thermal management becomes the primary physical bottleneck. A rising TSED indicates that the infrastructure is approaching its thermal limit, necessitating expensive retrofits or relocation.
- **Metric**: $TSED = PUE_{actual} / PUE_{ideal\_local}$.

### C. Compute-Energy Volatility Correlation (CEVC)
- **Definition**: The Pearson correlation coefficient between high-frequency compute demand (API calls, FLOPs utilization) and local energy spot prices.
- **Significance**: High correlation indicates that the compute infrastructure is "grid-exposed" and highly vulnerable to energy market shocks. Low correlation indicates successful "behind-the-meter" (BTM) energy integration (e.g., co-located SMRs).

## 3. The SCESI Formula (Conceptual)
$$SCESI = \frac{BPER \times (1 / TSED)}{1 + CEVC}$$

*Note: Higher SCESI values indicate a robust, vertically integrated, and stable compute-energy ecosystem.*

## 4. Strategic Application (Map-Trigger-Lock)

### 🗺️ Map (The Signal)
- **SCESI $\uparrow$ (Expansion Signal)**: High baseload stability, high thermal efficiency, and low energy correlation.
- **SCESI $\downarrow$ (Risk Signal)**: Low baseload, thermal saturation, and high energy price volatility exposure.

### ⚡ Trigger (The Inflection Point)
- **Expansion Trigger**: $SCESI > \tau_{high}$ AND [Local Energy Surplus Detected].
- **Risk Trigger**: $SCESI < \tau_{low}$ OR [Thermal Delta > 15% in 30 days].

### 🔒 Lock (The Action)
- **Expansion Lock**: Trigger aggressive CAPEX for co-located SMR/Energy infrastructure or Subsea compute expansion.
- **Risk Lock**: Execute "Inference Deflection" (rerouting non-critical compute to stable nodes) and increase energy-price hedging.

## 5. Strategic Value
## 6. Implementation Challenges & Mitigations
- **Data Latency**: Real-time CEVC requires high-frequency telemetry from both the compute layer and the energy grid.
  - *Mitigation*: Integration with smart meter APIs and data center power management systems (e.g., Open Compute Project standards).
- **Regulatory Divergence**: SMR deployment and subsea infrastructure face varied jurisdictional challenges.
  - *Mitigation*: Use of "Regulatory-Agnostic" design principles and focus on international waters/special economic zones.
- **Thermal Inertia**: The time lag between compute demand spikes and thermal response.
  - *Mitigation*: Predictive thermal modeling using AI-driven forecasting to pre-cool or pre-heat environments.

SCESI provides a single decision gate for:
1. **Sovereign Fund Allocation**: Deciding between domestic compute infrastructure vs. foreign cloud reliance.
2. **Hyperscaler Site Selection**: Evaluating the long-term viability of new data center regions.
3. **Energy-Compute Vertical Integration**: Validating the ROI of nuclear/renewable-to-compute projects.

---
*Created: 2026-06-07 via Evolution Engine (Deep Mode)*
*Status: Experimental / Proprietary*
