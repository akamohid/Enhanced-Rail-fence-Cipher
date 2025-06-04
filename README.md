# Enhanced Rail Fence Cipher (ERFC)

![ERFC Logo](https://img.shields.io/badge/emoji--based--crypto-purple?style=for-the-badge)

An **emoji‑driven substitution + transposition cipher** that builds on the classical Rail‑Fence cipher.  
ERFC balances **moderate security**, **fun UX**, and **zero external dependencies**.

---

## ✨ Key Features
- **62‑emoji substitution table** keyed by SHA‑256 of your secret.
- **Randomised matrix (“big grid”)** placement for strong diffusion.
- **Salt with encrypted length** to hide message size.
- **SHA‑256 integrity hash** shipped with each ciphertext.
- **Pure‑Python implementation** (`src/erfc.py`), Python ≥ 3.8.
- Academic paper included (`docs/ERFC_paper.pdf`).

---

## 📂 Repository Layout

```
ERFC_repo/
├── docs/               # Research paper & diagrams
│   └── ERFC_paper.pdf
├── src/                # Production source code
│   └── erfc.py
├── tests/              # Simple round‑trip unit test
│   └── test_erfc.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── CITATION.cff
```

---

## 🚀 Quick Start

```bash
# Clone or download the repo
git clone <your‑fork‑url>
cd ERFC_repo

# (Optional) create a venv
python -m venv .venv && source .venv/bin/activate

# Install requirements (stdlib‑only, so nothing to install)
pip install -r requirements.txt

# Encrypt
python src/erfc.py
# Follow the CLI prompts…

# Run tests
python tests/test_erfc.py
```

---

## 🛠️ Library Usage

```python
from src.erfc import encrypt, decrypt

ciphertext, msg_hash = encrypt("Hello123", "mySecretKey")
plaintext = decrypt(ciphertext, "mySecretKey", msg_hash)
assert plaintext == "Hello123"
```

---

## 🔐 Security Notes
ERFC is **not** a substitute for AES/RSA in high‑stakes settings.  
It *is* suitable for pedagogy, casual messaging, CTF puzzles, or games where moderate secrecy & emoji aesthetics are desirable.

See **Section VI** of the paper for detailed analysis.

---

## 🤝 Contributing
Bug reports, feature ideas, and pull requests are welcome!  
Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before diving in.

---

## 📜 License
Distributed under the MIT License – see [`LICENSE`](LICENSE) for details.

---

## 📝 Citation
If you use ERFC in academic work, please cite using the `CITATION.cff` provided.