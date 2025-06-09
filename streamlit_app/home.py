
import streamlit as st
import os

st.set_page_config(page_title="🏟️ RecruitPro Edge – All-Star Support Team", layout="centered")
st.title("🏟️ RecruitPro Edge – All-Star Support Team")

st.markdown("""
Welcome to your personal recruiting command center.

Choose an AI Agent below to guide you through your journey:
- Jordan will help you get started and build your recruiting profile
- Maya will keep you motivated with weekly challenges and mindset coaching
- Lisa will help your parents stay aligned, informed, and supportive
""")

# Agent Selector
agent = st.radio("Select Your Agent:", ["Jordan – Onboarding", "Maya – Motivation", "Lisa – Parent Coach"])

if agent == "Jordan – Onboarding":
    st.markdown("▶️ Click below to launch Jordan:")
    st.code("streamlit run jordan.py", language="bash")
    st.link_button("Launch Jordan", "jordan.py")

elif agent == "Maya – Motivation":
    st.markdown("▶️ Click below to launch Maya:")
    st.code("streamlit run maya.py", language="bash")
    st.link_button("Launch Maya", "maya.py")

elif agent == "Lisa – Parent Coach":
    st.markdown("▶️ Click below to launch Lisa:")
    st.code("streamlit run lisa.py", language="bash")
    st.link_button("Launch Lisa", "lisa.py")

st.markdown("---")
st.info("More agents like Magic and Bill are coming soon.")
