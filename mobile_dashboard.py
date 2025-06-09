import streamlit as st

# Safe initialization for active_agent
if "active_agent" not in st.session_state:
    st.session_state["active_agent"] = "jordan"
    st.experimental_rerun()

# Load the selected agent screen
agent = st.session_state["active_agent"]

# Placeholder render (replace with actual navigation/render logic)
st.title("RecruitPro Edge Mobile Dashboard")
st.success(f"Currently viewing: {agent.capitalize()}'s module")