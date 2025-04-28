# 🔒 Vulnerability Scanner

A simple Python-based vulnerability scanner that scans a target for open ports and performs basic banner grabbing.

## 📌 Features
- Port scanning (common ports)
- Banner grabbing (detects service information)
- Timeout handling for faster scans
- Clean and simple CLI


## 🛠️ Built With
- Python 3
- Socket library (built-in)

## 📦 Requirements
Install Python packages (if any):
```bash
pip install -r requirements.txt

 ## Example

```bash
python scanner.py --target example.com --start-port 20 --end-port 100

After the scan, a report is automatically saved to a file named `scan_report.txt`.
