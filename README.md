# SOC Log Monitoring & Threat Analysis

## 📌 Overview
This project simulates a **Security Operations Center (SOC)** workflow by analyzing authentication logs to detect suspicious activities such as brute-force login attempts and potential unauthorized access.

It demonstrates how SOC analysts monitor logs, classify incidents, and identify high-risk IP addresses.

---

## 🎯 Objectives
- Detect failed login attempts from system logs
- Identify suspicious IP addresses based on repeated failures
- Assist in incident severity classification
- Practice SOC reporting standards

---

## 🛠️ Tools & Technologies
- Python
- Linux Authentication Logs
- Regular Expressions (Regex)
- SOC Concepts (SIEM-style analysis)

---

## 🧠 Key Learnings
- Log analysis fundamentals
- Incident triage workflow
- SOC alert identification
- Python automation for security

---

## 📂 Project Structure
SOC-Log-Monitoring-and-Threat-Analysis/
│
├── logs/
│   └── sample_auth.log
│
├── scripts/
│   └── log_analyzer.py
│
├── reports/
│   └── incident_report.txt
│
└──  README.md


---

## ⚙️ How It Works
- Parses authentication logs
- Extracts failed login attempts
- Counts repeated attempts per IP
- Flags IPs exceeding a defined threshold

---

## ▶️ How to Run
```bash
cd scripts
python log_analyzer.py
