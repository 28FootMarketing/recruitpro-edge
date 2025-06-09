
import streamlit as st
import json
import os
from datetime import date
from fpdf import FPDF

st.set_page_config(page_title="👩‍👧 Lisa - Parent Communication Coach", layout="centered")
st.title("👩‍👧 Meet Lisa: Supporting You as You Support Your Athlete")

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tips_path = os.path.join(base_path, "data", "parents", "parent_tips.json")
prompts_path = os.path.join(base_path, "data", "parents", "weekly_prompts.json")
progress_path = os.path.join(base_path, "data/progress/shared_progress.json")

try:
    with open(tips_path, "r") as f:
        tips = json.load(f)
    with open(prompts_path, "r") as f:
        prompts = json.load(f)
    with open(progress_path, "r") as f:
        progress = json.load(f)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

st.subheader("📝 Parent Tip of the Week")
st.info(f"*{tips[date.today().isocalendar().week % len(tips)]}*")

st.subheader("💬 Conversation Starter")
st.markdown(f"**{prompts[date.today().isocalendar().week % len(prompts)]}**")

st.subheader("📊 Progress Check-In")
profile_updated = st.checkbox("Athlete updated their profile", value=progress["profile_updated"])
highlight_uploaded = st.checkbox("Highlight video uploaded", value=progress["highlight_uploaded"])
emails_sent = st.number_input("Emails sent to coaches", min_value=0, value=progress["emails_sent"])
new_colleges = st.number_input("New colleges added to list", min_value=0, value=progress["new_colleges_added"])

st.subheader("📥 Download Progress Summary")

def export_summary():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Parent Progress Summary", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {date.today()}", ln=True)
    pdf.cell(200, 10, txt=f"Profile Updated: {'Yes' if profile_updated else 'No'}", ln=True)
    pdf.cell(200, 10, txt=f"Highlight Video Uploaded: {'Yes' if highlight_uploaded else 'No'}", ln=True)
    pdf.cell(200, 10, txt=f"Emails Sent to Coaches: {emails_sent}", ln=True)
    pdf.cell(200, 10, txt=f"New Colleges Added: {new_colleges}", ln=True)
    output_path = os.path.join(base_path, "data", "parents", f"progress_summary_{date.today()}.pdf")
    pdf.output(output_path)
    return output_path

if st.button("Generate PDF Summary"):
    pdf_file_path = export_summary()
    with open(pdf_file_path, "rb") as f:
        st.download_button(
            label="📄 Download Summary PDF",
            data=f.read(),
            file_name=os.path.basename(pdf_file_path),
            mime="application/pdf"
        )
