
import streamlit as st
from pathlib import Path

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
