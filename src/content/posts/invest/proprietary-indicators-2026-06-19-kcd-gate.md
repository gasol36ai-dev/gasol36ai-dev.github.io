---
title: 'Proprietary Indicator: Kinetic-Cyber Discrepancy (KCD) Gate'
description: 'The Kinetic-Cyber Discrepancy (KCD) Gate is a high-fidelity judgment indicator designed to detect sophisticated cyber-physical attacks (e.g.…'
pubDate: 2026-06-19
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/Proprietary_Indicators_2026-06-19_KCD_Gate.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Kinetic-Cyber Discrepancy (KCD) Gate
**Date:** 2026-06-19
**Category:** Cyber-Kinetic Security / Industrial Intelligence
**Status:** Synthesized Proprietary Logic

## 1. Conceptual Overview
The **Kinetic-Cyber Discrepancy (KCD) Gate** is a high-fidelity judgment indicator designed to detect sophisticated cyber-physical attacks (e.g., Stuxnet-style sensor spoofing) by identifying the divergence between the reported digital state and the observable kinetic reality.

Traditional cybersecurity monitors the *bits*; CKD monitors the *momentum*.

## 2. Transmission Mapping: [Event] $\\rightarrow$ [Mechanism] $\\rightarrow$ [Reaction]

### I. The Discrepancy Trigger
- **[Event]**: An anomaly is detected between a digital sensor readout (e.g., a pressure, temperature, or rotational speed signal) and an independent, non-digital physical measurement (e.g., acoustic resonance, thermal radiation, or mechanical inertia).
- **[Mechanism]**: **Temporal-Kinetic Correlation Analysis**. The system compares the *expected* physical response time (governed by laws of thermodynamics and mechanics) against the *reported* digital transition.
- **[Reaction]**: If $\\text{Discrepancy} > \\text{Threshold} \\text{ ($\\delta$)},$ the system triggers an immediate "Kinetic Safe-State" (e.g., mechanical hard-stop or emergency decoupling).

### II. The Multi-Vector Convergence (The Gate)
A "High-Confidence" KCD signal requires convergence across at least two distinct physical modalities:
1. **Signal-to-Physics Divergence**: $\\text{Digital State } (S_d) \\neq \\text{Physical State } (S_p)$.
2. **Response-Time Incongruity**: $\\Delta t_{\\text{reported}} \\ll \\Delta t_{\\text{physical\_limit}}$.

## 3. Mathematical Formalization
The KCD Gate triggers when the **Kinetic Divergence Index ($\\text{KDI}$)** exceeds a critical threshold $\\sigma$:

$$\\text{KDI} = \\alpha \\cdot \\left| \\frac{S_d - S_p}{S_p} \\right| + \\beta \cdot \\left| \\frac{\Delta t_{\\text{reported}}}{\Delta t_{\\text{physical\_limit}}} - 1 \\right|$$

$$\\text{KCD}_{Active} = 1 \\iff \\text{KDI} > \\sigma$$

Where:
- $\\alpha, \\beta$: Weighting coefficients for magnitude vs. timing discrepancy.
- $S_d, S_p$: Digital and Physical states.
- $\Delta t_{\\text{reported}}$: The time interval recorded by the digital control system.
- $\Delta t_{\\text{physical\_limit}}$: The minimum theoretical time required for the physical transition (based on system inertia/thermodynamics).

## 4. Strategic Value & Action
- **Primary Use Case**: Detection of "Invisible" attacks where digital monitors are compromised but physical actuators are being manipulated.
- **Decision Logic**:
    - **KCD $\rightarrow 0$ (Normal)**: Continue autonomous operations.
    - **KCD $\rightarrow 1$ (Gate Open)**: **IMMEDIATE KINETIC ISOLATION.** Decouple digital control from mechanical actuators and transition to manual/mechanical fail-safe mode.

---
**[END OF PROPRIETARY INDICATOR]**
