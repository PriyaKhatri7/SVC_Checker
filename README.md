# SVC_Checker

**SVC Checker** is a lightweight Python automation script that performs health checks on one or more service endpoints (URLs) and reports their status.  
It’s perfect for simple uptime monitoring or integration into CI/CD pipelines.

---

## Features
- Sends HTTP GET requests to multiple URLs  
- Retries with exponential backoff for resilience  
- Logs results to console and `run.log`  
- Comes with automated `pytest` test suite  
- Fully integrated with GitHub Actions (Continuous Integration)

---

## Project Structure
```text
svc-checker/
│
├── main.py                # Main health check script
├── tests/                 # Test cases
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt       # Dependencies
├── pytest.ini             # Test configuration
├── .github/
│   └── workflows/
│       ├── ci.yml         # Continuous Integration workflow
│       └── scheduled.yml  # Scheduled health check workflow
│
├── .gitignore             # Ignore rules
└── README.md              # You are here :)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyaKhatri7/SVC_Checker.git
   cd SVC_Checker

2. Create a virtual environment: 
   ```bash
    python -m venv .venv
    .venv\Scripts\activate`      # Windows
    or
    `source .venv/bin/activate`   # macOS/Linux ```

3. Install dependencies: 
   ```bash
   python -m pip install -r requirements.txt ```

---

## Run the script manually
   `python main.py --urls="https://example.com,https://api.github.com"`


### Optional arguments: 
| Flag         | Description                           | Default    |
| ------------ | ------------------------------------- | ---------- |
| `--urls`     | Comma-separated list of URLs to check | *Required* |
| `--timeout`  | Timeout (seconds) for each request    | `5`        |
| `--attempts` | Number of retry attempts              | `3`        |

Logs will be saved to run.log and printed to the console.

---

## Continuous Integration (CI)
This project uses GitHub Actions to automatically:
- Install dependencies
- Run pytest
- Upload test results as an artifact

You can find the workflow file at:
```.github/workflows/ci.yml```

## Badges 
[![CI](https://github.com/PriyaKhatri7/SVC_Checker/actions/workflows/ci.yml/badge.svg)](https://github.com/PriyaKhatri7/SVC_Checker/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/build-passing-brightgreen)

# Future Improvements
 - Add parallel requests for faster checks
 - Send Slack/email alerts for failed endpoints
 - Add configurable JSON/YAML input for URLs
 -  Dockerize for deployment
