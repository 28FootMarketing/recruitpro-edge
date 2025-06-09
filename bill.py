
import streamlit as st
import json
import os

st.set_page_config(page_title="🛡️ Bill – System Monitor", layout="wide")
st.title("🛡️ Bill – The General (System Monitor)")

# Fallback alert functions
def check_fields(profile):
    alerts = []
    if not profile.get("sport"): alerts.append("❌ Missing Sport")
    if not profile.get("gpa_score"): alerts.append("❌ Missing GPA")
    if not profile.get("intended_major"): alerts.append("❌ Missing Intended Major")
    if not profile.get("sat_score") and not profile.get("act_score"):
        alerts.append("❌ Missing SAT/ACT scores")
    if not profile.get("location_preference"): alerts.append("❌ Missing Location Preference")
    return alerts

def load_progress():
    try:
        with open("data/progress/shared_progress.json", "r") as f:
            return json.load(f)
    except:
        return {}

def show_fallback_advice(alerts):
    if alerts:
        st.subheader("⚠️ Attention Needed")
        for a in alerts:
            st.error(a)
        st.info("Bill recommends syncing with Jordan or contacting Maya for motivational reset.")
    else:
        st.success("✅ All systems go. No critical fields missing.")

# Load data and evaluate
profile = load_progress()
st.subheader("📊 System Review Summary")
alerts = check_fields(profile)
show_fallback_advice(alerts)
