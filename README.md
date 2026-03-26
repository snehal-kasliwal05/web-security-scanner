# Web Security Scanner (XSS-Focused)

A Python-based web application security scanner designed to identify common vulnerabilities, with a primary focus on Cross-Site Scripting (XSS), input validation weaknesses, and security misconfigurations. The tool is designed for educational use and can be applied to test applications built using frameworks like Django and Flask.

---

## Overview

This project implements multiple security analysis mechanisms to evaluate the defensive posture of web applications. It combines static and dynamic analysis techniques to identify vulnerabilities related to XSS, insecure headers, weak cookie configurations, and improper input validation.

The scanner is framework-agnostic and can be used to analyze applications developed using Django, Flask, or any standard web stack.

---

## Features

### Content Security Policy (CSP) Analysis
- Detects missing or weak CSP configurations  
- Identifies unsafe directives that may allow script injection  

### Cookie Security Assessment
- Checks for secure cookie attributes:
  - HttpOnly  
  - Secure flag  
  - SameSite policy  

### Security Headers Evaluation
- Verifies the presence of important headers:
  - X-Frame-Options  
  - X-Content-Type-Options  
  - Strict-Transport-Security  
- Highlights missing or misconfigured headers  

### Input Validation Testing
- Passive analysis of form inputs and constraints  
- Active testing using payload injection  
- Detects:
  - Lack of validation  
  - Weak pattern-based filtering  
  - Improper length restrictions  

### DOM-Based XSS Detection
- Identifies dangerous JavaScript sinks such as:
  - innerHTML  
  - eval()  
- Tracks untrusted sources including:
  - URL parameters  
  - document.cookie  
  - local storage  

---

## Django and Flask Test Applications

This project includes lightweight test applications built using Django and Flask to simulate real-world XSS-related scenarios.

### Django Test App
The Django test application includes:
- safe and vulnerable template rendering examples
- input handling for XSS testing
- practical scenarios for validating scanner behavior

### Flask Test App
The Flask test application includes:
- a vulnerable route for unsafe input rendering
- a safer route for comparison
- simple test cases to observe XSS-related behavior

These applications were used to validate scanner results and understand how vulnerabilities manifest across different frameworks.

---

## Tech Stack

- Python  
- Requests  
- BeautifulSoup  
- Regular Expressions
- Django
- Flask

---

## Project Structure
```
web-security-scanner/
├── scanner/
├── demo/
├── notebooks/
├── test-apps/
│   ├── flask_app/
│   └── django_app/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/snehal-kasliwal05/web-security-scanner.git
cd web-security-scanner
pip install -r requirements.txt
```
## Usage

```bash
python main.py
```

## Demo

Sample output screenshots are available in the `demo/` folder.

---

## Learning Outcomes

* Understand how XSS vulnerabilities occur in real-world applications
* Explore how input validation impacts application security
* Analyze the role of security headers and CSP
* Study DOM-based XSS patterns and detection techniques
* Build simple Django and Flask applications for security testing
* Apply OWASP Top 10 concepts in practice
---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not use it on systems without proper permission.

---

## Author

Snehal Kasliwal
Cybersecurity Enthusiast
