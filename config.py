import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SMTP Configuration - CHANGE THESE VALUES
SMTP_SERVER = os.getenv("SMTP_SERVER", "sandbox.smtp.mailtrap.io")
SMTP_PORT = int(os.getenv("SMTP_PORT", "2525"))
SMTP_USER = os.getenv("SMTP_USER", "your_smtp_user")
SMTP_PASS = os.getenv("SMTP_PASS", "your_smtp_password")

# Admin Authentication - CHANGE THIS PASSWORD
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "change_this_password_123")

# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-to-random-string-in-production")

# Database
DATABASE = "phishing.db"
