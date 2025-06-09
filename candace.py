
import streamlit as st
import json
import os

st.set_page_config(page_title="🧾 Candace – Compliance Tracker", layout="wide")
st.title("🧾 Candace – Compliance, Forms & Eligibility")

def load_compliance_data():
    try:
        with open("data/progress/shared_progress.json", "r") as f:
            return json.load(f)
    except:
        return {}

def check_compliance(profile):
    missing = []
    if not profile.get("ncaa_id"): missing.append("❌ NCAA ID not found.")
    if not profile.get("naia_id"): missing.append("❌ NAIA ID not found.")
    if not profile.get("transcript_uploaded"): missing.append("❌ Transcript not uploaded.")
    if not profile.get("compliance_forms_signed"): missing.append("❌ Compliance forms incomplete.")
    return missing

# Load profile data
profile = load_compliance_data()
missing_items = check_compliance(profile)

st.subheader("📋 Compliance Summary")
if missing_items:
    for item in missing_items:
        st.error(item)
    st.info("🔔 Candace recommends syncing with Lisa or your school counselor to upload required forms.")
else:
    st.success("✅ All compliance and eligibility fields appear complete.")

st.markdown("---")
st.subheader("📂 Stored Fields:")
st.write(f"NCAA ID: {profile.get('ncaa_id', 'N/A')}")
st.write(f"NAIA ID: {profile.get('naia_id', 'N/A')}")
st.write(f"Transcript Uploaded: {profile.get('transcript_uploaded', 'N/A')}")
st.write(f"Forms Signed: {profile.get('compliance_forms_signed', 'N/A')}")
