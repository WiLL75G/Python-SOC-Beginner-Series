print("Welcome to SOC Python Basics")
print("This script will help me learn security automation")

# Simple SOC-style log simulation
logs = [
    "INFO User login from 192.168.1.10",
    "WARNING Failed login from 45.33.32.156",
    "INFO File accessed by user",
    "ALERT Suspicious activity from 102.89.45.12"
]

for log in logs:
    if "Failed" in log or "Suspicious" in log:
        print("⚠️ SOC ALERT:", log)
        
