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
svc-checker/
│
├── main.py              # Main healthcheck script
├── tests/               # Test files for pytest
├── requirements.txt     # Dependencies
├── pytest.ini           # Pytest config
├── .github/workflows/   # GitHub Actions CI workflows
├── .gitignore           # Ignored files/folders
└── README.md            # You are here :)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyaKhatri7/SVC_Checker.git
   cd SVC_Checker

2. Create a virtual environemnt 
  ```bash
  python -m venv .venv
.venv\Scripts\activate`      # Windows
 or
`source .venv/bin/activate`   # macOS/Linux

--- 

3. Install dependencies 
`python -m pip install -r requirements.txt`

---

## Run the script manually:
`python main.py --urls="https://example.com,https://api.github.com"`


### Optional arguments: 
| Flag         | Description                           | Default    |
| ------------ | ------------------------------------- | ---------- |
| `--urls`     | Comma-separated list of URLs to check | *Required* |
| `--timeout`  | Timeout (seconds) for each request    | `5`        |
| `--attempts` | Number of retry attempts              | `3`        |

Logs will be saved to run.log and printed to the console.

## Continuous Integration (CI)
This project uses GitHub Actions to automatically:
- Install dependencies
- Run pytest
- Upload test results as an artifact

You can find the workflow file at:
```.github/workflows/ci.yml```


CI Status Badge:

# Future Improvements
 - Add parallel requests for faster checks
 - Send Slack/email alerts for failed endpoints
 - Add configurable JSON/YAML input for URLs
 -  Dockerize for deployment
