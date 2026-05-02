# 🔧 SETUP GUIDE - READ THIS FIRST

## What Was Fixed

### 🚨 Critical Security Issues (FIXED)
1. **Hardcoded Credentials** - Moved to config.py and .env file
2. **No Input Validation** - Added regex sanitization on all user inputs
3. **Debug Mode Enabled** - Disabled for production
4. **No Admin Authentication** - Added password protection for admin routes
5. **Log Injection Vulnerability** - Sanitized all log entries
6. **Hardcoded Risk Score** - Now calculates based on actual user behavior

### ✅ What You Need to Understand for Interviews

**Q: "Tell me about your phishing simulator project"**

A: "I built a web-based phishing simulation tool using Flask and Python. It allows security teams to send simulated phishing emails, track who clicks the links and enters credentials, then provides immediate security awareness training. The system includes risk scoring, analytics dashboards, and audit logging. I focused heavily on secure coding practices like input validation, parameterized SQL queries, and proper credential management."

**Q: "What security measures did you implement?"**

A: "Several key measures:
- Input validation using regex to prevent injection attacks
- Parameterized SQL queries to prevent SQL injection
- Admin authentication with session management
- Environment variables for credential storage instead of hardcoding
- Log sanitization to prevent log injection
- Disabled debug mode for production
- Email validation before sending"

**Q: "What would you improve?"**

A: "I'd add multi-factor authentication for admins, implement role-based access control, add more sophisticated risk scoring using machine learning, create multiple email templates, add campaign scheduling, and implement rate limiting to prevent abuse."

## 🚀 How to Run This Project

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get SMTP Credentials (FREE)
1. Go to https://mailtrap.io
2. Sign up for free account
3. Go to "Email Testing" → "Inboxes" → "My Inbox"
4. Copy the SMTP credentials

### Step 3: Configure Your Environment
1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` file with your credentials:
   ```
   SMTP_SERVER=sandbox.smtp.mailtrap.io
   SMTP_PORT=2525
   SMTP_USER=<your_mailtrap_username>
   SMTP_PASS=<your_mailtrap_password>
   ADMIN_PASSWORD=MySecurePassword123
   SECRET_KEY=random-string-here-change-this
   ```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Dashboard
Open browser: http://127.0.0.1:5000

### Step 6: Test It Out
1. Click "Send Phishing Email"
2. Enter your Mailtrap email (shown in Mailtrap dashboard)
3. Check Mailtrap inbox for the phishing email
4. Click the link in the email
5. Enter fake credentials
6. See the awareness training page
7. Go back to dashboard → "View Campaign Report" (requires admin password)

## 📁 Project Structure Explained

```
Phishing simulator/
│
├── app.py                  # Main Flask application (ALL the logic)
├── config.py               # Configuration file (credentials loaded here)
├── requirements.txt        # Python dependencies
├── .env                    # Your actual credentials (DON'T COMMIT THIS)
├── .env.example            # Example env file (safe to commit)
├── .gitignore              # Prevents committing sensitive files
├── README.md               # Professional project documentation
├── phishing.db             # SQLite database (auto-created)
├── log.txt                 # Activity logs (auto-created)
│
└── templates/              # HTML pages
    ├── index.html          # Main dashboard
    ├── login.html          # Fake login page (phishing page)
    ├── awareness.html      # Training page after user falls for it
    ├── report.html         # Analytics dashboard
    ├── send_email.html     # Email sending interface
    └── admin_login.html    # Admin authentication page

```

## 🎯 Key Code Sections to Understand

### 1. Input Validation (app.py line ~50)
```python
# Sanitize input to prevent injection attacks
user = re.sub(r'[^a-zA-Z0-9@._-]', '', user)[:100]
```
**Why**: Removes dangerous characters that could break logs or inject code

### 2. Parameterized SQL Query (app.py line ~75)
```python
cursor.execute(
    "INSERT INTO logins (username, timestamp, ip, risk_score) VALUES (?, ?, ?, ?)",
    (username, time_now, ip_address, risk_score)
)
```
**Why**: The `?` placeholders prevent SQL injection attacks

### 3. Admin Authentication (app.py line ~95)
```python
if not session.get("authenticated"):
    return redirect(url_for("admin_login"))
```
**Why**: Protects sensitive routes from unauthorized access

### 4. Risk Score Calculation (app.py line ~180)
```python
def calculate_risk_score(username, ip_address):
    # Check if user has fallen for phishing before
    # Increase score for repeat offenders
```
**Why**: Shows you understand behavioral analysis in security

## 🎤 Demo Script for Interviews

"Let me show you my phishing simulator. [Open browser]

This is the main dashboard. From here, I can send phishing emails, view reports, and download logs.

[Click Send Email] I'll send a test phishing email. The system uses SMTP to deliver realistic-looking emails.

[Show Mailtrap inbox] Here's the email that was sent. Notice it looks like a legitimate password reset request.

[Click link in email] When the user clicks, we log that click and redirect them to a fake login page.

[Enter credentials] When they enter credentials, we capture that data, calculate a risk score based on their history, and immediately show them security awareness training.

[Go to reports] The admin dashboard requires authentication. [Login] Here we can see analytics - who clicked, who entered credentials, their risk scores, and timestamps. All of this is logged for compliance.

The entire system is built with security in mind - input validation, parameterized queries, no hardcoded credentials, and proper authentication."

## ⚠️ Common Issues

**Issue**: "Module not found: flask"
**Fix**: Run `pip install -r requirements.txt`

**Issue**: "Can't send emails"
**Fix**: Check your .env file has correct Mailtrap credentials

**Issue**: "Database locked"
**Fix**: Close any other programs accessing phishing.db

**Issue**: "Admin password not working"
**Fix**: Check ADMIN_PASSWORD in your .env file

## 🎓 Study These Concepts

Before interviews, make sure you understand:
- What is SQL injection and how parameterized queries prevent it
- What is input validation and why it matters
- What is session-based authentication
- What is SMTP and how email works
- What is phishing and common attack vectors
- What is security awareness training
- What is risk scoring in cybersecurity

## 📝 Next Steps

1. ✅ Run the project and test all features
2. ✅ Read through app.py and understand each function
3. ✅ Practice explaining the project out loud
4. ✅ Add this to your resume
5. ✅ Push to GitHub (make sure .env is in .gitignore!)
6. ✅ Add screenshots to README
7. ✅ Consider adding one more feature (email templates?)

Good luck with your cybersecurity career! 🚀
