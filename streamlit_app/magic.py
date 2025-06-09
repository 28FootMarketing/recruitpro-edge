
import streamlit as st
import json
import os
from fpdf import FPDF
from datetime import date

st.set_page_config(page_title="🎩 Magic - Opportunity Connector", layout="centered")
st.title("🎩 Meet Magic: Your College Opportunity Connector")

# Load athlete profile from shared_progress.json
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
progress_path = os.path.join(base_path, "data", "progress", "shared_progress.json")
match_file = os.path.join(base_path, "data", "magic", "match_rules.json")

try:
    with open(progress_path, "r") as f:
        shared_profile = json.load(f)
except Exception as e:
    st.warning("Shared profile not found. Please complete onboarding with Jordan.")
    shared_profile = {"gpa": 0.0, "sport": ""}

try:
    with open(match_file, "r") as f:
        match_rules = json.load(f)
except Exception as e:
    st.error(f"Failed to load match rules: {e}")
    st.stop()

# Prefilled athlete info
st.subheader("🎓 Your Profile")
gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=shared_profile.get("gpa", 0.0), step=0.1)
sport = st.selectbox("Sport", ["Basketball", "Football", "Soccer", "Track"], index=0 if shared_profile.get("sport") not in ["Basketball", "Football", "Soccer", "Track"] else ["Basketball", "Football", "Soccer", "Track"].index(shared_profile.get("sport", "Basketball")))
region = st.selectbox("Preferred Region", ["All", "East", "South", "Midwest", "West"])
location_pref = st.selectbox("Preferred Location Type", ["All", "Urban", "Suburban", "Rural"])
filter_hbcu = st.checkbox("HBCU Only")
filter_nil = st.checkbox("NIL Opportunity")

# Matching logic
st.subheader("📬 Magic's College Suggestions + Match Scores")
suggested_schools = []

for rule in match_rules:
    region_match = region == "All" or region in rule["regions"]
    location_match = location_pref == "All" or location_pref == rule.get("location_type", "")
    hbcu_match = not filter_hbcu or "HBCU" in rule.get("tags", [])
    nil_match = not filter_nil or "NIL" in rule.get("tags", [])

    if (
        rule["gpa_range"][0] <= gpa <= rule["gpa_range"][1]
        and sport in rule["sports"]
        and region_match and location_match and hbcu_match and nil_match
    ):
        for school in rule["suggestions"]:
            score = 0
            if rule["gpa_range"][0] <= gpa <= rule["gpa_range"][1]:
                score += 30
            if sport in rule["sports"]:
                score += 30
            if region_match:
                score += 20
            if filter_nil and "NIL" in rule.get("tags", []):
                score += 10
            if filter_hbcu and "HBCU" in rule.get("tags", []):
                score += 10
            suggested_schools.append((school, score, rule.get("tags", []), rule.get("location_type", "")))

if suggested_schools:
    suggested_schools = sorted(suggested_schools, key=lambda x: x[1], reverse=True)
    st.success("Magic found your best-fit colleges:")
    for school, score, tags, location in suggested_schools:
        st.markdown(f"- **{school}** – Score: `{score}/100` | Tags: `{', '.join(tags)}` | Location: `{location}`")
else:
    st.warning("No direct matches found. Try adjusting your filters or contact your coach.")

# PDF Export
st.subheader("📄 Export My Matches")

def export_matches():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Magic's College Match Summary", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {date.today()}", ln=True)
    pdf.cell(200, 10, txt=f"GPA: {gpa}", ln=True)
    pdf.cell(200, 10, txt=f"Sport: {sport}", ln=True)
    pdf.cell(200, 10, txt=f"Region: {region}", ln=True)
    pdf.cell(200, 10, txt=f"Location Type: {location_pref}", ln=True)
    pdf.cell(200, 10, txt=f"Filters: HBCU={filter_hbcu}, NIL={filter_nil}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Matches:", ln=True)
    for school, score, tags, location in suggested_schools:
        pdf.cell(200, 10, txt=f"- {school} ({score}/100) [{', '.join(tags)}] - {location}", ln=True)
    output_path = os.path.join(base_path, "data", "magic", f"college_matches_{date.today()}.pdf")
    pdf.output(output_path)
    return output_path

if suggested_schools and st.button("Generate Match PDF"):
    pdf_path = export_matches()
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download My Matches",
            data=f.read(),
            file_name=os.path.basename(pdf_path),
            mime="application/pdf"
        )
