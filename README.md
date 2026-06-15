# Global Currency Converter

[![CI](https://github.com/shanni213/python-ci-simulation/actions/workflows/ci.yml/badge.svg)](https://github.com/shanni213/python-ci-simulation)

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

A high-performance currency conversion tool engineered for reliability and maintainability. This project demonstrates a production-grade development workflow, featuring automated CI/CD pipelines, strict static type analysis, and robust unit testing.

---

## 🎯 Functional Overview
When launched, the application opens a graphical web interface via Streamlit. Users can seamlessly convert currencies with the following built-in logic:
* **Supported Currencies:** USD, EUR, ILS, GBP, JPY, CAD, AUD, CHF, CNY, AED, and KRW.
* **Input Resilience:** Automatically sanitizes input by trimming spaces and handling case-insensitive currency codes (e.g., `ils`, `ILS`).
* **Localization:** Features a localized layout supporting Right-to-Left (RTL) alignment for Hebrew users.

---

## 🛠️ Engineering Highlights
* **Automated Quality Assurance:** A complete GitHub Actions CI pipeline that enforces strict linting, formatting, and type-safety on every commit.
* **High Test Coverage:** Core logic is thoroughly validated by a suite of 8+ edge-case unit tests with a mandatory coverage threshold.
* **Type-Safe Core Architecture:** Developed with comprehensive Python type hints to ensure code clarity and eliminate runtime type errors.

---

## 💻 Technical Stack
* **UI Framework:** Streamlit
* **Package Management:** `uv` (fast environment syncing)
* **Static Analysis:** `ruff` (Linter & Formatter)
* **Type Checking:** `ty`
* **Testing Framework:** `pytest` (with >80% coverage)
* **CI/CD:** GitHub Actions

---

## 📋 Requirements
* Python 3.12 or later

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/shanni213/python-ci-simulation.git
cd python-ci-simulation
```

### Setup environment
```bash
uv sync --dev
```

### Execute application
```bash
uv run streamlit run src/app.py
```

### Run quality suite
```bash
uv run ruff format --check .
uv run ruff check .
uv run ty check
uv run pytest
```
