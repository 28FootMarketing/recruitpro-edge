
import streamlit as st
import os

st.set_page_config(page_title="🏆 All-Star Agent Dashboard", layout="wide")

st.title("🏆 All-Star AI Support Team")
st.markdown("Navigate below to access each agent and their tools.")

pages = {
    "🏀 Jordan – Athlete Profile Intake": "jordan.py",
    "🧠 Maya – Mindset & Motivation Coach": "maya.py",
    "👨‍👩‍👧 Lisa – Parent Dashboard": "lisa.py",
    "🔮 Magic – Opportunity Connector": "magic.py",
    "🎓 Cheryl – Academic Gameplan Coach": "cheryl.py",
    "🛡️ Bill – System Monitor": "bill.py",
    "📚 Ebony – Mentor/Mentee Triage": "ebony.py",
    "🧾 Candace – Compliance Tracker": "candace.py",
    "💬 Dawn – Emotional Reset (Coming Soon)": None
}

for name, script in pages.items():
    if script and os.path.exists(script):
        st.button(name, on_click=lambda s=script: st.switch_page(s))
    else:
        st.button(name, disabled=True)
