---
title: 'PQC-FM: Post-Quantum Financial Microstructure Wiki'
description: 'This wiki serves as a knowledge base for the integration of Post-Quantum Cryptography (PQC) into the global financial microstructure.'
pubDate: 2026-06-15
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/pqc_fm_core.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# PQC-FM: Post-Quantum Financial Microstructure Wiki

This wiki serves as a knowledge base for the integration of Post-Quantum Cryptography (PQC) into the global financial microstructure.

## Core Concepts
- **PQC-FM:** The study of how quantum-resistant cryptographic primitives affect the operational characteristics (latency, throughput, data volume) of financial systems.
- **SNDL (Store Now, Decrypt Later):** The threat where adversaries collect encrypted data today to decrypt it once a cryptographically relevant quantum computer (CRQC) exists.
- **CRQC:** Cryptographically Relevant Quantum Computer.

## Key Algorithms (NIST PQC Standard)
- **ML-KEM (Kyber):** Module-Lattice-based Key Encapsulation Mechanism. Used for secure key exchange.
- **ML-DSA (Dilithium):** Module-Lattice-based Digital Signature Algorithm. Used for transaction signing and identity.
- **SLH-DSA (Sphinx+):** Stateless Hash-based Digital Signature Algorithm. Used for long-term archival and root keys.

## Financial Domain Impact
### CBDCs
- **Issue:** Increased signature size leads to ledger bloat.
- **Solution:** Implementation of signature aggregation or zero-knowledge proofs (ZKP) to compress PQC signatures.

### HFT (High-Frequency Trading)
- **Issue:** Packet fragmentation due to ML-DSA signature size exceeding 1500-byte MTU.
- **Solution:** Hardware acceleration (FPGA) and optimization of transport layers.

### Financial Rails
- **Issue:** Legacy system incompatibility with larger PQC keys.
- **Solution:** Hybrid certificates (combining ECC and PQC).
