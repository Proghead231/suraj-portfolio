# 🌍 Suraj Joshi — Geospatial Portfolio

A Streamlit web application showcasing my research background, publications, and interactive geospatial tools built with Google Earth Engine and Python.

**Live app:** *(link after deployment)*

---

## 📄 Pages

| Page | Description |
|---|---|
| **About Me** | CV summary — education, publications, employment, and technical skills |
| **Trees Outside Forest** | Interactive tool that uses morphological filtering on ESA WorldCover to separate small tree stands from large forest blocks |
| **Forest Canopy Cover** | Embedded GEE app for canopy cover estimation |
| **GEE Downloader** | Streamlit app for downloading GEE datasets (hosted separately on Hugging Face) |
| **Propensity Matching** | Interactive propensity score matching tool (hosted separately on Hugging Face) |

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io) — web framework
- [Google Earth Engine Python API](https://developers.google.com/earth-engine) — geospatial computation
- [geemap](https://geemap.org) — interactive Earth Engine maps
- [streamlit-folium](https://folium.streamlit.app) — Folium map rendering in Streamlit

---

## 🚀 Local Development

### 1. Clone and set up environment

```bash
git clone <your-repo-url>
cd suraj_site
```

Create a conda environment:

```bash
conda create -n gee python=3.11
conda activate gee
pip install -r requirements.txt
```

### 2. Add GEE credentials

Place your Google Earth Engine service account key file in the project root:

```
ee-joshisur231-bd4e20465f61.json   ← never commit this!
```

> ⚠️ This file is excluded by `.gitignore`. Never push it to a public repository.

### 3. Run the app

```bash
streamlit run Home.py
```

---

## ☁️ Deploying to Streamlit Community Cloud

1. Push this repository to GitHub (**without** the `.json` key file).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Set **Main file path** to `Home.py`.
4. Under **Advanced settings → Secrets**, paste:

```toml
GEE_SERVICE_ACCOUNT_JSON = '''
{
  "type": "service_account",
  "project_id": "ee-joshisur231",
  ...paste full contents of your key file here...
}
'''
```

5. Click **Deploy**.

---

## 📁 Project Structure

```
suraj_site/
├── Home.py                  # App entry point & navigation
├── utils.py                 # Shared CSS injection & GEE init
├── requirements.txt
├── .streamlit/
│   └── config.toml          # Theme configuration
├── images/
│   └── profile_pic.jpg
└── views/
    ├── about.py             # About Me / CV page
    ├── trees_outside_forest.py
    ├── forest_canopy_cover.py
    ├── gee_downloader.py
    └── propensity_matching.py
```

---

## 📜 License

MIT — see [LICENSE](LICENSE).
