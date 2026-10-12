import re
import sys
from collections import defaultdict

THRESHOLD = 3
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
FAILED_PATTERN = re.compile(r"failed (login|password)", re.IGNORECASE)

def analyze(log_file, threshold=THRESHOLD):
    failed = defaultdict(int)
    with open(log_file, "r") as f:
        for line in f:
            if FAILED_PATTERN.search(line):
                match = IP_PATTERN.search(line)
                if match:
                    failed[match.group()] += 1
    return {ip: n for ip, n in failed.items() if n >= threshold}

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "server_logs.txt"
    try:
        suspicious = analyze(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    print("Suspicious Activity Report\n")
    if not suspicious:
        print("No suspicious activity detected.")
    for ip, n in sorted(suspicious.items(), key=lambda x: -x[1]):
        print(f"Possible brute force attack from {ip} ({n} failed attempts)")