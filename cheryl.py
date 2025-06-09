
import streamlit as st
import json

def load_profile():
    try:
        with open("data/progress/shared_progress.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def academic_advice(profile):
    advice = []
    if profile.get("sat_score", 0) < 1000:
        advice.append("📉 Consider retaking the SAT to improve scholarship options.")
    if profile.get("intended_major", "") in ["Engineering", "Nursing", "Pre-Med"]:
        advice.append("🎓 Target schools with strong STEM programs.")
    if profile.get("academic_interest_level") == "High":
        advice.append("🧠 Consider applying for academic-based aid or honors colleges.")
    if not advice:
        advice.append("👍 Your academic profile looks solid. Maintain focus and communicate with academic advisors.")
    return advice

def show_cheryl():
    st.title("🎓 Cheryl – Academic Gameplan Coach")
    profile = load_profile()
    if not profile:
        st.error("No academic profile found.")
        return

    st.subheader("📚 Academic Review")
    st.write(f"SAT Score: {profile.get('sat_score', 'N/A')}")
    st.write(f"ACT Score: {profile.get('act_score', 'N/A')}")
    st.write(f"Intended Major: {profile.get('intended_major', 'N/A')}")
    st.write(f"Academic Interest Level: {profile.get('academic_interest_level', 'N/A')}")

    st.subheader("📝 Cheryl’s Suggestions")
    for note in academic_advice(profile):
        st.success(note)

# Launch Cheryl
show_cheryl()
