---
title: 'Research Report: Post-Quantum Financial Microstructure (PQC-FM)'
description: 'The transition to Post-Quantum Cryptography (PQC) represents a systemic necessity for the global financial microstructure. The "Store Now, D'
pubDate: 2026-06-15
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/pqc_fm.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Research Report: Post-Quantum Financial Microstructure (PQC-FM)

## 1. Executive Summary
The transition to Post-Quantum Cryptography (PQC) represents a systemic necessity for the global financial microstructure. The "Store Now, Decrypt Later" (SNDL) threat necessitates immediate migration of long-term financial assets and the underlying rails. This report analyzes the intersection of PQC and financial microstructure, specifically targeting Central Bank Digital Currencies (CBDC), High-Frequency Trading (HFT) latency, and the resilience of financial rails.

## 2. PQC Integration in CBDCs
CBDCs introduce a centralized yet digitally distributed ledger for sovereign currency. The integration of PQC is critical because CBDCs often aim for longevity and systemic trust.

### 2.1 Cryptographic Transitions
- **Signature Schemes:** Transition from ECDSA/EdDSA to ML-DSA (Dilithium) and SLH-DSA (Sphinx+). ML-DSA provides a balance of performance and size, whereas SLH-DSA offers high security based on hash functions but with significantly larger signatures.
- **Key Encapsulation:** Integration of ML-KEM (Kyber) for secure channel establishment between the Central Bank, commercial intermediaries, and end-users.

### 2.2 Architectural Challenges
- **Transaction Volume:** The increased size of PQC signatures (ML-DSA signatures are $\sim 2.4$ KB compared to $\sim 64$ bytes for EdDSA) increases the data load per transaction.
- **Storage Overhead:** State-bloat in CBDC ledgers will accelerate, requiring more aggressive pruning or sharding strategies to maintain throughput.

## 3. HFT Latency and PQC
High-Frequency Trading (HFT) operates in the microsecond ($\mu s$) and nanosecond ($ns$) regime. PQC introduces significant computational and data overhead.

### 3.1 Computational Latency
- **KEM Handshakes:** The time to establish a quantum-resistant session key using ML-KEM is slightly higher than X25519. While negligible for retail, it is a bottleneck for HFT order-entry gateways.
- **Verification Speed:** ML-DSA verification is efficient, but the time spent parsing larger packets can increase the "tick-to-trade" latency.

### 3.2 Network Microstructure Impact
- **MTU Fragmentation:** Larger PQC signatures may exceed the standard Ethernet Maximum Transmission Unit (MTU) of 1500 bytes, leading to packet fragmentation. This introduces non-deterministic jitter and increases the probability of packet loss, which is catastrophic for HFT.
- **Hardware Acceleration:** Migration will require FPGA-based PQC accelerators to offload ML-KEM and ML-DSA operations to maintain sub-microsecond execution.

## 4. Quantum-Resistant Financial Rails
Financial rails (SWIFT, FedWire, TARGET2) are the backbone of global liquidity.

### 4.1 Inter-Bank Settlement
- **Hybrid Certificates:** Implementation of "Hybrid" certificates combining classical (RSA/ECC) and PQC signatures to ensure backward compatibility during the transition period.
- **Quantum Key Distribution (QKD):** For critical back-haul links between central hubs, QKD provides information-theoretic security that does not rely on computational hardness.

### 4.2 Liquidity Management
- **Atomic Settlement:** PQC-enabled atomic swaps ensure that the transfer of assets and payments occurs simultaneously without exposure to quantum-enabled interception during the "handshake" phase.

## 5. Transmission Mapping: Quantum Threat to Microstructure
The following mapping delineates how quantum capabilities propagate through the financial system and the corresponding PQC mitigations.

| Threat Vector | Affected Component | PQC Mitigation | Microstructure Impact |
| :--- | :--- | :--- | :--- |
| Shor's Algorithm | Public Key Infrastructure (PKI) | ML-DSA / SLH-DSA | Increased certificate size; slower handshake |
| SNDL (Store Now Decrypt Later) | Inter-bank Communication | ML-KEM (Kyber) | Immediate need for KEM updates on all rails |
| Grover's Algorithm | Symmetric Encryption/Hashing | AES-256 / SHA-3 | Double key lengths; minimal latency impact |
| Quantum Man-in-the-Middle | Order Routing (HFT) | Hybrid PQC-ECC Signatures | Packet fragmentation; increased jitter |
| Quantum State Manipulation | Ledger Consensus | Quantum-Resistant VRFs | Higher compute overhead for leader election |

## 6. Conclusion and Recommendations
The financial microstructure is highly sensitive to latency and data volume. The transition to PQC is not a simple "drop-in" replacement but requires a fundamental redesign of packet handling and hardware acceleration.
1. **Prioritize KEM:** Implement ML-KEM immediately to mitigate SNDL threats.
2. **Hardware Offloading:** Invest in FPGA/ASIC accelerators for ML-DSA to protect HFT competitive edges.
3. **MTU Optimization:** Evaluate Jumbo Frames or custom transport protocols to handle larger PQC signatures without fragmentation.
