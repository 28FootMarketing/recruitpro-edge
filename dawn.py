
import streamlit as st
import json
import datetime

st.set_page_config(page_title="💬 Dawn – Emotional Reset Monitor", layout="wide")
st.title("💬 Dawn – Emotional Reset & Mood Monitor")

log_file = "data/moods/mood_log.json"

def load_mood_log():
    try:
        with open(log_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_mood_log(log):
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)

def log_mood(mood, note):
    log = load_mood_log()
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "mood": mood,
        "note": note
    }
    log.append(entry)
    save_mood_log(log)

st.subheader("🧠 How are you feeling today?")
mood = st.radio("Select your current mood:", ["😃 Great", "🙂 Okay", "😐 Meh", "😢 Sad", "😠 Frustrated"])
note = st.text_area("Would you like to share more?", "")

if st.button("Log Mood"):
    log_mood(mood, note)
    st.success("✅ Your mood has been logged.")

st.markdown("---")
st.subheader("📊 Mood History")
log = load_mood_log()
if log:
    for entry in reversed(log[-5:]):
        st.markdown(f"**{entry['timestamp'].split('T')[0]}** – {entry['mood']}")
        if entry["note"]:
            st.markdown(f"📝 {entry['note']}")
        st.markdown("---")
else:
    st.info("No mood entries yet.")

st.info("🔁 Dawn may recommend syncing with Maya, Cheryl, or Bill depending on patterns.")
