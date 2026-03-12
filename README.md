# Security Log Analyzer

A Python-based security tool designed to analyze server log files and detect suspicious login activity.
The program scans log entries to identify repeated failed login attempts from the same IP address, which may indicate a potential brute-force attack.

## Features

* Analyzes server log files for failed login attempts
* Detects suspicious IP addresses based on repeated failures
* Identifies possible brute-force attack patterns
* Generates a simple security activity report

## Technologies Used

* Python
* Log File Analysis
* Basic Threat Detection Techniques

## Project Structure

log-analyzer
│
├── log_analyzer.py
└── server_logs.txt

## How to Run

1. Make sure Python is installed on your system.

2. Run the program:

python log_analyzer.py

3. The program will analyze the log file and display suspicious activity detected from specific IP addresses.

## Example Log File

Example content of `server_logs.txt`:

192.168.1.10 Failed login
192.168.1.10 Failed login
192.168.1.10 Failed login
192.168.1.12 Failed login
192.168.1.12 Failed login
192.168.1.12 Failed login

## Example Output

Suspicious Activity Report

Possible brute force attack from 192.168.1.10 (3 failed attempts)
Possible brute force attack from 192.168.1.12 (3 failed attempts)

## Project Purpose

This project demonstrates how security analysts can analyze authentication logs to detect suspicious behavior and potential brute-force attacks.
It highlights the importance of monitoring login activity to improve system security.

## Author

Diksha Patil
