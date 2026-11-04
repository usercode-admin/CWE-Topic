<div align="center">

# CWE-Topic
### E Corp Vulnerable Banking Laboratory

<img src="https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png" width="180">

A deliberately vulnerable banking application built for learning **Common Weakness Enumeration (CWE)**, **Web Security**, **Secure Coding** and **Penetration Testing**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge)
![Educational](https://img.shields.io/badge/Purpose-Educational-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# Table of Contents

- Overview
- Features
- Screenshots
- Project Structure
- Technology Stack
- Learning Objectives
- Vulnerabilities
- Installation
- Default Accounts
- Available Pages
- Disclaimer
- Credits

---

# Overview

CWE-Topic is an educational vulnerable banking laboratory inspired by the fictional **E Corp (Evil Corp)** from the television series **Mr. Robot**.

Unlike a normal banking demo, this project intentionally contains insecure implementations so learners can discover vulnerabilities, understand why they exist, and practice securing them.

This repository is designed for:

- Cybersecurity Students
- Secure Coding Courses
- Web Penetration Testing
- Capture The Flag (CTF)
- University Labs
- Self-learning

---

# Features

| Module | Status |
|---------|:-----:|
| Landing Page | ✔ |
| Login System | ✔ |
| Registration | ✔ |
| User Profile | ✔ |
| Admin Dashboard | ✔ |
| User Management | ✔ |
| User Blocking | ✔ |
| User Deletion | ✔ |
| AJAX Username Validation | ✔ |
| Infrastructure Dashboard | ✔ |
| Linux System Monitor | ✔ |
| SQLite Database | ✔ |
| SSH Tunnel | ✔ |
| Custom Error Pages | ✔ |

---

# Screenshots

> Add screenshots here

```
Home Page

Login Page

Admin Dashboard

Infrastructure

Profile

403 / 404
```

---

# Project Structure

```text
CWE-Topic/
│
├── app.py
├── requirements.txt
├── mysql.sql
├── database.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── history.html
│   ├── infrastructure.html
│   ├── admin.html
│   ├── admin_info.html
│   ├── 403.html
│   └── 404.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask |
| Database | SQLite |
| Frontend | HTML5 |
| Styling | CSS3 |
| Client-side | JavaScript |
| Library | jQuery 1.12 |
| Language | Python 3 |
| Tunnel | localhost.run |

---

# Learning Objectives

This project demonstrates practical examples related to **Common Weakness Enumeration (CWE)**.

Learners can study topics including:

- SQL Injection
- Broken Authentication
- Broken Access Control
- Information Disclosure
- Session Management
- Input Validation
- Authorization Issues
- Administrative Abuse
- Information Leakage

---

# Vulnerabilities Included

| CWE | Description |
|------|-------------|
| CWE-89 | SQL Injection |
| CWE-200 | Information Exposure |
| CWE-285 | Improper Authorization |
| CWE-306 | Missing Authentication |
| CWE-20 | Improper Input Validation |
| CWE-522 | Insufficient Credential Protection |

---

# Installation

```bash
git clone https://github.com/USERNAME/CWE-Topic.git

cd CWE-Topic

pip install -r requirements.txt

python app.py
```

Server

```
http://127.0.0.1:5000
```

A public URL can also be generated automatically using **localhost.run**.

---

# Default Accounts

Administrator

```text
Username : administrator
Password : e_corp_master_key_2015
```

Demo User

```text
Username : Elliot
Password : fsociety2015
```

---

# Available Pages

| Route | Description |
|-------|-------------|
| / | Homepage |
| /login | Authentication |
| /register | Registration |
| /profile | User Profile |
| /history | Company History |
| /infrastructure | Infrastructure Dashboard |
| /admin | Admin Dashboard |
| /admin/info/<id> | User Information |
| /403 | Access Denied |
| /404 | Not Found |

---

# Educational Notice

> [!WARNING]
>
> This application intentionally contains insecure implementations.
>
> Do **NOT** deploy this project in production.
>
> It is intended exclusively for:
>
> - Security Research
> - Secure Coding
> - Cybersecurity Training
> - University Coursework
> - Capture The Flag
> - Demonstrations

---

# Future Improvements

- Docker Support
- REST API
- JWT Authentication
- Password Hashing
- Role-Based Access Control
- Logging Dashboard
- Security Hardening
- Unit Testing

---

# Credits

Inspired by:

- **Mr. Robot**
- **E Corp (Evil Corp)**

Developed as an educational laboratory for studying **Common Weakness Enumeration (CWE)**, **Web Application Security**, **Secure Coding**, and **Penetration Testing**.

---

<div align="center">

Made with 👀 for Cyber Security Education

</div>
