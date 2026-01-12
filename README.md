<h1 align="center">🛡️ GOTCHA – File Type Identification Tool</h1>

<p align="center">
A Linux-based defensive cybersecurity tool to detect disguised or suspicious files using <b>magic number analysis</b>.
</p>

---

## 📌 Overview

<b>GOTCHA</b> is a Linux-based defensive cybersecurity tool that detects disguised or suspicious files by analyzing
<b>binary headers (magic numbers)</b> instead of trusting file extensions.

Attackers often rename malicious executables as harmless-looking files such as <code>.jpg</code>, <code>.pdf</code>,
or <code>.txt</code>.  
GOTCHA exposes the <b>real file type</b>, highlights mismatches, and assigns a <b>risk-based status</b> to help
prevent accidental execution.

---

## 🚀 Key Features

- 🔍 Magic number (file signature) analysis  
- 📁 File extension validation  
- 🐧 Linux <code>file</code> command integration  
- 🚨 Detects file masquerading attacks  
- ⚖️ Risk classification:
  - <b>LOW</b> – Safe file  
  - <b>MEDIUM</b> – Misleading file  
  - <b>HIGH</b> – Disguised executable  
- 🎨 Custom <b>GOTCHA ASCII banner</b> for branding  

---

## 🧠 Why GOTCHA?

File extensions <b>cannot be trusted</b>.

| File Name   | Real Type         | Risk   |
|------------|-------------------|--------|
| image.jpg  | ELF executable    | HIGH   |
| script.sh  | Binary executable | MEDIUM |
| notes.txt  | Plain text        | LOW    |

GOTCHA helps detect such threats <b>before execution</b>, supporting safer file handling.

---

## 🛠️ Tech Stack

<b>Language:</b> Python 3  
<b>Operating System:</b> Kali Linux / Linux  

<b>Core Concepts</b>
- Magic Numbers  
- File Signature Analysis  
- Malware Disguise Detection  

<b>Tools Used</b>
- Linux <code>file</code> utility  

---

## 📦 Installation & Usage

### 🔹 Prerequisites
- Linux (Kali Linux recommended)
- Python 3

Check Python version:
```bash
python3 --version

🔹 Step 1: Clone the Repository

git clone https://github.com/Samjithkp/GOTCHA.git

🔹 Step 2: Navigate to the Project Directory

cd GOTCHA

🔹 Step 3: Make the Script Executable (Optional)

chmod +x GOTCHA.py

🔹 Step 4: Run the Tool

python3 GOTCHA.py

🔹 One-Line Run Example

git clone https://github.com/Samjithkp/GOTCHA.git && cd GOTCHA && chmod +x GOTCHA.py && python3 GOTCHA.py

🧪 Example Output
🟢 Safe File

File: text.txt
Detected: Text File
Status: SAFE TEXT FILE
Risk Level: LOW

🔴 Disguised Executable

File: fake.jpg
Detected: ELF Executable
Status: DISGUISED EXECUTABLE
Risk Level: HIGH

🧑‍💼 Use Cases

    Malware analysis and triage

    SOC analyst file validation

    Digital forensics investigations

    Security awareness demonstrations

    Learning malware masquerading techniques

🎯 Learning Outcomes

    Understanding file masquerading attacks

    Practical use of magic numbers

    Defensive cybersecurity mindset

    Linux-based Python tooling

⚠️ Disclaimer

This tool is developed <b>strictly for educational and defensive security purposes</b>.
Do <b>not</b> use it for malicious activities.
📌 Future Enhancements

    Folder / bulk file scanning

    Color-coded status output

    Logging scan results to file

    YARA rule integration

    GUI version

👤 Author

<b>Samjith K P</b>
Cyber Security Enthusiast | Malware Analysis | SOC | Pentesting
🔗 LinkedIn: https://www.linkedin.com/in/samjith-k-p
⭐ Support

If you find this project useful, consider giving it a ⭐ <b>star</b> on GitHub!
