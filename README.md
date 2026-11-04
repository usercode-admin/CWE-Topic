CWE-Topic — E Corp Vulnerable Banking Lab

<p align="center">
<img src="https://raw.githubusercontent.com/usercode-admin/Background/main/ecorp_logo.png" width="180">
</p><p align="center">
<b>A deliberately vulnerable banking application for studying Common Weakness Enumeration (CWE), secure coding and penetration testing.</b>
</p><p align="center">"Python" (https://img.shields.io/badge/Python-3.x-blue)
"Flask" (https://img.shields.io/badge/Flask-Web%20Framework-black)
"SQLite" (https://img.shields.io/badge/Database-SQLite-blue)
"License" (https://img.shields.io/badge/Educational-Only-red)

</p>---

Overview

«A vulnerable banking application inspired by the fictional E Corp (Evil Corp) from Mr. Robot.»

The objective of this project is to provide an educational laboratory where developers and security learners can analyze insecure implementations, identify Common Weakness Enumeration (CWE) issues and practice defensive programming techniques.

This repository intentionally contains vulnerable code and must never be deployed in production environments.

---

Features

✓ Flask Backend
✓ SQLite Database
✓ Login & Registration
✓ User Profiles
✓ Admin Dashboard
✓ Account Management
✓ User Blocking
✓ User Deletion
✓ Infrastructure Dashboard
✓ Linux Telemetry API
✓ AJAX Username Checker
✓ localhost.run Tunnel
✓ Custom 403 & 404 Pages

---

Project Structure

corp_bank/
│
├── app.py
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
    └── js/
        └── main.js

---

Technology Stack

Component| Technology
Backend| Flask
Database| SQLite
Frontend| HTML5 • CSS3 • JavaScript
Library| jQuery 1.12
Language| Python 3
Tunnel| localhost.run SSH

---

Learning Objectives

The project demonstrates practical examples related to Common Weakness Enumeration (CWE).

Topics include:

- SQL Injection
- Broken Authentication
- Broken Access Control
- Information Disclosure
- Session Management
- Administrative Function Abuse
- Input Validation Issues

Learners are encouraged to identify vulnerabilities and implement secure alternatives.

---

Installation

git clone <repository>

cd CWE-Topic

pip install flask

python app.py

Application URL

http://127.0.0.1:5000

A public URL can also be generated automatically using localhost.run.

---

Default Accounts

Administrator

Username : administrator
Password : e_corp_master_key_2015

Demo User

Username : Elliot
Password : fsociety2015

---

Available Pages

Route| Description
/| Homepage
/login| Login Portal
/register| Registration
/profile| User Profile
/history| Corporate History
/infrastructure| Infrastructure Monitor
/admin| Administration Panel
/admin/info/<id>| User Audit
/403| Access Denied
/404| Not Found

---

Educational Notice

«This project intentionally contains insecure implementations for educational purposes.»

It is designed for:

- Security Training
- University Coursework
- Capture The Flag (CTF)
- Secure Coding Practice
- Penetration Testing Labs
- Vulnerability Research

---

Credits

Inspired by the television series Mr. Robot and its fictional corporation E Corp (Evil Corp).

Developed as an educational laboratory focused on Common Weakness Enumeration (CWE), web security and secure software development.
