import streamlit as st
from utils import inject_custom_css

inject_custom_css()

st.title("⬇️ Google Earth Engine Downloader")
st.markdown("A Streamlit Web Application for downloading datasets from the Google Earth Engine Database.")
st.markdown("[View on Hugging Face](https://huggingface.co/spaces/Proghead231/GDownloader)")

st.iframe("https://proghead231-gdownloader.hf.space?embed=true", height=700)
