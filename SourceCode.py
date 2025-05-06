# --- Import necessary libraries ---
from flask import Flask, request, redirect, render_template_string, session
import pyotp
import datetime
import time
from functools import wraps
 
# --- Initialize Flask app and secret key (used for sessions) ---
app = Flask(__name__)
app.secret_key = 'supersecretkey'
 
# --- Define user roles (username, password, role) ---
roles = {
    "admin": {
        "username": "admin",
        "password": "adminpassword",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "userpassword",
        "role": "user"
    }
}
 
# --- Initialize TOTP MFA (same secret as QR code) ---
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
 
# --- Settings ---
SESSION_TIMEOUT = 120     # 2 minutes idle = auto logout
MAX_ATTEMPTS = 5          # Lock after 5 bad logins
LOCKOUT_TIME = 30         # Lockout duration in seconds
 
# --- Track failed attempts + lockout info (global variables) ---
failed_attempts = 0
lockout_until = 0
 
# --- HTML templates ---
login_page = '''
<h2>Login</h2>
<form method="post">
  Username: <input name="username"><br>
  Password: <input type="password" name="password"><br>
  MFA Code: <input name="otp"><br>
<input type="submit">
</form>
'''
 
camera_page = '''
<h2>Access Granted ✅</h2>
<img src="/static/cam.jpg" width="640">
'''
 
# --- Decorator to enforce session timeout (AFK auto logout) ---
def session_timeout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        last_activity = session.get('last_activity')
        if last_activity:
            now = datetime.datetime.now().timestamp()
            if now - last_activity > SESSION_TIMEOUT:
                session.clear()
                return redirect('/')
        session['last_activity'] = datetime.datetime.now().timestamp()
        return f(*args, **kwargs)
    return decorated_function
 
# --- Route: Login page ---
@app.route('/', methods=['GET', 'POST'])
def login():
    global failed_attempts, lockout_until
 
    # --- Check if currently locked out ---
    current_time = time.time()
    if current_time < lockout_until:
        remaining = int(lockout_until - current_time)
        return f"🔒 Too many failed attempts. Try again after {remaining} seconds."
 
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        otp = request.form['otp']
 
        # Find user by matching credentials
        user = None
        for role, info in roles.items():
            if info['username'] == username and info['password'] == password:
                user = info
                break
 
        # Check credentials + MFA
        if user and totp.verify(otp):
            # Reset failed attempts on successful login
            failed_attempts = 0
            session['role'] = user['role']
            session['last_activity'] = datetime.datetime.now().timestamp()
            return redirect('/camera')
        else:
            failed_attempts += 1
            if failed_attempts >= MAX_ATTEMPTS:
                lockout_until = time.time() + LOCKOUT_TIME
                return f"🔒 Too many failed attempts. Locked out for {LOCKOUT_TIME} seconds."
            return f"❌ Invalid login or MFA code. Attempts left: {MAX_ATTEMPTS - failed_attempts}"
 
    return render_template_string(login_page)
 
# --- Route: Camera page (protected with session timeout) ---
@app.route('/camera')
@session_timeout_required
def camera():
    if 'role' not in session:
        return redirect('/')
    return render_template_string(camera_page)
 
# --- Run Flask app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
