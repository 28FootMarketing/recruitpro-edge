
import smtplib
from email.mime.text import MIMEText
from pathlib import Path
from datetime import datetime

# CONFIGURATION (update these values before use)
SMTP_SERVER = "smtp.yourmail.com"
SMTP_PORT = 587
SMTP_USER = "you@example.com"
SMTP_PASS = "yourpassword"
RECIPIENT = "admin@example.com"
SENDER = "billbot@recruitproedge.com"

# Load log contents
log_file = Path("data/alerts/access_log.txt")
if not log_file.exists():
    print("No access log found.")
    exit()

log_content = log_file.read_text()

# Compose email
subject = f"📬 RecruitPro Access Report – {datetime.now().strftime('%Y-%m-%d')}"
message = MIMEText(log_content)
message["Subject"] = subject
message["From"] = SENDER
message["To"] = RECIPIENT

# Send email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SENDER, RECIPIENT, message.as_string())
    print("✅ Weekly access log sent.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
