# Project Environment Selection


## Objective  
This document explains the rationale behind selecting our test environment and hardware setup for implementing multi-factor authentication (MFA) in an IoT-based security system. It covers our decision to use an Raspberry Pi with a camera module and provides reasoning that aligns with both course concepts and project goals.

---

## 1. Test Environment Evaluation

We considered three main options for hosting the system:

### Option 1: Virtual Machine (VM)  
- **Pros:** Easy to reset/test; controlled environment  
- **Cons:** Not realistic for simulating IoT hardware  
- **Limitation:** Limited interaction with physical devices like cameras or sensors

### Option 2: Cloud-Hosted Server (e.g., AWS, Azure)  
- **Pros:** Scalable, remote access possible, supports real-world deployment conditions  
- **Cons:** Cost and complexity; would still require remote integration with a physical IoT device  
- **Limitation:** Not ideal for beginner-level or embedded device prototyping

### Option 3: Local Hardware (Raspberry Pi + Camera)  
- **Pros:** Physical device reflects real IoT scenarios; supports peripherals (camera)  
- **Cons:** Requires setup and monitoring of physical hardware  
- **Benefit:** Enables hands-on experience and aligns with the course's emphasis on **endpoint security**, **network configuration**, and **IoT-specific challenges**

---

## 2. Final Environment Choice: On-Premises Local Hardware

We chose to **host the project on a Raspberry Pi with a connected camera**, operating as a local web server secured by MFA.

### Justification:
- **Reflects Course Concepts:** The project incorporates multiple topics covered in the course, including endpoint security, authentication layers, threat modeling, and device hardening.
- **Simulates a Real-World Use Case:** Cameras are widely used in IoT security systems. Access control to camera feeds is critical in smart homes, industrial settings, and even school security.
- **Hands-On Security Implementation:** The Raspberry Pi allows full control over the OS and network, letting us directly implement firewalls, authentication, and encryption protocols.
- **Supports Lightweight Web Application:** We are able to host a Flask-based web interface on the Pi, where users must authenticate via password and QR code to access the camera.
- **Cost-Effective and Flexible:** The Raspberry Pi is affordable, reusable, and capable of supporting Python, Flask, and OpenCV—all tools relevant to our skillset and this course.

---

## Conclusion

By choosing an Raspberry Pi with a camera, we created a realistic IoT testing environment that mirrors real-world scenarios while remaining appropriate for an academic project. This setup allows us to implement, monitor, and evaluate MFA in a way that supports both academic learning and practical cybersecurity application.
