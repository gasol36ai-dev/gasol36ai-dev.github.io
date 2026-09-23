---
title: 'ML-KEM Edge Mapping'
description: 'The process of fragmenting, sequencing, and mapping ML-KEM (Module-Lattice-based Key Encapsulation Mechanism, formerly Kyber) ciphertexts an…'
pubDate: 2026-07-08
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/ML-KEM_Edge_Mapping.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# ML-KEM Edge Mapping
**Atomic Concept: Communication Efficiency**

## Definition
The process of fragmenting, sequencing, and mapping ML-KEM (Module-Lattice-based Key Encapsulation Mechanism, formerly Kyber) ciphertexts and public keys across low-bandwidth, low-power edge protocols such as BLE (Bluetooth Low Energy), Zigbee, and IEEE 802.15.4.

## Transmission Mappings
- **[KEM Ciphertext Generation] $\rightarrow$ [Multi-Frame Segmentation] $\rightarrow$ [Duty Cycle Increase]**: Generating a ~1KB ciphertext requires the radio to remain active for multiple transmission cycles, significantly increasing the device's power consumption and duty cycle.
- **[Frame Drop in KEM Sequence] $\rightarrow$ [Partial Payload Discard] $\rightarrow$ [Handshake Restart]**: Since ML-KEM requires the full ciphertext for decapsulation, the loss of a single frame in a 9-frame sequence renders the entire key useless, forcing a costly full re-transmission.
- **[Edge Mapping Layer Execution] $\rightarrow$ [CPU Cycle Spike] $\rightarrow$ [Interrupt Latency]**: The overhead of managing sequence numbering, checksums, and buffer reassembly on low-power MCUs increases CPU load, potentially delaying time-critical sensor interrupts.

## Technical Detail
The mapping layer solves a fundamental size mismatch:
- **ML-KEM-768 Ciphertext**: ~1088 bytes.
- **IEEE 802.15.4 Frame**: 127 bytes (maximum).
- **Result**: A single key exchange requires a sequence of approximately 9–11 frames.

The **"Mapping Layer"** implements:
1. **Sequence Indexing**: Each frame is tagged with a position index to allow out-of-order reassembly.
2. **Integrity Checksums**: Per-frame and per-payload CRC checks to ensure the ciphertext is not corrupted during the fragmentation process.
3. **Sliding Window Acknowledgement**: A lightweight ACK mechanism to request only missing frames rather than the full payload.

## Strategic Value
Enables quantum-secure key exchange on legacy IoT hardware and constrained devices that cannot support jumbo frames or high-MTU networks. This ensures that "the edge" is not the weakest link in a post-quantum security architecture.
