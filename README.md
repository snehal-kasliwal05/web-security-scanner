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

## Django and Flask Relevance

This scanner can be used to assess applications built with Django and Flask by:

- Testing form input handling and validation logic  
- Identifying improper use of templating that may lead to XSS  
- Verifying security headers configured at the framework or server level  
- Analyzing session and cookie security configurations  

Although Django provides built-in protections like auto-escaping and CSRF protection, and Flask allows flexible security configurations, misconfigurations can still introduce vulnerabilities. This tool helps identify such gaps.

---

## Tech Stack

- Python  
- Requests  
- BeautifulSoup  
- Regular Expressions  

---

## Project Structure
```
web-security-scanner/
├── scanner/
├── demo/
├── notebooks/
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
* Apply OWASP Top 10 concepts in practice

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not use it on systems without proper permission.

---

## Author

Snehal Kasliwal
Cybersecurity Enthusiast
