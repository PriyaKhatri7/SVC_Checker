import argparse, logging, os, sys, time
import requests

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("run.log")]
    )

def check(url, timeout=5, attempts=3, backoff=1.5):
    last_exc = None
    for i in range(attempts):
        try:
            r = requests.get(url, timeout=timeout)
            return r.status_code, r.text
        except Exception as e:
            last_exc = e
            time.sleep(backoff ** (i+1))
    raise last_exc

def parse_args():
    p = argparse.ArgumentParser(description="healthcheck script")
    p.add_argument("--urls", required=True, help="comma-seperated URLs")
    p.add_argument("--timeout", type=int, default=5)
    p.add_argument("--attempts", type=int, default=3)
    return p.parse_args()

def main():
    setup_logger()
    args = parse_args()
    urls = [u.strip() for u in args.urls.split(",") if u.strip()]
    failures = []
    for u in urls:
        try:
            code, _ = check(u, timeout=args.timeout, attempts=args.attempts)
            logging.info(f"{u} -> {code}")
            if code >= 400:
                failures.append((u, code))
        except Exception as e:
            logging.error(f"{u} failed: {e}")
            failures.append((u, "EXC"))
    if failures:
        logging.error(f"Failures: {failures}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
