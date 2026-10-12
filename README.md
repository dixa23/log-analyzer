# Security Log Analyzer

A Python script that reads server log files and flags IP addresses with repeated failed login attempts, which are possible brute-force attack sources.

## Features

- Counts failed login attempts per IP address
- Flags IPs with 3 or more failures (the threshold is configurable)
- Case-insensitive matching ("Failed login", "failed login")
- Extracts IP addresses with a regular expression
- Supports simple log lines and Linux `sshd`-style lines
- Accepts the log file path as a command-line argument
- Prints a clear message if the file is not found
- Sorts the report from most to least failed attempts

## Requirements

- Python 3
- No external libraries

## Usage

```
python log_analyzer.py server_logs.txt
```

If no file is given, the script reads `server_logs.txt` in the same folder.

### Supported log lines

```
192.168.1.10 Failed login
192.168.1.15 Successful login
Oct 11 10:32:01 server sshd[1234]: Failed password for root from 203.0.113.5 port 52111 ssh2
```

A line counts as a failure if it contains "failed login" or "failed password" and has an IPv4 address.

### Changing the threshold

Edit this line at the top of `log_analyzer.py`:

```python
THRESHOLD = 3
```

## Testing

### 1,000-line synthetic log

`generate_log.py` creates a synthetic 1,000-line log with 3 simulated attacker IPs and 20 normal IPs. A fixed random seed makes the file identical on every run.

```
python generate_log.py
python log_analyzer.py test_1000.log
```

Expected result: the 3 attacker IPs are flagged and none of the normal IPs.

Sample output:

```
Suspicious Activity Report

Possible brute force attack from 198.51.100.7 (23 failed attempts)
Possible brute force attack from 203.0.113.5 (18 failed attempts)
Possible brute force attack from 203.0.113.9 (15 failed attempts)
```

### sshd format test

`sshd_test.log` contains 3 Linux `sshd`-style failed-password lines from one IP:

```
python log_analyzer.py sshd_test.log
```

Expected result: `203.0.113.5` is flagged with 3 failed attempts.

The test data is synthetic and does not come from real traffic.

## Limitations

- The IP pattern does not validate addresses (for example, `999.1.1.1` would match)
- Only IPv4 addresses are supported, and only the first IP on each line is used
- Failures are counted over the whole file, with no time window
- It is a learning project and not a replacement for tools like fail2ban

## Possible improvements

- Validate IP addresses
- Add a time-window check (for example, N failures within 5 minutes)
- Support IPv6 and more log formats
- Export the report to a CSV file