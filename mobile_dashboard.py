import streamlit as st

# Session-based navigation
if "active_agent" not in st.session_state:
    st.session_state["active_agent"] = "home"

if st.session_state["active_agent"] == "home":
    st.title("🏅 All-Star Agent Dashboard")
    st.markdown("Choose your recruiting support agent:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Jordan – Onboarding"):
if "active_agent" not in st.session_state:
    st.session_state["active_agent"] = "jordan"
    st.experimental_rerun()

        if st.button("📘 Maya – Education Coach"):
        if st.button("👨‍👩‍👧 Lisa – Parent Portal"):
        if st.button("🎯 Magic – Opportunity Connector"):
    with col2:
        if st.button("📚 Cheryl – Academic Advisor"):
        if st.button("🎤 Kareem – Wisdom Coach"):
        if st.button("🔥 Kobe – Training & Mental Toughness"):
        if st.button("💬 Dawn – Mood Reset"):
        if st.button("🧾 Candace – Compliance Tracker"):
        if st.button("📊 Bill – System Manager"):
        if st.button("📚 Ebony – Mentor Support"):

# Route to agents
if st.session_state["active_agent"] == "jordan":
    from agents.jordan import jordan_main; jordan_main()
elif st.session_state["active_agent"] == "maya":
    from agents.maya import maya_main; maya_main()
elif st.session_state["active_agent"] == "lisa":
    from agents.lisa import lisa_main; lisa_main()
elif st.session_state["active_agent"] == "magic":
    from agents.magic import magic_main; magic_main()
elif st.session_state["active_agent"] == "cheryl":
    from agents.cheryl import cheryl_main; cheryl_main()
elif st.session_state["active_agent"] == "kareem":
    from agents.kareem import kareem_main; kareem_main()
elif st.session_state["active_agent"] == "kobe":
    from agents.kobe import kobe_main; kobe_main()
elif st.session_state["active_agent"] == "dawn":
    from agents.dawn import dawn_main; dawn_main()
elif st.session_state["active_agent"] == "candace":
    from agents.candace import candace_main; candace_main()
elif st.session_state["active_agent"] == "bill":
    from agents.bill import bill_main; bill_main()
elif st.session_state["active_agent"] == "ebony":
    from agents.ebony import ebony_main; ebony_main()