# CodeAlpha Task 3 – Secure Coding Review

**Prepared by:** Agha Ahmad Khan

## Overview
A small Python Flask web application was manually reviewed for common
secure-coding weaknesses, supported by static analysis using **Bandit**.
The reviewed app intentionally contains 8 vulnerability patterns so they
could be identified, rated by severity, and documented with remediation.

## Files
- `vulnerable_app.py` – intentionally vulnerable sample application
- `setup_db.py` – helper script to initialize the test database
- `Secure_Coding_Review_Task3.docx` – full findings and remediation report
- `bandit_output.png` – static analyzer results (Bandit scan)

## Method
- Manual line-by-line code review
- Static analysis with Bandit (`pip install bandit && bandit vulnerable_app.py`)

## Findings

| # | Issue | Severity |
|---|-------|----------|
| 1 | SQL Injection (login route) | Critical |
| 2 | Command Injection (`/ping` route, `shell=True`) | Critical |
| 3 | Path Traversal (`/download` route) | High |
| 4 | Reflected XSS (`/search` route) | High |
| 5 | Hardcoded secrets (`secret_key`, DB password) | High |
| 6 | Insecure session cookie (missing HttpOnly/Secure/SameSite) | Medium |
| 7 | Debug mode enabled in production (`debug=True`) | Medium |
| 8 | Unauthenticated debug endpoint (`/debug`) | Low |

Full details, root causes, and specific remediation steps for each finding
are in `Secure_Coding_Review_Task3.docx`.

## Key Recommendations
- Use parameterized queries instead of string-built SQL
- Avoid `shell=True`; pass subprocess arguments as a list
- Validate and sanitize all file paths and user input
- Load secrets from environment variables, never hardcode them
- Use Jinja2 autoescaping instead of building HTML with f-strings
- Set `HttpOnly`, `Secure`, and `SameSite` flags on session cookies
- Disable debug mode and use a production WSGI server before deployment

> **Note:** `vulnerable_app.py` is for educational review only and must
> never be deployed as-is.