
import json
from datetime import datetime
from pathlib import Path

def load_profile():
    with open("data/progress/shared_progress.json") as f:
        return json.load(f)

def save_alert(message):
    alert_path = Path("data/alerts/bill_clear_alert.json")
    alert_path.parent.mkdir(parents=True, exist_ok=True)
    with open(alert_path, "w") as f:
        json.dump({
            "status": message,
            "timestamp": str(datetime.now()),
            "trigger_tag": "profile_verified",
            "assigned_agent": "Bill"
        }, f, indent=2)

def send_email(subject, body):
    print(f"[EMAIL] Subject: {subject}\n\n{body}\n")

def send_sms(message):
    print(f"[SMS] {message}\n")

def main():
    required_fields = [
        "name", "email", "sport", "gpa", "graduation_year", "position",
        "height", "weight", "region", "preferred_location", "goals",
        "sat_score", "act_score", "intended_major", "academic_interest_level",
        "ncaa_id", "naia_id", "transcript_uploaded", "compliance_forms_signed"
    ]

    profile = load_profile()
    all_verified = all(profile.get(field) for field in required_fields)

    if all_verified:
        save_alert("✅ All required profile fields have been completed.")

        if profile.get("bill_alert_email"):
            subject = "✅ Profile Verified – You're Mission Ready"
            body = (
                "🛡️ This is Agent Bill reporting in.\n\n"
                "I have reviewed your recruiting profile, and I am pleased to report that all required fields are now complete.\n\n"
                "This means your support team can operate at full capacity, and your opportunities for exposure are now optimized.\n\n"
                "If you update any key information (SAT/ACT, transcript, or eligibility forms), I will rerun diagnostics automatically.\n\n"
                "Stay sharp.\n\n– Bill, System Manager (a.k.a. The General)"
            )
            send_email(subject, body)

        if profile.get("bill_alert_sms"):
            send_sms("✅ Agent Bill confirms your profile is verified. Your team is mission-ready. Stay sharp.")

        if profile.get("bill_alert_popup"):
            print("[DASHBOARD POPUP] ✅ All profile fields complete. Agent Bill approves.")

if __name__ == "__main__":
    main()


def cleanup_old_reports(directory, retention_days=90):
    now = time.time()
    cutoff = now - (retention_days * 86400)

    for file in Path(directory).glob("bill_*.txt"):
        if file.is_file() and file.stat().st_mtime < cutoff:
            print(f"[AUTO DELETE] Removing old report: {file.name}")
            alert_log_path = Path("data/alerts/deletion_log.txt")
            with open(alert_log_path, "a") as alert_log:
                alert_log.write(f"{datetime.now()} - Deleted: {file.name}\n")
            file.unlink()


    print("[REVIEW] Bill triggered a 30-day review cycle for all reports.")

    # Determine system status
    missing_fields = [field for field in required_fields if not profile.get(field)]
    if not missing_fields:
        system_status = 'GREEN'
    elif len(missing_fields) <= 3:
        system_status = 'YELLOW'
    else:
        system_status = 'RED'

    # Save or display the system status
    status_file = Path("data/alerts/system_status.txt")
    status_file.parent.mkdir(parents=True, exist_ok=True)
    with open(status_file, "w") as f:
        f.write(f"System Status: {system_status}\nMissing Fields: {missing_fields if missing_fields else 'None'}\n")
    print(f"[STATUS] System flagged as {system_status}")
        cleanup_old_reports('agents/bill/reports')



st.markdown("### 📜 Access Log (Mobile Dashboard)")
log_path = Path("data/alerts/access_log.txt")
if log_path.exists():
    logs = log_path.read_text().splitlines()
    for entry in reversed(logs[-10:]):
        st.code(entry)
else:
    st.info("No login attempts logged yet.")
