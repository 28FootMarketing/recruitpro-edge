
import streamlit as st
import json

st.set_page_config(page_title="📚 Ebony – Mentor/Mentee Triage", layout="wide")
st.title("📚 Ebony – Mentor/Mentee Triage Support")

def load_profile():
    try:
        with open("data/progress/shared_progress.json", "r") as f:
            return json.load(f)
    except:
        return {}

def triage_check(profile):
    flags = []
    if profile.get("mentorship_status") == "inactive":
        flags.append("⛔ No current mentor relationship established.")
    if profile.get("mentee_goals", "") == "":
        flags.append("⚠️ Mentee goals not yet defined.")
    if profile.get("mentor_checkin_frequency", "") == "rarely":
        flags.append("⚠️ Mentor check-ins are too infrequent.")
    if profile.get("mentor_communication_quality", "") == "low":
        flags.append("⚠️ Communication quality is poor.")
    return flags

def triage_advice(flags):
    st.subheader("🩺 Triage Summary")
    if not flags:
        st.success("✅ Mentor/Mentee relationship appears stable and productive.")
    else:
        for f in flags:
            st.error(f)
        st.info("💡 Ebony recommends clarifying roles, setting mutual goals, and syncing with Maya for mindset reinforcement.")

# Load and process
profile = load_profile()
st.subheader("🔍 Reviewing Mentor/Mentee Relationship Fields")
st.write(f"Mentorship Status: {profile.get('mentorship_status', 'N/A')}")
st.write(f"Mentee Goals: {profile.get('mentee_goals', 'N/A')}")
st.write(f"Check-in Frequency: {profile.get('mentor_checkin_frequency', 'N/A')}")
st.write(f"Communication Quality: {profile.get('mentor_communication_quality', 'N/A')}")

# Display triage review
triage_advice(triage_check(profile))
