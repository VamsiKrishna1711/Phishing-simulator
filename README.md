<img width="1847" height="887" alt="Screenshot 2026-05-02 221443" src="https://github.com/user-attachments/assets/636d21fb-0d6e-4a35-89ac-5bc847286545" />
<img width="1849" height="879" alt="Screenshot 2026-05-02 221453" src="https://github.com/user-attachments/assets/e7cf1d89-c8dc-49f7-8ebf-f6553faab74c" />
<img width="1821" height="883" alt="Screenshot 2026-05-02 221532" src="https://github.com/user-attachments/assets/162612d3-82ee-47ed-982d-e1d8e108b11a" />
<img width="1840" height="868" alt="Screenshot 2026-05-02 221816" src="https://github.com/user-attachments/assets/15e78635-0655-4622-a984-526f40cdfc05" />
<img width="1535" height="672" alt="Screenshot 2026-05-02 221824" src="https://github.com/user-attachments/assets/eb0f9f00-5e2c-407e-8ed8-ff57f2e5885e" />
<img width="1845" height="866" alt="Screenshot 2026-05-02 221759" src="https://github.com/user-attachments/assets/39e74e66-4043-43fd-bfe0-dab986140a74" />
<img width="1051" height="747" alt="Screenshot 2026-05-02 221648" src="https://github.com/user-attachments/assets/5679868f-83cd-4399-b669-9c1347a8830f" />



# 🎣 Phishing Simulator - Security Awareness Training Tool

A web-based phishing simulation platform designed to educate users about phishing attacks and improve organizational security awareness.

## 🎯 Project Purpose

This tool helps organizations:
- Test employee susceptibility to phishing attacks
- Track and analyze user behavior during simulated campaigns
- Provide immediate security awareness training
- Generate reports on organizational security posture

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY**

This tool is designed for:
- Cybersecurity training and education
- Authorized penetration testing with written permission
- Security awareness campaigns within your own organization

**DO NOT use this tool for:**
- Unauthorized phishing attacks
- Malicious purposes
- Testing systems you don't own or have permission to test

Unauthorized use may violate laws including the Computer Fraud and Abuse Act (CFAA) and similar legislation worldwide.

## 🚀 Features

- **Email Campaign Management**: Send simulated phishing emails to targets
- **Fake Login Pages**: Realistic credential harvesting simulation
- **Click Tracking**: Monitor who clicks on phishing links
- **Risk Scoring**: Automatic risk assessment based on user behavior
- **Analytics Dashboard**: Visual reports with charts and statistics
- **Security Awareness**: Immediate educational feedback for users who fall for the simulation
- **Admin Authentication**: Protected admin panel for viewing sensitive data
- **Audit Logging**: Complete activity logs for compliance

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js
- **Email**: SMTP (Mailtrap for testing)

## 📋 Prerequisites

- Python 3.7+
- pip (Python package manager)
- SMTP server access (Mailtrap recommended for testing)

## 🔧 Installation

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**:
```bash
# Copy the example env file
copy .env.example .env

# Edit .env with your actual credentials
notepad .env
```

4. **Set up your credentials in .env**:
```
SMTP_SERVER=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USER=your_mailtrap_username
SMTP_PASS=your_mailtrap_password
ADMIN_PASSWORD=your_secure_password
SECRET_KEY=your-random-secret-key
```

5. **Run the application**:
```bash
python app.py
```

6. **Access the dashboard**:
```
http://127.0.0.1:5000
```

## 🔐 Security Features Implemented

### 1. **No Hardcoded Credentials**
- All sensitive data stored in environment variables
- Config file separates credentials from code

### 2. **Input Validation & Sanitization**
- Regex validation on user inputs
- Protection against log injection attacks
- Email format validation

### 3. **SQL Injection Prevention**
- Parameterized queries throughout
- No string concatenation in SQL statements

### 4. **Admin Authentication**
- Password-protected admin routes
- Session-based authentication
- Logout functionality

### 5. **Secure Configuration**
- Debug mode disabled in production
- Secret key for session management
- Localhost binding by default

### 6. **Audit Logging**
- All activities logged with timestamps
- Sanitized log entries prevent injection
- Downloadable logs for compliance

## 📊 How It Works

1. **Admin sends phishing email** → Target receives realistic phishing email
2. **Target clicks link** → Click is logged, user redirected to fake login page
3. **Target enters credentials** → Data captured, risk score calculated
4. **Immediate feedback** → User sees awareness training page
5. **Admin reviews results** → Dashboard shows who clicked/logged in with risk scores

## 🎓 What I Learned Building This

- Web application security fundamentals
- Common phishing attack vectors and techniques
- Secure coding practices (input validation, parameterized queries)
- Authentication and session management
- Database design and SQL
- Flask framework and Python web development
- Security awareness training methodologies

## 🔮 Future Improvements

- [ ] Multiple email templates
- [ ] Campaign scheduling
- [ ] Email template customization UI
- [ ] More sophisticated risk scoring algorithms
- [ ] Export reports to PDF/CSV
- [ ] Multi-factor authentication for admin
- [ ] Support for multiple admin users
- [ ] Integration with Active Directory
- [ ] Mobile-responsive design improvements

## 🐛 Known Limitations

- Single admin user only
- Basic risk scoring algorithm
- No email template variety
- Local deployment only (not production-ready for internet exposure)
- Limited to SMTP email sending

## 📝 License

This project is for educational purposes. Use responsibly and ethically.

## 👤 Author

Created as part of cybersecurity career development following Google Cybersecurity Certification.

## 🙏 Acknowledgments

- Built to demonstrate understanding of phishing attack vectors
- Inspired by real-world security awareness training platforms
- Designed with ethical hacking principles in mind

---

**Remember**: Always obtain written permission before conducting any security testing.
