from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
CONTENT = APP_DIR / "content"

def read_md(name: str) -> str:
    return (CONTENT / name).read_text(encoding="utf-8")

st.set_page_config(page_title="Relocation FAQ", layout="wide")
st.title("Relocation FAQ")
st.markdown(read_md("faq.md"))

st.divider()
st.subheader("Voices from Newcomers")
st.markdown((CONTENT / "testimonials.md").read_text(encoding="utf-8"))
