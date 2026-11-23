import streamlit as st
import ee
import os

os.environ["USE_FOLIUM"] = "1"
import geemap.foliumap as geemap
from streamlit_folium import st_folium
from utils import inject_custom_css, initialize_gee

inject_custom_css()
initialize_gee()


# ── Core algorithm ────────────────────────────────────────────────────────────

def tof(roi, npixels_to_expand_other_classes=3, npixels_to_expand_tof=5,
        npixels_to_expand_forest=8, scale=10, niterations=1):
    """
    Identifies Trees Outside Forest (TOF) using morphological filtering on
    the ESA WorldCover v200 land-cover dataset.

    Returns an image with values:
        1 → Trees Outside Forest (TOF)
        2 → Forest
    """
    lc = ee.ImageCollection("ESA/WorldCover/v200").first().clip(roi)
    # Reclassify: tree cover (class 10) → 1, everything else → 0
    lc_reclassified = lc.remap([10], to=[1], defaultValue=0)
    tree_cover_mask = lc_reclassified.eq(1)
    other_classes_mask = lc_reclassified.eq(0)

    def expand(image_to_expand, npixels_to_expand, expand_value, background_values, roi, scale):
        """Buffer features of a given label value and merge with background features."""
        vectors = image_to_expand.select(0).int8().reduceToVectors(
            geometry=roi, scale=scale, maxPixels=1e10
        )

        def buffer(feature):
            return ee.Feature(feature).buffer(npixels_to_expand * scale, 1)

        vectors_buffer = vectors.filter(ee.Filter.eq("label", expand_value)).map(buffer)

        vectors_merged = ee.FeatureCollection([])
        for bg_val in background_values:
            vectors_merged = vectors_merged.merge(
                vectors.filter(ee.Filter.eq("label", bg_val))
            )

        final_merge = vectors_buffer.merge(vectors_merged)
        expanded_image = final_merge.reduceToImage(["label"], ee.Reducer.first()).clip(roi)
        return expanded_image

    # --- Morphological filtering ---
    expanded_other = expand(other_classes_mask, npixels_to_expand_other_classes, 1, [0], roi, scale)
    add_other_lc = lc_reclassified.add(expanded_other.remap([0, 1], [1, 0]))

    expanded_tof = expand(add_other_lc, npixels_to_expand_tof, 1, [0, 2], roi, scale)
    expanded_forest = expand(expanded_tof, npixels_to_expand_forest, 2, [0, 1], roi, scale)

    for _ in range(niterations - 1):
        expanded_other = expand(expanded_other, npixels_to_expand_other_classes, 1, [0], roi, scale)
        add_other_lc = lc_reclassified.add(expanded_other.remap([0, 1], [1, 0]))
        expanded_tof = expand(add_other_lc, npixels_to_expand_tof, 1, [0, 2], roi, scale)
        expanded_forest = expand(expanded_tof, npixels_to_expand_forest, 2, [0, 1], roi, scale)

    # Mask result to actual tree-covered pixels
    forest_vectors = (
        lc_reclassified.updateMask(tree_cover_mask)
        .select(0).int8()
        .reduceToVectors(geometry=roi, scale=scale, maxPixels=1e10)
    )
    tof_and_forest = expanded_forest.clip(forest_vectors)
    return tof_and_forest


# ── Page header ───────────────────────────────────────────────────────────────

st.title("🌳 Trees Outside Forest Identification")
st.markdown(
    "Uses morphological filtering on the **ESA WorldCover v200** dataset to distinguish "
    "small-scale tree stands (**Trees Outside Forest**) from large contiguous **forest blocks**. "
    "Draw a small area on the map, tune the parameters, and hit **Run Analysis**."
)

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("⚙️ Analysis Parameters")

    with st.expander("📋 How to use", expanded=True):
        st.markdown(
            "1. Use the ✏️ **draw tools** on the map to draw a polygon (ROI).\n"
            "2. Adjust the parameters below.\n"
            "3. Click **▶ Run Analysis**.\n"
            "4. After results appear, use the **layer control** (top-right of map) "
            "to toggle Forest / TOF layers."
        )

    st.warning(
        "⚠️ **Keep the drawn area small.** `reduceToVectors` is computationally intensive "
        "and will hit Earth Engine memory limits for large regions.",
        icon="⚠️",
    )

    st.divider()

    npixels_other = st.slider(
        "Pixels to expand **Other classes**", 1, 10, 3,
        help="Controls how much non-tree area erodes tree patches before TOF detection."
    )
    npixels_tof = st.slider(
        "Pixels to expand **TOF**", 1, 10, 5,
        help="Buffer size used to grow Trees-Outside-Forest candidates."
    )
    npixels_forest = st.slider(
        "Pixels to expand **Forest**", 1, 10, 8,
        help="Buffer size used to grow Forest candidates."
    )
    scale = st.number_input(
        "Scale (m/pixel)", min_value=5, max_value=100, value=10, step=5,
        help="Analysis resolution in metres. 10 m matches the WorldCover native resolution."
    )
    niterations = st.number_input(
        "Iterations", min_value=1, max_value=5, value=1,
        help="Number of morphological filter passes. More iterations refine the boundary but are slower."
    )

    run_btn = st.button("▶ Run Analysis", type="primary", use_container_width=True)

    st.divider()
    st.markdown("**Legend**")
    st.markdown(
        '<span style="color:#22c55e;font-size:1.3rem;">■</span> **Forest**  \n'
        '<span style="color:#3b82f6;font-size:1.3rem;">■</span> **Trees Outside Forest**',
        unsafe_allow_html=True,
    )

# ── Initialise base map (once per session) ────────────────────────────────────

if "tof_map" not in st.session_state:
    m = geemap.Map(center=[27.606, 85.54], zoom=13)
    m.add_basemap("SATELLITE")
    st.session_state.tof_map = m

# ── Run analysis ──────────────────────────────────────────────────────────────

if run_btn:
    # st_folium stores its returned objects in session_state under the widget key
    st_data = st.session_state.get("tof_map_render", {})
    roi = None

    if st_data and st_data.get("last_active_drawing"):
        roi = ee.Geometry(st_data["last_active_drawing"]["geometry"])
    elif st_data and st_data.get("all_drawings"):
        drawings = st_data["all_drawings"]
        if drawings:
            roi = ee.Geometry(drawings[-1]["geometry"])  # use the most-recent drawing

    if roi is None:
        st.error("🗺️ Please **draw a polygon** on the map before running the analysis.")
    else:
        try:
            with st.status("Running Trees Outside Forest analysis...", expanded=True) as status:

                result = tof(
                    roi=roi,
                    npixels_to_expand_other_classes=npixels_other,
                    npixels_to_expand_tof=npixels_tof,
                    npixels_to_expand_forest=npixels_forest,
                    scale=int(scale),
                    niterations=int(niterations),
                )

                # Update status before preparing the map
                status.update(
                    label="Analysis complete. Adding layers to the map...",
                    state="running"
                )

                new_map = geemap.Map(center=[27.6, 85.5], zoom=13)
                new_map.add_basemap("SATELLITE")

                tof_only = result.updateMask(result.eq(1))
                forest_only = result.updateMask(result.eq(2))

                new_map.addLayer(
                    tof_only,
                    {"min": 1, "max": 1, "palette": ["#3b82f6"]},
                    "Trees Outside Forest",
                )

                new_map.addLayer(
                    forest_only,
                    {"min": 2, "max": 2, "palette": ["#22c55e"]},
                    "Forest",
                    shown=True,
                )

                new_map.centerObject(roi, zoom=14)

                st.session_state.tof_map = new_map

                status.update(
                    label="Layers added! Loading the map...",
                    state="complete",
                    expanded=False
                )

            st.success("✅ Analysis complete!")
            st.info("⏳ Please wait while the map layers load. This may take some time for larger areas. Once the layers are visible, use the layer control in the top-right corner of the map to toggle them on or off.")
        except ee.EEException as e:
            st.error(f"**Earth Engine error:** {e}")
            st.info(
                "💡 This usually means the drawn area is too large. "
                "Try drawing a smaller region, or increase the Scale parameter."
            )

        except Exception as e:
            st.error(f"**Unexpected error:** {e}")

# ── Render map ────────────────────────────────────────────────────────────────

try:
    st.session_state.tof_map.add_layer_control()
except Exception:
    pass

st_folium(
    st.session_state.tof_map,
    width="100%",
    height=620,
    key="tof_map_render",
    returned_objects=["last_active_drawing", "all_drawings"],
)
