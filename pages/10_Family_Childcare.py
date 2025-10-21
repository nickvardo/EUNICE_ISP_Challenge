# pages/10_Family_Childcare.py
from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]  # πάει δύο πάνω από /pages/
CONTENT = APP_DIR / "content"

def read_md(name: str) -> str:
    return (CONTENT / name).read_text(encoding="utf-8")

st.set_page_config(page_title="Family & Childcare", layout="wide")
st.title("Family & Childcare")
st.markdown(read_md("family_childcare.md"))
