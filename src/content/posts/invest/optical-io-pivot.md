---
title: 'Concept: The Optical I/O Pivot (CPO)'
description: 'AI cluster scaling is fundamentally a data-movement problem. The "Electrical Wall" occurs when the energy required to move a bit across a PC'
pubDate: 2026-07-09
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/optical_io_pivot.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Concept: The Optical I/O Pivot (CPO)

## Core Thesis
AI cluster scaling is fundamentally a data-movement problem. The "Electrical Wall" occurs when the energy required to move a bit across a PCB exceeds the energy required to compute on that bit. Co-Packaged Optics (CPO) solves this by collapsing the distance between the compute core and the optical medium.

## Conceptual Model: [Electrical] $\rightarrow$ [Optical]
- **Electrical Logic**: High speed = High loss. To maintain signal integrity at 224Gbps, we must "push" harder (more power) or "clean" more (retimers).
- **Optical Logic**: Distance is irrelevant to signal integrity (low loss). The cost is shifted to the *conversion* (E-O/O-E).
- **The Pivot**: By moving the conversion point (Optical Engine) into the package, we eliminate the "pushing" and "cleaning" phases of the electrical journey.

## Key Architectural Shifts
1. **Decoupled Light Source**: Moving lasers away from the heat source (ASIC) to prevent wavelength drift and degradation.
2. **Bandwidth Density**: Shifting from faceplate-limited I/O (pluggable) to package-edge-limited I/O, enabling orders of magnitude more lanes per $\text{mm}^2$.
3. **Thermal Synergy**: Integrating optical engines into the liquid-cooling envelope of the GPU/TPU, treating the photonic layer as part of the primary thermal load.

## Critical Metric
**pJ/bit (pico-Joules per bit)**: The ultimate measure of interconnect efficiency. CPO aims to drive this below 5 pJ/bit to enable sustainable AI scaling.
