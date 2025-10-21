# app.py
from pathlib import Path
from datetime import date, timedelta
import os, socket, subprocess
import streamlit as st

# --- helpers/paths ---
APP_DIR = Path(__file__).resolve().parent
CONTENT = APP_DIR / "content"

def read_md(name: str) -> str:
    return (CONTENT / name).read_text(encoding="utf-8")

def _running_in_streamlit() -> bool:
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        return get_script_run_ctx() is not None
    except Exception:
        return False

# --- page setup ---
st.set_page_config(page_title="Live & Work in Lusatia", layout="wide")

# --- language toggle (απλό placeholder) ---
lang = st.sidebar.selectbox("Language", ["EN", "DE (soon)"], index=0)
if lang.startswith("DE"):
    st.sidebar.info("German content coming soon. Showing English.")

# --- hero / title ---
st.title("ISP • Live & Work in Lusatia")
st.caption("Why here • What we do for you • Start your 90-day plan")

# --- quick CTA row ---
ccta1, ccta2 = st.columns([1,1])
with ccta1:
    st.page_link("pages/40_Plan_Builder.py", label="🧭 Build my 90-day plan", help="Personal relocation steps")
with ccta2:
    st.page_link("pages/30_FAQ.py", label="❓ Relocation FAQ", help="Common questions answered")

st.divider()

# --- highlight badges (γρήγορο μήνυμα) ---
b1, b2, b3, b4 = st.columns(4)
b1.metric("Career", "Modern plants")
b2.metric("Cost of living", "Sensible rents")
b3.metric("Location", "Nature + hubs")
b4.metric("Family", "Childcare paths")

st.divider()

# --- EVP from markdown ---
st.header("Work & Live in Lusatia")
st.markdown(read_md("evp.md"))

st.divider()

# --- Explore short-cards (nav to pages) ---
st.subheader("Explore")
c1, c2, c3 = st.columns(3)
with c1:
    st.page_link("pages/10_Family_Childcare.py", label="Family & Childcare →")
with c2:
    st.page_link("pages/20_Language_Community.py", label="Language & Community →")
with c3:
    st.page_link("pages/30_FAQ.py", label="Relocation FAQ →")

st.info("Tip: All page content shown here comes from the **/content** folder.")

st.divider()

# --- Testimonials (από content/testimonials.md) ---
st.subheader("Voices from Newcomers")
st.markdown(read_md("testimonials.md"))

st.divider()

# --- QR to open on phone (LAN) ---
st.subheader("Open on your phone (same Wi-Fi)")
# προσπαθώ να μαντέψω το LAN URL
port = int(os.environ.get("STREAMLIT_SERVER_PORT", "8501"))
ip = socket.gethostbyname(socket.gethostname())
demo_url = f"http://{ip}:{port}"
st.code(demo_url, language="text")

# Προαιρετικό QR (αν υπάρχει η βιβλιοθήκη qrcode)
try:
    import qrcode
    import io
    img = qrcode.make(demo_url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Scan me", width=180)
except Exception:
    st.caption("Install qrcode to show QR in-page.")

# --- safe F5 runner: only when launched as plain Python ---
if __name__ == "__main__" and not _running_in_streamlit():
    subprocess.run([os.sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)])
