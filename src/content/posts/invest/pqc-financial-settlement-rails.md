---
title: 'Research Report: Post-Quantum Cryptography (PQC) in Financial Settlement Rails'
description: 'The arrival of a Cryptographically Relevant Quantum Computer (CRQC) poses a systemic risk to global financial stability. Financial settlemen'
pubDate: 2026-06-23
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/PQC_Financial_Settlement_Rails.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Research Report: Post-Quantum Cryptography (PQC) in Financial Settlement Rails

## 1. Executive Summary
The arrival of a Cryptographically Relevant Quantum Computer (CRQC) poses a systemic risk to global financial stability. Financial settlement rails—the critical infrastructure facilitating the transfer of value between central banks and commercial institutions (e.g., FedWire, SWIFT, TARGET2, CHIPS)—rely almost exclusively on asymmetric cryptography (RSA, ECC) for authentication, integrity, and confidentiality. This report analyzes the transition to Post-Quantum Cryptography (PQC) within these rails, focusing on algorithmic selection, infrastructure constraints, and migration strategies.

## 2. The Quantum Threat Vector in Finance
### 2.1. The Collapse of the Trust Root
The primary threat is Shor's Algorithm, which can factorize large integers and compute discrete logarithms in polynomial time. This effectively renders RSA, Diffie-Hellman, and Elliptic Curve Cryptography (ECC) obsolete. In settlement rails, this compromises:
- **Transaction Signing**: Forged signatures allowing unauthorized movement of funds.
- **Secure Key Exchange**: Interception of session keys used to encrypt inter-bank communications.
- **Identity Verification**: Breakdown of the PKI (Public Key Infrastructure) that verifies the identity of participating financial institutions.

### 2.2. "Store Now, Decrypt Later" (SNDL)
Financial data has long-term sensitivity. Adversaries may capture encrypted settlement traffic today to decrypt it once a CRQC is available. For systemic settlement rails, this exposes historical transaction patterns, sensitive liquidity positions, and strategic sovereign movements.

## 3. PQC Algorithmic Landscape for Settlement
The industry is aligning with NIST's PQC standardization process. The following primitives are critical for settlement rails:

### 3.1. Key Encapsulation Mechanisms (KEMs)
- **ML-KEM (Kyber)**: Lattice-based. Preferred for general encryption and secure key exchange due to high efficiency and relatively small key sizes.
- **Use Case**: Establishing secure TLS channels for RTGS (Real-Time Gross Settlement) communications.

### 3.2. Digital Signature Schemes (DSS)
- **ML-DSA (Dilithium)**: Lattice-based. Offers a strong balance of performance and signature size.
- **SLH-DSA (SPHINCS+)**: Hash-based. Slower and larger signatures but relies on minimal security assumptions, making it a "fail-safe" backup.
- **Falcon**: Lattice-based. Extremely compact signatures, ideal for bandwidth-constrained legacy rails, but computationally complex to implement.
- **Use Case**: Signing payment instructions, settlement confirmations, and audit logs.

## 4. Implementation Challenges in Settlement Infrastructure
### 4.1. The "Message Size" Problem
Legacy settlement rails often use rigid message formats (e.g., SWIFT MT messages). PQC signatures and keys are orders of magnitude larger than ECC equivalents:
- **ECC Signature**: ~64 bytes.
- **ML-DSA Signature**: ~2,400 bytes.
- **Impact**: This increase can exceed MT buffer limits, requiring a mandatory transition to ISO 20022 (XML-based), which is more flexible but increases parsing overhead.

### 4.2. Computational Latency
RTGS systems require sub-millisecond finality for high-volume liquidity management. While ML-KEM is fast, the increased computational load of PQC verification across millions of daily transactions may necessitate hardware acceleration (e.g., FPGA/ASIC) in HSMs (Hardware Security Modules).

### 4.3. The Hybrid Transition Period
A "big bang" migration is impossible. Rails must implement **Hybrid Cryptography**:
- **Dual Signatures**: Every transaction is signed with both a classical (ECC) and a PQC (ML-DSA) signature.
- **Dual KEMs**: Key exchange combines a classical secret and a PQC secret.
- **Benefit**: Ensures security against current threats while providing quantum resistance, preventing a single point of failure during the transition.

## 5. Strategic Migration Roadmap
### Phase I: Quantum Risk Inventory
- Mapping all cryptographic assets across the rail.
- Identifying "High-Value/Long-Life" data subject to SNDL.
- Auditing third-party dependencies (VPNs, HSM vendors).

### Phase II: Cryptographic Agility Implementation
- Abstracting the crypto-layer from the application logic.
- Implementing "Pluggable" algorithms to allow rapid swapping as standards evolve.

### Phase III: Pilot Hybrid Integration
- Deploying hybrid signatures in non-critical settlement channels.
- Testing the impact of larger packet sizes on network latency and throughput.

### Phase IV: Full PQC Cutover
- Deprecating classical algorithms.
- Transitioning to pure PQC or high-assurance hybrid modes.

## 6. Integration with Digital Assets and CBDCs
Central Bank Digital Currencies (CBDCs) provide a unique opportunity to integrate PQC from the genesis block. By utilizing quantum-resistant ledger technologies (e.g., hash-based signatures for wallet addresses), CBDCs can bypass the legacy "technical debt" of traditional RTGS systems.

## 7. Conclusion
The transition to PQC in financial settlement rails is not merely a technical update but a requirement for systemic survival. The primary bottleneck is not the mathematics of PQC, but the architectural rigidity of legacy financial messaging. Priority must be given to **Cryptographic Agility** and the adoption of **ISO 20022** to accommodate the larger payloads of the post-quantum era.
