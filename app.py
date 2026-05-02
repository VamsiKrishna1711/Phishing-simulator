from flask import Flask, render_template, request, send_file, session, redirect, url_for
import datetime
import sqlite3
import smtplib
from email.mime.text import MIMEText
import re
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

clicks = []

def init_db():
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            timestamp TEXT,
            ip TEXT,
            risk_score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def write_log(message):
    timestamp = datetime.datetime.now()
    safe_message = message.replace('\n', ' ').replace('\r', '')
    log_entry = f"[{timestamp}] {safe_message}\n"
    with open("log.txt", "a") as f:
        f.write(log_entry)

def calculate_risk_score(username, ip_address):
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM logins WHERE username = ? OR ip = ?",
        (username, ip_address)
    )
    previous_attempts = cursor.fetchone()[0]
    conn.close()
    
    if previous_attempts > 0:
        return min(5, 2 + previous_attempts)
    return 1

def send_phishing_email(target_email):
    body = f"""Subject: Password Reset Required

Dear User,

Your password will expire today.

Click the link below:

http://127.0.0.1:5000/track?user={target_email}

IT Security Team
"""
    msg = MIMEText(body)
    server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    server.login(config.SMTP_USER, config.SMTP_PASS)
    server.sendmail(config.SMTP_USER, target_email, msg.as_string())
    server.quit()
    write_log(f"Phishing email sent to: {target_email}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/track")
def track():
    user = request.args.get("user", "unknown")
    user = re.sub(r'[^a-zA-Z0-9@._-]', '', user)[:100]
    clicks.append(user)
    write_log(f"User clicked phishing link: {user}")
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "")
    
    if not username or len(username) > 100:
        return "Invalid input", 400
    
    safe_username = re.sub(r'[^a-zA-Z0-9@._-]', '', username)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.remote_addr
    risk_score = calculate_risk_score(username, ip_address)
    
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logins (username, timestamp, ip, risk_score) VALUES (?, ?, ?, ?)",
        (username, timestamp, ip_address, risk_score)
    )
    conn.commit()
    conn.close()
    
    write_log(f"Login attempt: {safe_username} | IP: {ip_address}")
    return render_template("awareness.html")

@app.route("/report")
def report():
    if not session.get("authenticated"):
        return redirect(url_for("admin_login"))
    
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, timestamp, ip, risk_score FROM logins")
    users = cursor.fetchall()
    conn.close()
    
    return render_template(
        "report.html",
        click_count=len(clicks),
        login_count=len(users),
        users=users
    )

@app.route("/send_email", methods=["GET", "POST"])
def send_email():
    if not session.get("authenticated"):
        return redirect(url_for("admin_login"))
    
    if request.method == "POST":
        target_email = request.form.get("email", "")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", target_email):
            return "Invalid email", 400
        
        try:
            send_phishing_email(target_email)
            return "Email sent successfully"
        except Exception as e:
            write_log(f"Email failed: {str(e)}")
            return "Failed to send email", 500
    
    return render_template("send_email.html")

@app.route("/download_logs")
def download_logs():
    if not session.get("authenticated"):
        return redirect(url_for("admin_login"))
    return send_file("log.txt", as_attachment=True)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == config.ADMIN_PASSWORD:
            session["authenticated"] = True
            return redirect(url_for("report"))
        return render_template("admin_login.html", error="Invalid password")
    return render_template("admin_login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop("authenticated", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=False, host="127.0.0.1", port=5000)
