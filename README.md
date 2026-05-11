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

```mermaid
flowchart TD

    %% =========================
    %% PHASE 1: BANK
    %% =========================
    subgraph P1["🏦 PHASE 1: BANK (Trusted Enclave)"]
        A["Raw Data z"]
        B["Encode with Δ"]
        C["Message m ∈ R_q"]
        D["RLWE Encryption"]
        E["Ciphertext (c₀, c₁)"]

        A --> B
        B --> C
        C --> D
        D --> E
    end

    %% =========================
    %% PHASE 2: CLOUD
    %% =========================
    subgraph P2["☁️ PHASE 2: CLOUD (Zero-Trust)"]
        F["Cloud FinTech"]
        G["HE Evaluation"]
        H["Encrypted Score"]

        F --> G
        G --> H
    end

    %% =========================
    %% PHASE 3: BANK
    %% =========================
    subgraph P3["🏦 PHASE 3: BANK (Trusted Enclave)"]
        I["Decrypt"]
        J["Decode"]
        K["Final Score ≈ 1115.55"]
        L["CREDIT APPROVED"]

        I --> J
        J --> K
        K --> L
    end

    %% =========================
    %% CROSS-PHASE FLOWS
    %% =========================
    E -->|"pk, evk, c"| F
    H -->|"Return"| I
```
```bash
=======================================================================
                   PHASE 1: BANQUE CLIENTE (Trusted Enclave)
=======================================================================

  Raw Data z in R^(N/2)
  [4500.0, 1200.5, 710.0, 34.0]
         |
         v
  Encoding: Delta = 2^40  -->  Polynomial m in R_q
         |
         v
  RLWE Encryption  -->  c = (c0, c1)

  [KEY] sk (kept local)  |  [OUT] pk, evk, c --> Cloud

=======================================================================
                   PHASE 2: CLOUD FINTECH (Zero-Trust)
=======================================================================

  [IN] Receive pk, evk, c
         |
         v
  AI Model: W = [0.4, -0.7, 0.2, 0.1], Bias = +10.5
         |
         v
  HE Evaluation: c_res = c * W + Bias
  (Add, Mult, Relinearize, Rescale)
         |
         v
  Noise critical? --> No (depth = 1) --> Continue
         |
         v
  [OUT] Encrypted score --> Bank

=======================================================================
                   PHASE 3: BANQUE CLIENTE (Trusted Enclave)
=======================================================================

  [IN] Receive encrypted score
         |
         v
  Decrypt: m' = c0 + c1 * sk  (mod q)
         |
         v
  Decode: z' = m' / Delta
         |
         v
  Final Score ~ 1115.55  -->  CREDIT APPROVED ✓
```
---

## 📁 Project Structure

```text
CKKS_Financial_Scoring/
│
├── bank_client/                    # Trusted Banking Enclave
│   ├── __init__.py
│   ├── keygen.py                   # Key generation (sk, pk, evk)
│   ├── encrypt.py                  # Data encoding & RLWE encryption
│   ├── decrypt.py                  # Score decryption & decoding
│   └── bank_context_secret.txt     # Secret context (sk) - NEVER leaves
│
├── fintech_cloud/                  # Untrusted Cloud FinTech
│   ├── __init__.py
│   ├── ai_scoring_model.py         # AI model weights & bias
│   └── homomorphic_evaluation.py   # Blind inference on ciphertexts
│
├── shared_data/                    # Encrypted data exchange zone
│   ├── cloud_context_public.txt    # Public context (pk, evk only)
│   ├── client_ciphertext.txt       # Encrypted client dossier
│   └── encrypted_score_result.txt  # Encrypted credit score
│
├── app.py                          # SOC Streamlit dashboard
├── Dockerfile                      # Container configuration
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---
## 🚀 Quick Start

### Prerequisites

- **Docker** installed ([Get Docker](https://docs.docker.com/get-docker/))
- **Git** installed ([Get Git](https://git-scm.com/))

### Option 1: Docker (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/CKKS_Financial_Scoring.git
cd CKKS_Financial_Scoring

# 2. Build the Docker image
docker build -t ckks-finance .

# 3. Run the container
docker run -it -p 8501:8501 -v ${PWD}:/app ckks-finance

# 4. Inside the container, launch the SOC dashboard
streamlit run app.py --server.address=0.0.0.0

# 5. Open your browser
# Local URL: http://localhost:8501
```
### Option 2: Manual Installation

```bash
# 1. Clone the repository
git clone https://github.com/mohammedkehal/Projet_Crypto_FHE_CKKS.git
cd Projet_Crypto_FHE_CKKS

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the SOC dashboard
streamlit run app.py
```
## 👨‍💻 Author
**Mohammed KEHAL** |
**Zineb CHAFIK** |
**Ossama EL KHALFI**

*Project developed within the Master's program in Computer Engineering and Systems Security (2I2S).*
