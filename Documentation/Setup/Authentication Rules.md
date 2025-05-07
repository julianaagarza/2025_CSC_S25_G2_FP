# MFA Authentication Rules


## Objective  
This document outlines the **authentication rules** and **enforcement policies** for our project, which secures access to a camera system via a Raspberry Pi using MFA with **Google Authenticator**. The goal is to ensure clear, role-based and context-aware application of multi-factor authentication, enhancing security without unnecessary friction.

---

## 1. When MFA Is Required

We have defined the following conditions under which MFA will be enforced:

### Required Scenarios
- **Every login from a new device**  
  MFA is triggered when the system detects a login attempt from an unknown or previously unused browser/device.

- **First-time login per user**  
  During the user’s initial login to the camera access system, MFA is enforced to verify identity before access is granted.

- **Every login after logout**  
  Each complete login cycle (after logout) will require MFA.

- **Administrative or configuration access attempts**  
  If a user attempts to access camera configuration or admin-level controls (e.g., change resolution, update code), MFA is enforced regardless of session status.

---

## 2. MFA Enforcement by User Role

The system distinguishes between two user roles: **Standard User** and **Administrator**. MFA is enforced differently based on the level of system access and risk.

### Standard User
- **Access:** View-only access to camera feed (image or video)
- **MFA Policy:** MFA is required only on first login, or when accessing from a new device.
- **Session Length:** MFA is remembered for the duration of the current browser session.

### Administrator
- **Access:** Can view feed and modify system settings (e.g., enable/disable camera, restart services, change user permissions)
- **MFA Policy:** MFA is required on **every login**, regardless of device.  
  Additionally, re-verification is required before performing any critical configuration change.

---

## 3. Session Timeout and Re-Authentication

- **Session Timeout:** Sessions will expire after **15 minutes** of inactivity. Upon timeout, users will be logged out and MFA will be required again at the next login.
- **"Remember This Device" Option:** Not implemented for this project to maintain strict control in the IoT context, where device ownership can’t always be assumed secure.

---

## Justification for Selected Policies

Since this project simulates access to a potentially sensitive system (a live camera feed), enforcing MFA on first access and all admin actions helps prevent unauthorized use while minimizing user frustration for basic viewers. 
Using **Google Authenticator** with QR-based enrollment fits well into this approach by being secure, offline-capable, and easy to implement in a Python Flask environment without relying on external services.
