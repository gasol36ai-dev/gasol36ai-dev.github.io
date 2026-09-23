---
title: 'Hybrid Bonding'
description: 'Hybrid Bonding (Cu-to-Cu) is a bumpless interconnect technology that bonds copper pads and dielectric surfaces simultaneously, creating a di…'
pubDate: 2026-07-11
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/Hybrid_Bonding.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hybrid Bonding
**Type:** Concept
**Domain:** Advanced Packaging 2.0 / Hardware Security

## Definition
Hybrid Bonding (Cu-to-Cu) is a bumpless interconnect technology that bonds copper pads and dielectric surfaces simultaneously, creating a direct metal-to-metal connection.

## Technical Leap
- **Pitch Reduction:** Moves from $\sim$10$\mu$m micro-bumps to <1$\mu$m hybrid bonds.
- **Interconnect Density:** Increases the number of vertical connections by $10\times$ to $100\times$.
- **Electrical Performance:** Significantly lower parasitic capacitance and resistance compared to bumps.

## Security & Trust Vectors
Hybrid bonding is not just a performance leap but a security boundary:
- **Physical Unclonability**: The precise alignment and bonding pressure create unique contact resistances at each bond point. This can be leveraged as a "Bond-PUF" to authenticate that a specific die was bonded to a specific substrate.
- **Anti-Tamper Boundaries**: The seamless transition between the dielectric and copper in hybrid bonding makes it significantly harder for attackers to insert "interposer shims" or probes compared to traditional micro-bumps.
- **Die-to-Die Authentication**: Secure handshakes can be performed at the bonding interface to ensure only authorized chiplets are integrated into the 3D stack.

## Strategic Bottleneck
Requires extreme surface planarity (CMP) and ultra-clean environments, making the equipment (e.g., EVG, Besi) a geopolitical chokepoint. Controlling the hybrid bonding process is equivalent to controlling the "Trust Root" of the hardware.

**Related**: [[3D-IC]], [[Advanced_Packaging_2.0]], [[Hardware_Rooted_Zero_Trust]]
