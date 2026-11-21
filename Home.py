import streamlit as st
from utils import inject_custom_css

# Global page config (must be the first Streamlit command)
st.set_page_config(page_title="Suraj Joshi | Portfolio", page_icon="🌍", layout="wide", initial_sidebar_state="expanded")

# Setup Navigation with sections
pg = st.navigation({
    "": [
        st.Page("views/about.py", title="About Me", icon="👤", default=True),
    ],
    "Geospatial Apps": [
        st.Page("views/trees_outside_forest.py", title="Trees Outside Forest", icon="🌳"),
        st.Page("views/forest_canopy_cover.py", title="Forest Canopy Cover", icon="🌲"),
        st.Page("views/gee_downloader.py", title="GEE Downloader", icon="⬇️"),
        st.Page("views/propensity_matching.py", title="Propensity Matching", icon="📊")
    ]
})

# Run the selected page
pg.run()
