
import streamlit as st

st.set_page_config(page_title="AI Content Assistant Pro", layout="centered")

st.title("🤖 AI Content Assistant Pro")
st.subheader("Optimizează-ți video-urile pentru TikTok, YouTube și Meta")

with st.form("seo_form"):
    video_title = st.text_input("Titlu video")
    language = st.selectbox("Limbă", ["Română", "Engleză", "Maghiară"])
    generate = st.form_submit_button("Generează SEO")

if generate:
    st.success(f"🔍 SEO generat pentru titlul: '{video_title}' în limba {language}")
    st.write(f"Hashtaguri: #ai #contentcreator #{language.lower()}video")
    st.write(f"Descriere: Acest video te ajută să devii viral pe platformele sociale.")

st.markdown("---")
st.caption("v1.0 • Powered by ChatGPT")
