
import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="🔒 RecruitPro Edge – Mobile Dashboard", layout="centered")
st.title("🔒 RecruitPro Edge – Mobile Dashboard")

# Passcode lock
correct_passcode = "edge123"  # Change as needed
passcode = st.text_input("Enter Access Code:", type="password")

# Log access attempts
log_dir = Path("data/alerts")
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "access_log.txt"
log_file.write_text(f"{datetime.now()} - Access Attempted\n", encoding='utf-8')

if passcode != correct_passcode:
    st.warning("Access restricted. Enter the correct code.")
    log_file.write_text(f"{datetime.now()} - ❌ Failed login with code: {passcode}\n", encoding='utf-8')
    st.stop()
else:
    log_file.write_text(f"{datetime.now()} - ✅ Successful login\n", encoding='utf-8')

# System status
status_file = Path("data/alerts/system_status.txt")
if status_file.exists():
    content = status_file.read_text()
    if "GREEN" in content:
        st.success("✅ System Status: GREEN — All systems operational.")
    elif "YELLOW" in content:
        st.warning("⚠️ System Status: YELLOW — Some fields missing.")
    elif "RED" in content:
        st.error("🚨 System Status: RED — Immediate attention needed.")
    else:
        st.info("ℹ️ System Status: Unknown.")
else:
    st.info("System status file not found.")

# Agent quick access
st.markdown("### ⚙️ Quick Access")
agents = [
    "Jordan", "Maya", "Lisa", "Magic", "Cheryl",
    "Candace", "Dawn", "Ebony", "Kareem", "Kobe", "Bill"
]
for agent in agents:
    st.button(f"Launch {agent}")

# System alerts
st.markdown("### 🔔 System Alerts")
log_path = Path("data/alerts/deletion_log.txt")
if log_path.exists():
    with open(log_path, "r") as log:
        entries = log.readlines()[-5:]
        for entry in reversed(entries):
            st.code(entry.strip())
else:
    st.info("No recent alerts logged.")

# Mini-report viewer
st.markdown("### 📄 Latest System Report")
report_files = list(Path("agents/bill/reports").glob("bill_*.txt"))
if report_files:
    latest = sorted(report_files, key=lambda x: x.stat().st_mtime, reverse=True)[0]
    st.text(f"🗂 Viewing: {latest.name}")
    st.code(latest.read_text())
else:
    st.info("No reports found.")
