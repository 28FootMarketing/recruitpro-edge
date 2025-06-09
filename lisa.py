
import json
import streamlit as st

def load_magic_results():
    try:
        with open("data/output/magic_matches.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_lisa_dashboard():
    st.header("📊 Parent Dashboard – School Match Summary")
    matches = load_magic_results()
    if not matches:
        st.warning("No results found. Ask your athlete to complete their profile.")
        return

    for match in matches:
        st.subheader(f"{match['school_name']}")
        st.write(f"📍 Location: {match['location']} | 🎓 Match Score: {match['match_score']}")
        st.progress(match['match_score'] / 100)
        if st.button(f"Download PDF for {match['school_name']}"):
            st.markdown(f"[📄 View PDF](output/{match['pdf_filename']})", unsafe_allow_html=True)

# Run Lisa's dashboard logic
show_lisa_dashboard()
