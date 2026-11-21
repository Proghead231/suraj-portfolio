import streamlit as st
from utils import inject_custom_css

inject_custom_css()

st.title("📊 Propensity Score Matching")
st.markdown("Upload your CSV data and select variables to perform propensity score matching. The app identifies matched pairs and displays results with visual comparisons before and after matching.")
st.markdown("[View on Hugging Face](https://huggingface.co/spaces/Proghead231/propensity_matching)")

st.iframe("https://proghead231-propensity-matching.hf.space?embed=true", height=700)
