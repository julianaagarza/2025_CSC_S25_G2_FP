# Issues and Troubleshooting in Environment Setup



When the project environment was initially set up on a Raspberry Pi, the Flask server was accessible only through the local area network (LAN). This meant that only users connected to the same Wi-Fi network could reach the login portal via the Raspberry Pi's IP address and port (`192.168.1.171:5000`).

### Challenge:
This limited our ability to conduct multi-user testing and demo the system remotely. It also did not reflect a real-world scenario where users often authenticate from various locations.

### Solution: Ngrok
To address this, we used **Ngrok**, a secure tunneling service that allows local servers to be exposed to the internet.

**What is Ngrok?**  
Ngrok is a flexible API gateway that provides instant, secure access to internal services from external networks. It creates a secure tunnel between a public endpoint and the Flask server running on the Raspberry Pi.

**Steps Taken:**
- Installed Ngrok on the Raspberry Pi.
- Linked the account and authenticated using the Ngrok token.
- Ran `ngrok http 5000` to generate a public HTTPS address.
- Shared the public URL with team members for remote access and testing.

**Outcome:**  
This allowed all group members to access the web app from their own devices, enabling broader testing, troubleshooting, and feedback collection.
