# 🛡️ GOTCHA – File Type Identification Tool

A Linux-based defensive cybersecurity tool that detects disguised or suspicious files using **magic number analysis** instead of trusting file extensions.

---

## 📌 Overview

**GOTCHA** detects files that are disguised as harmless formats (such as `.jpg`, `.pdf`, or `.txt`) by analyzing **binary headers (magic numbers)**.

Attackers often rename malicious executables to trick users.  
GOTCHA exposes the **real file type**, highlights mismatches, and assigns a **risk-based status** to help prevent accidental execution.

---

## 🚀 Key Features

- 🔍 Magic number (file signature) analysis  
- 📁 File extension validation  
- 🐧 Linux `file` command integration  
- 🚨 Detects file masquerading attacks  
- ⚖️ Risk classification:
  - **LOW** – Safe file  
  - **MEDIUM** – Misleading file  
  - **HIGH** – Disguised executable  
- 🎨 Custom **GOTCHA ASCII banner**

---

## 🧠 Why GOTCHA?

File extensions **cannot be trusted**.

| File Name  | Real Type         | Risk   |
|-----------|-------------------|--------|
| image.jpg | ELF executable    | HIGH   |
| script.sh | Binary executable | MEDIUM |
| notes.txt | Plain text        | LOW    |

GOTCHA helps detect such threats **before execution**, supporting safer file handling.

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Operating System:** Kali Linux / Linux  

### Core Concepts
- Magic Numbers  
- File Signature Analysis  
- Malware Disguise Detection  

### Tools Used
- Linux `file` utility  

---

## 📦 Installation & Usage

### 🔹 Prerequisites
- Linux (Kali Linux recommended)
- Python 3

Check Python version:

```bash
python3 --version
```

📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Samjithkp/GOTCHA.git

# Navigate to the project directory
cd GOTCHA

# Make the script executable (optional)
chmod +x GOTCHA.py

# Run the tool
python3 GOTCHA.py
```

📦 One-Line Run Example

```bash
git clone https://github.com/Samjithkp/GOTCHA.git && cd GOTCHA && chmod +x GOTCHA.py && python3 GOTCHA.py
```

<br><br>
## 🧪 Example Output
### 🟢 Safe File

```bash
File: text.txt
Detected: Text File
Status: SAFE TEXT FILE
Risk Level: LOW
```

🔴 Disguised Executable

```bash
File: fake.jpg
Detected: ELF Executable
Status: DISGUISED EXECUTABLE
Risk Level: HIGH
```
<br>



## 🧑‍💼 Use Cases

- Malware analysis and triage  
- SOC analyst file validation  
- Digital forensics investigations  
- Security awareness demonstrations  
- Learning malware masquerading techniques  

---

## 🎯 Learning Outcomes

- Understanding file masquerading attacks  
- Practical use of magic numbers  
- Defensive cybersecurity mindset  
- Linux-based Python tooling  

---

## ⚠️ Disclaimer

This tool is developed strictly for **educational and defensive security purposes**.  
Do **not** use it for malicious activities.

---

## 🚀 Future Enhancements

- Folder / bulk file scanning  
- Color-coded status output  
- Logging scan results to file  
- YARA rule integration  
- GUI version  

---

## 👤 Author

**Samjith K P**  
Cyber Security Enthusiast 
🔗 LinkedIn: https://www.linkedin.com/in/samjith-k-p  

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ **star** on GitHub!
