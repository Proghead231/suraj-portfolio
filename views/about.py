import streamlit as st
from utils import inject_custom_css

inject_custom_css()

col1, col2 = st.columns([3, 1])

with col1:
    st.title("Suraj Joshi")
    st.markdown(
        "GIS & Remote Sensing Researcher interested in understanding how "
        "geospatial technologies can be used to characterize vegetation, "
        "monitor long-term ecosystem and land-use dynamics, and uncover "
        "the drivers of environmental change."
    )
    st.markdown("❤️ **Favorite tool:** Google Earth Engine with Python")
    st.markdown(
        "📍 Kathmandu, Nepal &nbsp;|&nbsp; "
        "📧 [joshisur231@gmail.com](mailto:joshisur231@gmail.com) &nbsp;|&nbsp; "
        "💻 [GitHub](https://github.com/Proghead231) &nbsp;|&nbsp; "
        "🔬 [ResearchGate](https://www.researchgate.net/profile/Suraj-Joshi-6)",
        unsafe_allow_html=True,
    )

with col2:
    st.image("images/profile_pic.jpg", width=200)

st.divider()

# ── Skills ────────────────────────────────────────────────────────────────────
st.header("🛠️ Technical Skills")

skills = {
    "Remote Sensing & GIS": [
        "Google Earth Engine", "QGIS", "ArcGIS", "LandTrendr", 
        "OBIA", "Time-Series Analysis",
    ],
    "Programming": [
        "Python", "JavaScript (GEE)",
    ],
    "Machine Learning": [
        "Scikit-learn",
    ],
    "Data & Visualization": [
        "Pandas", "NumPy", "Matplotlib", "Streamlit",
        "GeoPandas", "Rasterio",
    ],
    "Ecosystem Modelling": [
        "InVEST Suite", "Landslide Susceptibility",
        "Groundwater Recharge Modelling",
    ],
}

cols = st.columns(len(skills))
for col, (category, items) in zip(cols, skills.items()):
    with col:
        st.markdown(f"**{category}**")
        badges = " ".join(f'<span class="skill-badge">{s}</span>' for s in items)
        st.markdown(badges, unsafe_allow_html=True)

st.divider()


st.header("🎓 Education")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">MSc. in Geographical Information Science and Systems</div>
    <div class="cv-subtitle">University of Salzburg – UNIGIS Kathmandu | 2018 - 2021</div>
</div>
<div class="cv-card">
    <div class="cv-title">BSc. in Forestry</div>
    <div class="cv-subtitle">Tribhuvan University - Institute of Forestry | 2014 - 2018</div>
</div>
""", unsafe_allow_html=True)

# ── Publications ─────────────────────────────────────────────────────────────
st.header("📄 Publications & Research")

st.subheader("Under Peer Review")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Climatic and non-climatic drivers of rangeland vegetation change in Nepal</div>
    <div class="cv-subtitle">Uttam Babu Shrestha, <b>Suraj Joshi</b><br>
    Preprint, 2026 · <a href="https://doi.org/10.64898/2026.07.09.737421" target="_blank">DOI</a></div>
</div>
<div class="cv-card">
    <div class="cv-title">Groundwater Recharge Potential Prediction using Machine Learning in Karnali Basin</div>
    <div class="cv-subtitle">Sanjita Khanal, <b>Suraj Joshi</b>, Uttam Babu Shrestha, Ram Devi Tachamo-Shah, Kanchan Mani Dixit, Umesh Singh, Deep Narayan Shah</div>
</div>
""", unsafe_allow_html=True)

st.subheader("Peer-Reviewed Publications")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Assessing the Effectiveness of Protected Areas in Nepal for Forests and Biodiversity Conservation</div>
    <div class="cv-subtitle">Uttam Babu Shrestha, <b>Suraj Joshi</b>, Sujata Shrestha, Pashupati Chaudhary, Ram Prasad Chaudhary<br>
    Biological Conservation, 2026 · <a href="https://doi.org/10.1016/j.biocon.2026.111830" target="_blank">DOI</a></div>
</div>

<div class="cv-card">
    <div class="cv-title">Topographic and climatic drivers of elevation-dependent land surface phenology shifts across Nepal's ecoregions</div>
    <div class="cv-subtitle">Jeevan Prakash Katel, Uttam Babu Shrestha, <b>Suraj Joshi</b><br>
    International Journal of Biometeorology, 2026 · <a href="https://doi.org/10.1007/s00484-026-03209-1" target="_blank">DOI</a></div>
</div>

<div class="cv-card">
    <div class="cv-title">Livelihood vulnerability and human wildlife conflict in Nepal's lowland protected areas</div>
    <div class="cv-subtitle">Sujata Shrestha, Uttam Babu Shrestha, Prience Shrestha, <b>Suraj Joshi</b><br>
    Global Ecology and Conservation, 2026 · <a href="https://doi.org/10.1016/j.gecco.2025.e04029" target="_blank">DOI</a></div>
</div>

<div class="cv-card">
    <div class="cv-title">Breeding Habitat Suitability Modeling of White-rumped Vulture (<i>Gyps bengalensis</i>) in Proximity to Vulture Restaurants in Central Low Land of Nepal</div>
    <div class="cv-subtitle">Nishan Baral, <b>Suraj Joshi</b>, Nitant Rai, Ankit Bilash Joshi, Kiran Poudel, Shailendra Kumar Yadav<br>
    Frontiers in Conservation Science, 2025 · <a href="https://doi.org/10.3389/fcosc.2025.1645493" target="_blank">DOI</a></div>
</div>

<div class="cv-card">
    <div class="cv-title">Monitoring and Assessing Urbanization Progress in Thailand between 2000 and 2020 using SDG Indicator 11.3.1</div>
    <div class="cv-subtitle">Roshan Bhandari, Wenchao Xue, Salvatore G.P. Virdis, Ekbordin Winijkul, Thi Phuoc Lai Nguyen, <b>Suraj Joshi</b><br>
    Sustainability, 2023 · <a href="https://doi.org/10.3390/su15129794" target="_blank">DOI</a></div>
</div>

<div class="cv-card">
    <div class="cv-title">Land Use/Land Cover (LULC) Change in Suburb of Central Himalayas: A Study from Chandragiri, Kathmandu</div>
    <div class="cv-subtitle"><b>Suraj Joshi</b>, Nitant Rai, Rijan Sharma, Nishan Baral<br>
    Journal of Forest and Environmental Science, 2021 · <a href="https://doi.org/10.7747/JFES.2021.37.1.44" target="_blank">DOI</a></div>
</div>
""", unsafe_allow_html=True)

st.subheader("Technical Report")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Rangeland Management Strategy and Action Plan of Karnali Province, Nepal</div>
    <div class="cv-subtitle">Uttam Babu Shrestha, Bharat Babu Shrestha, Sujata Shrestha, Uma Dhungel, <b>Suraj Joshi</b>, Sanjita Khanal, Nishan Baral, Tulasa Chaudhary, Jeevan Prakash Katel, Anuja Shrestha<br>
    Ministry of Industry, Tourism, Forest and Environment, 2026, Karnali Province · <a href="https://doi.org/10.13140/RG.2.2.14536.07686" target="_blank">DOI</a></div>
</div>
""", unsafe_allow_html=True)

st.subheader("Ongoing Research")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Identifying Spatial Pattern of Agricultural Land Abandonment in Nepal</div>
    <div class="cv-subtitle">Developing a method in Google Earth Engine and Python that integrates Object-Based Image Analysis (OBIA) and Random Forest classification with the LandTrendr algorithm to detect structural breaks and temporal shifts in agricultural land-use across a 22-year time series.</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Experience ───────────────────────────────────────────────────────────────
st.header("💼 Employment")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Research Associate</div>
    <div class="cv-subtitle">Global Institute for Interdisciplinary Studies | July 2023 - Present</div>
    <ul>
        <li>Lead advanced geospatial analyses, machine learning workflows, and time-series analysis for funded environmental projects.</li>
        <li>Analyzed rangeland dynamics and their drivers in Karnali province for multiple funded projects using remote sensing and statistical methods.</li>
        <li>Engineered automated data pipelines using Python and Google Earth Engine to build a Community Forest Vulnerability Index, integrating socio-economic records with multi-decadal climate and fire trends.</li>
        <li>Developed Google Earth Engine workflow to extract and process 70+ years of climate data for the RES-WASH project.</li>
        <li>Developed machine learning models in Google Earth Engine to map groundwater recharge potential zones in Karnali province.</li>
        <li>Modeled key ecosystem services for the nation of Nauru using InVEST suite to support ecosystem restoration and policy development.</li>
        <li>Designed and delivered training workshops to government officials on GIS, remote sensing, Google Earth Engine, and QGIS.</li>
        <li>Produced publication-quality maps and visualizations supporting multiple peer-reviewed studies and technical reports.</li>
        <li>Deployed a Linux-based central server to provide centralized data storage and secure access for staff.</li>
        <li>Developed various geospatial applications to support ongoing projects.</li>
    </ul>
</div>

<div class="cv-card">
    <div class="cv-title">Freelance GIS / Remote Sensing Analyst</div>
    <div class="cv-subtitle">Various Organizations | October 2018 - July 2023</div>
    <ul>
        <li><b>Government Forest Mapping Project</b> (NRM Consulting, 2023): Identified and mapped government-managed forest in Makawanpur and Rasuwa districts of Nepal.</li>
        <li><b>Bagmati River Basin Improvement Project</b> (WWN Nepal / BRBIP, 2023): Provided geospatial expertise to support the forest inventory and planning phase for the Nagmati reservoir construction.</li>
        <li><b>Assessment of Trees Outside Forest in Bagmati Province</b> (Shilanidevi Green Eyes Nepal, 2022): Developed a novel geospatial workflow using morphological filtering to rapidly distinguish individual and small-scale tree stands from large forest blocks using global land cover dataset.</li>
        <li><b>Landslide Susceptibility Analysis in Bangad Kupinde Municipality</b> (Initiative for Nature Utilization, 2021-2022): Assessed landslide susceptibility using geospatial overlay method and analytical hierarchical process.</li>
        <li><b>Tourism Management and Operational Plan</b> (Popular Environment Consultancy, 2020-2021): Mapped potential tourism sites and community forest boundaries; assisted in community forest inventory.</li>
        <li><b>Identification of Suitable Sites for Non-timber Forest Products</b> (Shilanidevi Green Eyes Nepal, 2019): Identified suitable sites using geospatial suitability modelling.</li>
        <li><b>Integrated Urban Development Planning Project</b> (Shilanidevi Green Eyes Nepal, 2018-2019): Performed multi-hazard susceptibility modelling (landslide, flood, drought); delineated watersheds and stream networks using DEMs.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("🎓 Certification")
st.markdown("""
<div class="cv-card">
    <div class="cv-title">Machine Learning with Python- Zero to GBMs (2023) <a href="https://doi.org/10.3389/fcosc.2025.1645493" target="_blank">Certificate</a></div>
</div>
<div class="cv-card">
    <div class="cv-title">Learning Pix4D Drone Mapping- LinkedIn Learning (2022) <a href="https://www.linkedin.com/learning/certificates/a00b8b8afb63ba17b33b35af3b4ec1679847f6c54d0a89a76325ee1eaccc6d53?contentTrackingId=Bw8lIj%2F6Ss6PDi2xfbIH7w%3D%3D&viewName=premium-nav-upsell-text&upsellOrderOrigin=Tracking%3Av1%3Apremium_nav_upsell_text%3ANav%3AIn-Product" target="_blank">Certificate</a></div>
</div>
""", unsafe_allow_html=True)