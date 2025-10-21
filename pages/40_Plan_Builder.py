# pages/40_Plan_Builder.py
from datetime import date, timedelta
from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
CONTENT = APP_DIR / "content"

st.set_page_config(page_title="90-Day Plan Builder", layout="wide")
st.title("🧭 Personal 90-Day Relocation Plan")

st.markdown((CONTENT / "plan_builder_intro.md").read_text(encoding="utf-8") if (CONTENT / "plan_builder_intro.md").exists() else "")

# --- inputs ---
col1, col2 = st.columns(2)
with col1:
    has_family = st.selectbox("Coming with family?", ["No", "Yes"]) == "Yes"
    budget = st.slider("Monthly housing budget (€)", 300, 2000, 900, 50)
    shift = st.checkbox("I will work shifts / late hours")
with col2:
    start = st.date_input("Target start date", value=date.today() + timedelta(days=30))
    level = st.selectbox("German level", ["None", "A1", "A2", "B1+"])
    need_childcare = st.checkbox("I need childcare", value=has_family)

st.divider()

# --- plan generation (simple bullets with suggested dates) ---
def step(d, text):
    return f"- **{d.strftime('%Y-%m-%d')}** — {text}"

d0 = start - timedelta(days=30)   # before arrival window
d1 = start                        # arrival
d7 = start + timedelta(days=7)
d14 = start + timedelta(days=14)
d21 = start + timedelta(days=21)
d30 = start + timedelta(days=30)
d60 = start + timedelta(days=60)
d90 = start + timedelta(days=90)

plan = []
plan.append("### Before you arrive (−30…0 days)")
plan += [
    step(d0, "Collect documents: passport, birth/marriage certificates, diplomas."),
    step(d0, "Book temporary housing (short-term)."),
    step(d0, "Pre-book city registration & bank appointments."),
]
if level in ["None", "A1"]:
    plan.append(step(d0, "Enroll to starter German class (even online)."))

plan.append("\n### Week 1 (0…7 days)")
plan += [
    step(d1, "City registration (Anmeldung)."),
    step(d1, "Get SIM card & public transport card."),
    step(d7, "Open bank account (if not online)."),
]
if shift:
    plan.append(step(d7, "Arrange late-night transport route / car-share."))
if need_childcare:
    plan.append(step(d7, "Visit childcare options; start application."))

plan.append("\n### Weeks 2–3 (8…21 days)")
plan += [
    step(d14, "Start long-term housing search (budget ~€" + str(budget) + ")."),
    step(d14, "Book health insurance appointment."),
    step(d21, "Buddy meetup / community event."),
]

plan.append("\n### Month 2 (22…60 days)")
plan += [
    step(d30, "Lease signing & move-in."),
    step(d30, "Register utilities / internet."),
]
if has_family:
    plan.append(step(d30, "School/Kindergarten registration timeline confirmed."))

plan.append("\n### Month 3 (61…90 days)")
plan += [
    step(d60, "Finalize documents (tax ID, payroll, GP registration)."),
    step(d60, "Language checkpoint (A1→A2) & next cohort enrollment."),
    step(d90, "Review: housing settled, transport stable, social circle growing."),
]

# --- show ---
st.subheader("Your plan")
st.markdown("\n".join(plan))

# --- export ---
st.download_button("⬇️ Download as Markdown", data="\n".join(plan), file_name="90_day_plan.md", mime="text/markdown")
