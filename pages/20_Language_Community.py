from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
CONTENT = APP_DIR / "content"

def read_md(name: str) -> str:
    return (CONTENT / name).read_text(encoding="utf-8")

st.set_page_config(page_title="Language & Community", layout="wide")
st.title("Language & Community")
st.markdown(read_md("language_community.md"))
