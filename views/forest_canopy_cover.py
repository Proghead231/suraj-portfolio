import streamlit as st
from utils import inject_custom_css

inject_custom_css()

st.title("🌲 Forest Canopy Cover Estimation")
st.markdown("An interactive application to estimate forest canopy cover using satellite imagery.")
st.markdown("[View Full GEE App ↗](https://joshisur231.users.earthengine.app/view/fcc)")

st.iframe("https://joshisur231.users.earthengine.app/view/fcc", height=700)
