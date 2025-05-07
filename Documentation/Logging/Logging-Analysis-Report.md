# Logging Implementation and Analysis Report

## Objective

Implement a robust logging system to track all authentication attempts on the IoT device, including both successful and failed logins. This aids in identifying potential threats like brute-force attacks or unauthorized access, and supports compliance with best security practices. Logging also enables integration with real-time alerting systems and SIEM platforms for advanced monitoring, while providing a historical record for audits and forensic investigations.  


## Enable Logging of Login Attempts

### Implementation:
Logging was enabled on the Flask-based IoT camera system to record all authentication activity. The following fields are captured per attempt:

- Timestamp of login attempt
- Source IP address
- Device ID (Raspberry Pi identifier)
- Username entered
- Result (Success or Failure)

**Testing Log Entry:**
- Jaime's computer attempts to logon 192.168.1.171:5000/camera (3) attempts failed to logon.


### Summary:
- Logging captures both success and failure states.
- Repeated failed attempts are visible in logs.
- Logs are written to a file (`auth.log`) and stored locally on the Pi for 30 days.

---

## Log Analysis 

### Findings:
- **Last 4 Authentication Logs** reviewed.
- **3 failed attempts** followed by **1 successful login** from IP `192.168.1.171` (user: Jaime).
- **No suspicious activity** detected beyond repeated login attempts from a familiar IP.

### Summary:
- No unusual IPs or unknown devices detected.
- No alerts triggered during the review window.
- System is logging and functioning correctly.

---

## MFA Implementation and Test Results

### MFA Implementation Overview:
The IoT system uses **Google Authenticator-based Time-Based One-Time Passwords (TOTP)** to secure camera access. The Flask app requires both username/password and a 6-digit TOTP code to authenticate users.

### Event Logging:
All authentication attempts are recorded, capturing:

- Timestamps  
- Success/failure results  
- IP addresses  
- Associated device ID  
- Username

### Real-Time Alerting:
The system generates alerts for:

- Multiple failed login attempts in a short window (to detect brute-force attempts).
- Login attempts from new or unknown IP addresses.
- Repeated failures triggering account lockout after 5 attempts.

### Dashboard and Visibility:
A monitoring dashboard is available that visualizes:

- Authentication trends
- Active users
- Failed login heatmaps
- Alerts and anomalies

### Log Retention and Searchability:
- Logs retained locally for **30 days**.
- Searchable by **username, IP, device, and date range**.

### SIEM Integration (Optional/Future):
- Authentication logs can be exported in JSON or syslog format for use in external platforms such as **Splunk**, **ELK Stack**, or **Microsoft Sentinel**.

---

## Conclusion

Logging and monitoring features were successfully implemented and tested. Logs provide visibility into user behavior and support both manual and automated alerting. No suspicious activity was found during the latest audit. The system is ready for integration with SIEM tools and supports further scalability.
