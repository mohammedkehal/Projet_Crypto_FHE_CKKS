# 🛡️ Zero-Trust Financial Scoring Architecture (FHE CKKS)

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![Docker](https://img.shields.io/badge/docker-✓-2496ED.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)

**🔐 Cloud AI + Absolute Banking Secrecy = Finally Reconciled**

</div>

---

## 📖 Overview

This project implements a **Zero-Trust Architecture** for financial credit scoring using **Fully Homomorphic Encryption (FHE)** with the **CKKS scheme** (Cheon-Kim-Kim-Song, 2017).

The core innovation: a Cloud FinTech evaluates its AI model **directly on encrypted client data** without ever decrypting it. The bank is the sole entity capable of decrypting the final credit score. This preserves **absolute banking secrecy** while leveraging external Cloud computing power.

> **Propriété fondamentale :** $\text{Decrypt}(f(\text{Encrypt}(x))) = f(x)$ — *The Cloud computes without seeing.*

---

## 🎯 Key Features

### 🔐 Post-Quantum Cryptography
- Security based on the **RLWE (Ring Learning With Errors)** problem
- Polynomial ring: $\mathcal{R}_q = \mathbb{Z}_q[X]/(X^N + 1)$ with $N = 8192$
- Scale factor $\Delta = 2^{40}$ for floating-point precision preservation
- Resistant to both classical and quantum attacks (NIST post-quantum candidate)

### 📊 CKKS Scheme — Finance Native
- **The only FHE scheme** natively handling floating-point real numbers
- Essential for financial ratios, interest rates (e.g., $5.25\%$), debt ratios ($0.33$), and continuous risk scores
- Approximate arithmetic with configurable precision

### 🔒 End-to-End Encryption
Strict modular separation between two environments:

| Environment | Location | Files | Has Secret Key? |
|------------|----------|-------|-----------------|
| 🏦 **Banking Enclave** | `bank_client/` | `keygen.py`, `encrypt.py`, `decrypt.py` | ✅ Yes |
| ☁️ **Cloud FinTech** | `fintech_cloud/` | `homomorphic_evaluation.py`, `ai_scoring_model.py` | ❌ No |
| 🔄 **Shared Zone** | `shared_data/` | Ciphertexts only | — |

### 🖥️ SOC Command Center
Real-time interactive dashboard built with **Streamlit**:
- Visualize RLWE parameters ($N$, $\Delta$)
- Monitor polynomial noise simulation in 3D
- Execute the 3-phase pipeline with one-click buttons
- Observe live execution logs

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.10+ | Core logic |
| **Cryptography** | [TenSEAL](https://github.com/OpenMined/TenSEAL) | FHE operations (Microsoft SEAL wrapper) |
| **Frontend/SOC** | [Streamlit](https://streamlit.io/) | Interactive dashboard |
| **3D Visualization** | Plotly | Polynomial noise representation |
| **Infrastructure** | [Docker](https://www.docker.com/) | Containerized isolation |
| **CI/CD** | GitHub Actions *(planned)* | Automated testing & deployment |
| **Orchestration** | Kubernetes *(planned)* | Production-scale pod separation |

---

## 🏗️ Architecture Flow
═══════════════════════════════════════════════════════════════════════
                    PHASE 1: BANQUE CLIENTE (Trusted Enclave)
═══════════════════════════════════════════════════════════════════════

  Données Brutes z ∈ R^(N/2)
  [4500.0, 1200.5, 710.0, 34.0]
         │
         ▼
  Encodage Δ = 2^40  ──►  Polynôme m ∈ R_q
         │
         ▼
  Chiffrement RLWE  ──►  c = (c₀, c₁)

  🔑 sk (gardée localement)  │  📤 pk, evk, c → Cloud

═══════════════════════════════════════════════════════════════════════
                    PHASE 2: CLOUD FINTECH (Zero-Trust)
═══════════════════════════════════════════════════════════════════════

  📥 Réception de pk, evk, c
         │
         ▼
  Modèle IA: W = [0.4, -0.7, 0.2, 0.1], Biais = +10.5
         │
         ▼
  Évaluation Homomorphe: c_res = c · W + Biais
  (Additions, Multiplications, Relinéarisation, Rescaling)
         │
         ▼
  Bruit critique ? ──► Non (profondeur = 1) ──► On continue
         │
         ▼
  📤 Score chiffré → Banque

═══════════════════════════════════════════════════════════════════════
                    PHASE 3: BANQUE CLIENTE (Trusted Enclave)
═══════════════════════════════════════════════════════════════════════

  📥 Réception du score chiffré
         │
         ▼
  Déchiffrement: m' = c₀ + c₁ · sk  (mod q)
         │
         ▼
  Décodage: z' = m' / Δ
         │
         ▼
  Score final ≈ 1115.55  ──►  CRÉDIT ACCORDÉ ✅

---

## 📁 Project Structure
CKKS_Financial_Scoring/
│
├── bank_client/                    # 🏦 Trusted Banking Enclave
│   ├── __init__.py
│   ├── keygen.py                   # Key generation (sk, pk, evk)
│   ├── encrypt.py                  # Data encoding & RLWE encryption
│   ├── decrypt.py                  # Score decryption & decoding
│   └── bank_context_secret.txt     # 🔑 Secret context (sk) — NEVER leaves
│
├── fintech_cloud/                  # ☁️ Untrusted Cloud FinTech
│   ├── __init__.py
│   ├── ai_scoring_model.py         # AI model weights & bias
│   └── homomorphic_evaluation.py   # Blind inference on ciphertexts
│
├── shared_data/                    # 🔄 Encrypted data exchange zone
│   ├── cloud_context_public.txt    # Public context (pk, evk only)
│   ├── client_ciphertext.txt       # Encrypted client dossier
│   └── encrypted_score_result.txt  # Encrypted credit score
│
├── app.py                          # 🖥️ SOC Streamlit dashboard
├── Dockerfile                      # 🐳 Container configuration
├── requirements.txt                # 📦 Python dependencies
└── README.md                       # 📖 This file

---
## 👨‍💻 Author
**Mohammed KEHAL** |
**Zineb CHAFIK** |
**Ossama EL KHALFI**

*Project developed within the Master's program in Computer Engineering and Systems Security (2I2S).*
