# Environment Setup Steps

This document outlines our steps to set up the Raspberry Pi environment with Flask and Google Authenticator for securing access to a connected USB webcam using multi-factor authentication (MFA).

---

## Hardware & Tools Used

- **Device**: Raspberry Pi 4
- **Camera**: 720p Logi USB Webcam  
- **Command to capture image**:  
  ```bash
  fswebcam -r 1280x720 cam.jpg

- **Operating System**: Raspberry Pi OS  
- **Web Framework**: Flask  
- **MFA Method**: Google Authenticator (TOTP-based codes)

## Environment Setup Steps

1. **Install Dependencies**  
   - Update and upgrade the Pi.  
   - Install Python3, Flask, fswebcam, and pyotp.

2. **Import Required Libraries**  
   - Set up the Flask web server and include modules for TOTP, sessions, and HTML rendering.

3. **Initialize Flask App & Secret Key**  
   - Create a Flask app instance and define a secret key for session management.

4. **Define User Roles**  
   - Configure hardcoded user credentials and their roles (admin/user) within the application.

5. **Initialize TOTP for MFA**  
   - Set up the TOTP object using a base32 secret shared with Google Authenticator.

6. **Configure Security Settings**  
   - Define session timeout duration, maximum login attempts, and lockout time after failed logins.

7. **Track Failed Logins**  
   - Add global variables to monitor and control failed login attempts and lockout timing.

8. **Create Login HTML Template**  
   - Design a basic form requesting username, password, and MFA code.

9. **Create Camera Access Template**  
   - Design a simple page to display the webcam image upon successful login.

10. **Implement Session Timeout Decorator**  
    - Build a function that logs users out after being idle beyond the timeout limit.

11. **Build the Login Route**  
    - Handle authentication: check username, password, and TOTP code, and redirect appropriately.  
    - Implement lockout logic and attempt counter for failed logins.

12. **Build Camera Access Route**  
    - Protect the camera access page using the session timeout decorator and role check.

13. **Run the Flask Server**  
    - Launch the app so it listens on all network interfaces on port 5000.

## Final Output

Once configured, users will access the Flask web portal, log in using their credentials and a TOTP code from Google Authenticator, and securely view the camera feed if authenticated successfully.

