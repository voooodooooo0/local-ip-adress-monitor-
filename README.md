# 🖧 Network Device Scanner & Monitor

A Python-based tool to scan a local network, identify active devices, estimate their data usage, and categorize them as **Phones**, **Computers**, or **Other**.

## 🔍 Features

- Fast subnet scan using `nmap`
- OS detection and classification
- Estimates bandwidth/data usage via SNMP
- Categorizes devices intelligently
- Buildable to `.exe` using PyInstaller

## 🛠 Requirements

- Python 3.8+
- Nmap (installed and added to PATH)
- SNMP-enabled devices (for usage monitoring)

## 📦 Installation

```bash
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
