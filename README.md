# GOTCHA – File Type Identification Tool 🛡️

GOTCHA is a Linux-based defensive cybersecurity tool that detects **disguised or suspicious files** by analyzing binary headers (magic numbers) instead of trusting file extensions.

## 🔍 Why GOTCHA?
Attackers often disguise malware by renaming executables as harmless files like `.jpg`, `.pdf`, or `.txt`. GOTCHA exposes the real file type and assigns a **risk-based status**.

## 🚀 Features
- Magic number (file signature) analysis
- File extension validation
- Linux `file` command integration
- Detects disguised executables
- Risk classification:
  - LOW (Safe)
  - MEDIUM (Misleading)
  - HIGH (Disguised Executable)
- Custom **GOTCHA ASCII banner**

## 🛠️ Tech Stack
- Python 3
- Kali Linux / Linux
- Magic numbers (file signatures)
- Linux `file` utility

## ▶️ How to Run
```bash
python3 file_type_identifier.py
# GOTCHA
