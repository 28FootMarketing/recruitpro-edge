import streamlit as st

# Initialize default agent
if "active_agent" not in st.session_state:
    st.session_state["active_agent"] = "jordan"
    st.experimental_rerun()

agent = st.session_state.get("active_agent", "jordan")

st.title("RecruitPro Edge Mobile Dashboard")
st.success(f"Currently viewing: {agent.capitalize()}'s module")

# Dynamically load agent modules with render functions
try:
    if agent == "jordan":
        import jordan
        jordan.render()
    elif agent == "maya":
        import maya
        maya.render()
    elif agent == "lisa":
        import lisa
        lisa.render()
    elif agent == "magic":
        import magic
        magic.render()
    elif agent == "kobe":
        import kobe
        kobe.render()
    elif agent == "kareem":
        import kareem
        kareem.render()
    elif agent == "candace":
        import candace
        candace.render()
    elif agent == "dawn":
        import dawn
        dawn.render()
    elif agent == "ebony":
        import ebony
        ebony.render()
    else:
        st.warning("Unknown agent selected.")
except Exception as e:
    st.error(f"Error loading agent: {e}")

# Agent Activation Selector UI
st.sidebar.header("🎯 Choose Your Agent")
agent_options = [
    "jordan", "maya", "lisa", "magic",
    "kobe", "kareem", "candace", "dawn", "ebony"
]

selected_agent = st.sidebar.radio("Select Agent:", agent_options, index=agent_options.index(agent))

if selected_agent != agent:
    st.session_state["active_agent"] = selected_agent
    st.experimental_rerun()