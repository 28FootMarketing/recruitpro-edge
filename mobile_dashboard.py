import streamlit as st

# Safe initialization
if "active_agent" not in st.session_state:
    st.session_state["active_agent"] = "jordan"
    st.stop()  # Avoid early rerun crash

# Load selected agent view
agent = st.session_state["active_agent"]

# Display dashboard
st.title("RecruitPro Edge Mobile Dashboard")
st.success(f"Currently viewing: {agent.capitalize()}'s module")