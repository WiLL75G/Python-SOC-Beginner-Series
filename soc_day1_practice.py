# -------------------------------
# Beginner SOC Python Practice
# -------------------------------

# Sample logs
logs = [
    "INFO User: Alice logged in from 192.168.1.10",
    "WARNING User: Bob failed login from 45.33.32.156",
    "ALERT User: Eve attempted unauthorized access from 102.89.45.12",
    "INFO User: Charlie viewed file",
    "WARNING Disk space low on server",
    "ALERT Malware detected in system"
]

# List of suspicious users
suspicious_users = ["Eve", "Mallory"]

# Counter for alerts
alert_count = 0

print("\n=== SOC Daily Log Analysis ===\n")

# Process each log
for log in logs:
    # Count alerts
    if "ALERT" in log or "WARNING" in log:
        alert_count += 1

    # Check for suspicious users
    user_flagged = False
    for user in suspicious_users:
        if user in log:
            user_flagged = True
            print(f"🚨 Suspicious user detected: {user} | Log: {log}")

    # Classify severity
    if "ALERT" in log:
        severity = "HIGH"
    elif "WARNING" in log:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # Print log with severity if not flagged already
    if not user_flagged:
        print(f"Log: {log} | Severity: {severity}")

# Summary
print("\n=== Summary ===")
print(f"Total alerts detected: {alert_count}")
print(f"Suspicious users flagged today: {', '.join(suspicious_users)}")
