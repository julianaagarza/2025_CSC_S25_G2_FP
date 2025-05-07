# Research on Various MFA Methods: Usability vs. Security


## Objective  
This document outlines the **advantages and disadvantages** of common multi-factor authentication (MFA) methods. Each method is evaluated based on its **usability** and **security**, helping determine which is best suited for a project where ease of use, secure implementation, and realistic deployment are all factors.

---

## 1. SMS-Based OTP

**Advantages:**
- Easy to set up and widely supported
- Does not require users to install an additional app
- Familiar to most users

**Disadvantages:**
- Highly vulnerable to SIM-swapping attacks
- Can be intercepted through SS7 network flaws
- Requires a reliable mobile network signal
- Limited logging or audit capabilities

**Usability vs. Security:**  
Very user-friendly, but has significant security weaknesses. Not recommended for systems managing sensitive data.

---

## 2. Email-Based OTP

**Advantages:**
- Easy to deploy; most users already have email access
- Doesn’t require installation of new software

**Disadvantages:**
- Depends on the security of the user’s email account
- Vulnerable to phishing and credential reuse
- No centralized visibility or control

**Usability vs. Security:**  
Simple and accessible, but security is only as strong as the user’s email password and device protection.

---

## 3. App-Based OTP (e.g., Google Authenticator)

**Advantages:**
- Generates codes locally on the device (no internet needed)
- Based on open standards (TOTP)
- Works across many platforms and services

**Disadvantages:**
- Requires users to manually enter a code
- No backup or recovery if the device is lost (unless paired with a backup solution)
- No central admin control or logging

**Usability vs. Security:**  
Offers a good balance. Stronger security than SMS/email, with only moderate usability friction.

---

## 4. Push Notification-Based MFA (e.g., Duo Push, Microsoft Authenticator)

**Advantages:**
- Extremely easy to use—just approve or deny
- Fast login with minimal typing
- Supports real-time alerting of unauthorized access

**Disadvantages:**
- Requires an internet connection
- Vulnerable to “MFA fatigue” attacks (e.g., repeated push requests)
- Often requires integration with a third-party platform and APIs

**Usability vs. Security:**  
High usability and solid security, but may introduce complexity in setup. Better suited for enterprise environments.

---

## 5. Biometric MFA (e.g., Fingerprint, Facial Recognition)

**Advantages:**
- Fast and convenient
- Can’t be forgotten or guessed
- Often built into mobile devices and laptops

**Disadvantages:**
- Biometric data cannot be changed if compromised
- False positives/negatives depending on sensor quality
- Not standardized across all platforms

**Usability vs. Security:**  
Very user-friendly and increasingly secure—but loss of biometric data can be irreversible, making it a high-stakes option.

---

## Summary and Recommendation

After evaluating each method, our group prioritized a solution that was:
- Secure enough for IoT use cases like camera access control
- Easy to integrate with a Flask-based system running on Raspberry Pi
- Practical for testing within a virtual or embedded environment

**Recommendation and Implementation:**  
We selected **Google Authenticator** for our MFA implementation due to its balance of simplicity and security. It uses the TOTP standard, works offline, and does not rely on third-party APIs or push services—making it ideal for resource-constrained environments like IoT.

As part of our project, we **implemented QR code-based TOTP authentication using Google Authenticator to secure access to a camera system running on a Raspberry Pi**. The QR code is scanned during enrollment and links the user’s app to their account. Upon successful login and OTP verification through Flask, the user is granted access to the camera’s image or live feed.

This approach keeps our solution lightweight, secure, and well-suited for real-world IoT deployment scenarios where usability and minimal resource impact are critical.
