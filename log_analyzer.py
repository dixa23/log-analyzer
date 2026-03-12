from collections import defaultdict

log_file = "server_logs.txt"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            ip = line.split()[0]
            failed_attempts[ip] += 1

print("Suspicious Activity Report\n")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"Possible brute force attack from {ip} ({count} failed attempts)")