# Integration Testing Results

## Overview
During Milestone 2, we completed integration of Multi-Factor Authentication (MFA) using Google Authenticator within our Flask-based login system. After completing the integration, we ran a series of tests to confirm that the system behaved as expected and blocked common attack methods.

## Testing Summary

### Brute Force Attack
- **Objective:** Simulate repeated login attempts using incorrect credentials.
- **Result:** System displayed a lockout message after five failed attempts.
- **Conclusion:** Brute force protection was effective, and retry limits worked as intended.

###  Replay Attack
- **Objective:** Reuse a previously valid MFA token after it had expired.
- **Result:** System responded with an “invalid code” message and denied access.
- **Conclusion:** Tokens expired properly and could not be reused, confirming secure token handling.

###  Cross-Device Compatibility
- **Objective:** Ensure that the web interface and authentication system worked on multiple types of devices.
- **Tested Devices:** Laptop (Windows/macOS), Mobile phone (iOS/Android)
- **Result:** No layout or functionality issues. QR code pairing, login, and camera display worked on all tested devices.
- **Conclusion:** The environment was accessible and usable across platforms, supporting both desktop and mobile users.

## Summary
All tests confirmed that our MFA integration was secure and functioning as designed. The system effectively blocked brute force and replay attacks, while also offering reliable usability across multiple devices.

