import streamlit as st
import ee
import json
import os

def inject_custom_css():
    """Injects custom CSS to hide Streamlit branding and improve layout."""
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] {visibility: hidden;}
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }
        /* Custom card styling */
        .cv-card {
            background-color: #1e293b;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border: 1px solid #334155;
            transition: border-color 0.2s ease;
        }
        .cv-card:hover {
            border-color: #10b981;
        }
        .cv-title {
            color: #10b981;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
        }
        .cv-subtitle {
            color: #94a3b8;
            font-size: 0.875rem;
            margin-bottom: 0.75rem;
        }
        .cv-subtitle a {
            color: #10b981;
            text-decoration: none;
        }
        .cv-subtitle a:hover {
            text-decoration: underline;
        }
        .cv-card ul {
            color: #cbd5e1;
            padding-left: 1.25rem;
            margin-top: 0;
        }
        .cv-card li {
            margin-bottom: 0.4rem;
            line-height: 1.5;
        }
        /* Skill badge styling */
        .skill-badge {
            display: inline-block;
            background-color: #0f3460;
            color: #10b981;
            border: 1px solid #10b981;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 500;
            margin: 0.2rem 0.15rem;
        }
        </style>
    """, unsafe_allow_html=True)


def initialize_gee():
    """
    Initializes Google Earth Engine.

    Deployment priority:
      1. GOOGLE_APPLICATION_CREDENTIALS env var (points to a key file path)
      2. GEE_SERVICE_ACCOUNT_JSON env var (the full JSON as a string — for Hugging Face / Streamlit Cloud secrets)
      3. Local fallback: looks for the key file next to this utils.py
    """
    if "gee_initialized" in st.session_state and st.session_state.gee_initialized:
        return  # already initialized in this session, skip

    try:
        # --- Method 1: Streamlit Cloud secrets (st.secrets["GEE_SERVICE_ACCOUNT_JSON"]) ---
        # Streamlit Cloud injects secrets into st.secrets, not always into os.environ.
        try:
            key_json_str = st.secrets.get("GEE_SERVICE_ACCOUNT_JSON", "")
        except Exception:
            key_json_str = ""
        if key_json_str:
            key_data = json.loads(key_json_str)
            credentials = ee.ServiceAccountCredentials(key_data["client_email"], key_data=key_data)
            ee.Initialize(credentials)
            st.session_state.gee_initialized = True
            return

        # --- Method 2: env var points to a key file on disk ---
        key_path_env = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
        if key_path_env and os.path.isfile(key_path_env):
            with open(key_path_env, "r") as f:
                key_data = json.load(f)
            credentials = ee.ServiceAccountCredentials(key_data["client_email"], key_path_env)
            ee.Initialize(credentials)
            st.session_state.gee_initialized = True
            return

        # --- Method 3: full JSON in an OS env var ---
        key_json_str = os.environ.get("GEE_SERVICE_ACCOUNT_JSON", "")
        if key_json_str:
            key_data = json.loads(key_json_str)
            credentials = ee.ServiceAccountCredentials(key_data["client_email"], key_data=key_data)
            ee.Initialize(credentials)
            st.session_state.gee_initialized = True
            return

        # --- Method 4: local dev fallback — key file beside utils.py ---
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_key = os.path.join(script_dir, "ee-joshisur231-bd4e20465f61.json")
        if os.path.isfile(local_key):
            with open(local_key, "r") as f:
                key_data = json.load(f)
            credentials = ee.ServiceAccountCredentials(key_data["client_email"], local_key)
            ee.Initialize(credentials)
            st.session_state.gee_initialized = True
            return

        st.error("⚠️ Google Earth Engine credentials not found.")
        st.info(
            "For local dev: place `ee-joshisur231-bd4e20465f61.json` in the project root.\n\n"
            "For deployment: add **`GEE_SERVICE_ACCOUNT_JSON`** to your Streamlit Cloud secrets "
            "(paste the full contents of the key JSON file)."
        )

    except Exception as e:
        st.error(f"Google Earth Engine initialization failed: {e}")
