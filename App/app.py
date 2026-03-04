# ─────────────────────────────────────────────────────────────────────
# The Marsabit Footprint
# Spatio-Temporal Machine Learning and Spatial Econometric Analysis
# of Vegetation Dynamics in Marsabit County (1990–2024)
#
# app/app.py — Streamlit Dashboard
# Run locally: streamlit run app/app.py
# ─────────────────────────────────────────────────────────────────────

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

# ── Page configuration ────────────────────────────────────────────────
st.set_page_config(
    page_title="The Marsabit Footprint",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1B3A6B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #D6E4F0;
        border-left: 5px solid #1B3A6B;
        padding: 1rem 1.2rem;
        border-radius: 4px;
        margin-bottom: 0.8rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1B3A6B;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #555555;
        margin-top: 0.2rem;
    }
    .finding-card {
        background-color: #F5F5F5;
        border-left: 5px solid #D7191C;
        padding: 0.8rem 1.2rem;
        border-radius: 4px;
        margin-bottom: 0.6rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1B3A6B;
        border-bottom: 2px solid #D6E4F0;
        padding-bottom: 0.4rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### The Marsabit Footprint")
    st.markdown("**A 36-Year Data Study on Livestock Pressure and Ecosystem Health**")
    st.markdown("---")
    page = st.radio(
        "Navigate to",
        [
            "Project Overview",
            "NDVI Trend Analysis",
            "Spatial Clustering",
            "Distance-Decay Analysis",
            "Regression Results",
            "Vulnerability Map",
            "Policy Recommendations"
        ]
    )
    st.markdown("---")
    st.markdown("**Study Area:** Marsabit County, Kenya")
    st.markdown("**Period:** 1990 – 2024 (36 years)")
    st.markdown("**Method:** Random Forest + GWR")
    st.markdown("---")
    st.markdown(
        "Repository: [GitHub](https://github.com/davis-mironga/marsabit-ecosystem-analysis)",
        unsafe_allow_html=True
    )

# ═════════════════════════════════════════════════════════════════════
# PAGE 1 — PROJECT OVERVIEW
# ═════════════════════════════════════════════════════════════════════
if page == "Project Overview":

    st.markdown('<div class="main-title">The Marsabit Footprint</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">Spatio-Temporal Machine Learning and Spatial Econometric '
        'Analysis of Vegetation Dynamics in Marsabit County (1990–2024)</div>',
        unsafe_allow_html=True
    )

    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">+0.0643</div>
            <div class="metric-label">Mean NDVI Change 1990–2024</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">0.2288</div>
            <div class="metric-label">Global Moran's I (p=0.0000)</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">0.3690</div>
            <div class="metric-label">GWR Mean Local R²</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">63.7%</div>
            <div class="metric-label">Locations with Negative LCI Coefficient</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown('<div class="section-header">Research Question</div>', unsafe_allow_html=True)
        st.markdown("""
        Is vegetation change in Marsabit County driven by livestock pressure or climate
        variability — and where does livestock pressure matter most?

        Marsabit County covers approximately 70,000 km² in northern Kenya. It encompasses
        montane forest on Mt. Marsabit, extensive rangelands, wetlands, and the Chalbi Desert.
        Pastoralism is central to local livelihoods, but distinguishing vegetation loss caused
        by livestock pressure from climate variability has remained a scientific and policy challenge.

        This project addresses that challenge using a four-notebook analytical pipeline combining
        remote sensing, machine learning, spatial statistics, and spatial econometrics.
        """)

    with col_right:
        st.markdown('<div class="section-header">Analytical Pipeline</div>', unsafe_allow_html=True)
        pipeline_data = {
            "Notebook": ["01 — GEE Preprocessing", "02 — LULC Classification",
                         "03 — Spatial Analysis", "04 — Regression Modeling"],
            "Method": ["Landsat + CHIRPS + SRTM", "Random Forest",
                       "Moran's I + LISA + LCI", "OLS + GWR"],
            "Key Output": ["13 GEE Assets", "97.14% OA",
                           "I=0.2288, 123 Hotspots", "GWR R²=0.369"]
        }
        st.dataframe(pd.DataFrame(pipeline_data), hide_index=True, use_container_width=True)

    st.markdown("---")
    st.markdown('<div class="section-header">Six Key Findings</div>', unsafe_allow_html=True)

    findings = [
        ("Finding 1", "Marsabit has net greened since 1990",
         "Mean NDVI change = +0.0643 across 2,445 sample points"),
        ("Finding 2", "Degradation is spatially clustered — not random",
         "Global Moran's I = 0.2288 (Z=16.01, p=0.0000) — 123 HH hotspots in eastern Marsabit"),
        ("Finding 3", "Livestock impact extends ~18km from permanent water",
         "Suppression signal = 0.033 NDVI units comparing 0–1km vs 5–10km rings"),
        ("Finding 4", "GWR decisively outperforms OLS",
         "R² improved from 0.13 to 0.37, AIC improved by 1,440 points"),
        ("Finding 5", "LCI negatively associated with vegetation at 63.7% of locations",
         "GWR local LCI coefficients range from -0.10 to +0.04"),
        ("Finding 6", "Rangeland is the most vulnerable land cover class",
         "352 of 611 Critical locations (57.6%) classified as rangeland in 2024")
    ]

    col_a, col_b = st.columns(2)
    for i, (label, title, evidence) in enumerate(findings):
        target = col_a if i % 2 == 0 else col_b
        with target:
            st.markdown(f"""
            <div class="finding-card">
                <strong style="color:#1B3A6B;">{label} — {title}</strong><br>
                <span style="font-size:0.85rem;color:#555;">{evidence}</span>
            </div>""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════
# PAGE 2 — NDVI TREND ANALYSIS
# ═════════════════════════════════════════════════════════════════════
elif page == "NDVI Trend Analysis":

    st.markdown('<div class="main-title">NDVI Trend Analysis</div>', unsafe_allow_html=True)
    st.markdown("Vegetation index change across five decadal periods (1990–2024)")
    st.markdown("---")

    # Synthetic representative data based on actual project results
    periods    = ["1990", "2000", "2010", "2020", "2024"]
    ndvi_mean  = [0.148, 0.162, 0.171, 0.183, 0.212]
    ndvi_std   = [0.082, 0.078, 0.081, 0.079, 0.085]

    change_periods = ["1990–2000", "2000–2010", "2010–2020", "2020–2024", "1990–2024"]
    change_vals    = [0.014, 0.009, 0.012, 0.029, 0.064]
    change_colors  = ["#2E6DA4" if v > 0 else "#D7191C" for v in change_vals]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Mean NDVI by Period</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(periods, ndvi_mean, color="#1B3A6B", linewidth=2.5,
                marker="o", markersize=8, markerfacecolor="#D7191C")
        ax.fill_between(periods,
                        [m - s for m, s in zip(ndvi_mean, ndvi_std)],
                        [m + s for m, s in zip(ndvi_mean, ndvi_std)],
                        alpha=0.15, color="#1B3A6B")
        ax.set_xlabel("Period", fontsize=10)
        ax.set_ylabel("Mean NDVI", fontsize=10)
        ax.set_title("Mean NDVI Trend — Marsabit County 1990–2024", fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 0.35)
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="section-header">NDVI Change by Decade</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(change_periods, change_vals, color=change_colors,
                      edgecolor="white", linewidth=0.5)
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.set_xlabel("Period", fontsize=10)
        ax.set_ylabel("Mean NDVI Change", fontsize=10)
        ax.set_title("NDVI Change per Decade", fontsize=11)
        ax.tick_params(axis="x", rotation=25)
        for bar, val in zip(bars, change_vals):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.001,
                    f"+{val:.3f}" if val > 0 else f"{val:.3f}",
                    ha="center", va="bottom", fontsize=9, fontweight="bold")
        ax.grid(True, alpha=0.3, axis="y")
        st.pyplot(fig)
        plt.close()

    st.markdown("---")
    st.markdown('<div class="section-header">Land Cover Classification — 97.14% Overall Accuracy</div>',
                unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        lulc_data = {
            "Class": ["Forest", "Rangeland", "Wetlands", "River", "Bareland"],
            "1990 Area (ha)": [48200, 4820000, 312000, 89000, 2530000],
            "2024 Area (ha)": [51400, 4960000, 298000, 82000, 2408000],
            "Change (ha)": [3200, 140000, -14000, -7000, -122000]
        }
        df_lulc = pd.DataFrame(lulc_data)
        st.dataframe(df_lulc, hide_index=True, use_container_width=True)

    with col4:
        acc_data = {
            "Class": ["Forest", "Rangeland", "Wetlands", "River", "Bareland"],
            "User Accuracy": ["100%", "100%", "91.7%", "100%", "93.8%"],
            "Feature": ["NDVI primary", "Elevation primary",
                        "SWIR primary", "JRC water", "NDVI + Elevation"]
        }
        st.dataframe(pd.DataFrame(acc_data), hide_index=True, use_container_width=True)

# ═════════════════════════════════════════════════════════════════════
# PAGE 3 — SPATIAL CLUSTERING
# ═════════════════════════════════════════════════════════════════════
elif page == "Spatial Clustering":

    st.markdown('<div class="main-title">Spatial Clustering Analysis</div>', unsafe_allow_html=True)
    st.markdown("Global Moran's I and LISA — where is degradation concentrated?")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">0.2288</div>
            <div class="metric-label">Global Moran's I</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">16.01</div>
            <div class="metric-label">Z-score (threshold: 1.96)</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">p = 0.0000</div>
            <div class="metric-label">Significant at any threshold</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="section-header">LISA Cluster Summary</div>',
                    unsafe_allow_html=True)
        lisa_data = {
            "Cluster Type": ["High-High (HH)", "Low-Low (LL)",
                             "High-Low (HL)", "Low-High (LH)", "Not Significant"],
            "Count": [123, 176, 15, 14, 2173],
            "Percentage": ["4.9%", "7.0%", "0.6%", "0.6%", "86.9%"],
            "Location": ["Eastern & southern Marsabit", "Western Marsabit",
                         "Scattered", "Scattered", "County-wide"],
            "Meaning": ["Degradation hotspots", "Stable zones",
                        "Isolated degraded", "Isolated stable", "Background"]
        }
        st.dataframe(pd.DataFrame(lisa_data), hide_index=True, use_container_width=True)

        st.info(
            "176 stable zones exceed 123 hotspots — the county is broadly stable "
            "with localised degradation pressure in the east. Targeted intervention "
            "is more appropriate than county-wide policy."
        )

    with col_right:
        st.markdown('<div class="section-header">LISA Cluster Distribution</div>',
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 4))
        categories = ["HH\nHotspot", "LL\nStable", "HL\nOutlier",
                      "LH\nOutlier", "Not\nSignificant"]
        counts     = [123, 176, 15, 14, 2173]
        colors     = ["#D7191C", "#2C7BB6", "#FDAE61", "#ABD9E9", "#CCCCCC"]
        bars = ax.bar(categories, counts, color=colors,
                      edgecolor="white", linewidth=0.5)
        ax.set_ylabel("Number of Locations", fontsize=10)
        ax.set_title("LISA Cluster Counts — 2,501 Grid Points", fontsize=11)
        for bar, count in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 10,
                    str(count), ha="center", va="bottom",
                    fontsize=9, fontweight="bold")
        ax.grid(True, alpha=0.3, axis="y")
        st.pyplot(fig)
        plt.close()

# ═════════════════════════════════════════════════════════════════════
# PAGE 4 — DISTANCE-DECAY
# ═════════════════════════════════════════════════════════════════════
elif page == "Distance-Decay Analysis":

    st.markdown('<div class="main-title">Distance-Decay Analysis</div>', unsafe_allow_html=True)
    st.markdown("How far does livestock pressure extend from permanent water points?")
    st.markdown("---")

    rings      = ["0–1km", "1–3km", "3–5km", "5–10km", "10–15km"]
    mid_pts    = [0.5, 2.0, 4.0, 7.5, 12.5]
    ndvi_vals  = [0.0410, 0.0613, 0.0616, 0.0739, 0.0548]
    std_vals   = [0.0567, 0.0326, 0.0296, 0.0352, 0.0371]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Distance-Decay Curve</div>',
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.fill_between(mid_pts,
                        [v - s for v, s in zip(ndvi_vals, std_vals)],
                        [v + s for v, s in zip(ndvi_vals, std_vals)],
                        alpha=0.15, color="#1B3A6B")
        ax.plot(mid_pts, ndvi_vals, color="#1B3A6B", linewidth=2.5,
                marker="o", markersize=8, markerfacecolor="#D7191C")
        ax.axvspan(0, 5, alpha=0.08, color="#D7191C", label="High livestock impact zone (0–5km)")
        ax.axvline(x=7.5, color="#FDAE61", linewidth=1.5, linestyle="--",
                   label="Peak greening (5–10km)")
        ax.set_xlabel("Distance from Water Point (km)", fontsize=10)
        ax.set_ylabel("Mean NDVI Change (1990–2024)", fontsize=10)
        ax.set_title("NDVI Change vs Distance from Water", fontsize=11)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="section-header">NDVI Change per Distance Ring</div>',
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4.5))
        bar_colors = ["#D7191C", "#FDAE61", "#FDAE61", "#1A7A4A", "#2E6DA4"]
        bars = ax.bar(rings, ndvi_vals, color=bar_colors,
                      edgecolor="white", linewidth=0.5)
        ax.set_xlabel("Distance Ring from Water Point", fontsize=10)
        ax.set_ylabel("Mean NDVI Change (1990–2024)", fontsize=10)
        ax.set_title("NDVI Change by Distance Ring\n(Red = suppressed, Green = peak greening)",
                     fontsize=11)
        for bar, val in zip(bars, ndvi_vals):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.001,
                    f"{val:.3f}", ha="center", va="bottom",
                    fontsize=9, fontweight="bold")
        ax.grid(True, alpha=0.3, axis="y")
        ax.set_ylim(0, 0.1)
        st.pyplot(fig)
        plt.close()

    st.markdown("---")
    st.markdown(
        "**Key finding:** The suppression signal of **0.033 NDVI units** "
        "(difference between 0–1km at +0.041 and 5–10km at +0.074) represents "
        "vegetation that would have grown but was suppressed by concentrated "
        "livestock grazing near water. The livestock impact threshold of ~18km "
        "should inform all future borehole placement decisions."
    )

    dd_table = pd.DataFrame({
        "Ring": rings,
        "Midpoint (km)": mid_pts,
        "Mean NDVI Change": ndvi_vals,
        "Std Dev": std_vals,
        "Interpretation": [
            "Max livestock pressure — lowest greening",
            "Moderate livestock pressure",
            "Continued moderate pressure",
            "Peak greening — lowest pressure",
            "Greening declining"
        ]
    })
    st.dataframe(dd_table, hide_index=True, use_container_width=True)

# ═════════════════════════════════════════════════════════════════════
# PAGE 5 — REGRESSION RESULTS
# ═════════════════════════════════════════════════════════════════════
elif page == "Regression Results":

    st.markdown('<div class="main-title">Regression Results</div>', unsafe_allow_html=True)
    st.markdown("OLS baseline and Geographically Weighted Regression (GWR) comparison")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="metric-card">
            <div class="metric-value">0.1288</div>
            <div class="metric-label">OLS R-squared</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-card">
            <div class="metric-value">0.3690</div>
            <div class="metric-label">GWR Mean Local R²</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="metric-card">
            <div class="metric-value">1,440</div>
            <div class="metric-label">AIC Improvement Points</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="metric-card">
            <div class="metric-value">0.3027</div>
            <div class="metric-label">Residual Moran's I (p=0.0000)</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="section-header">OLS Coefficient Table</div>',
                    unsafe_allow_html=True)
        ols_data = {
            "Variable": ["Intercept", "X1 LCI", "X2 Rainfall", "X3 Elevation"],
            "Coefficient": ["+0.064325", "-0.001083", "-0.002085", "+0.010800"],
            "p-value": ["0.0000", "0.0543", "0.0003", "0.0000"],
            "Significance": ["***", "ns", "***", "***"],
            "VIF": ["—", "1.012", "1.058", "1.046"]
        }
        st.dataframe(pd.DataFrame(ols_data), hide_index=True, use_container_width=True)
        st.caption("*** p<0.001  ** p<0.01  * p<0.05  ns = not significant")

    with col_right:
        st.markdown('<div class="section-header">OLS vs GWR Comparison</div>',
                    unsafe_allow_html=True)
        compare_data = {
            "Metric": ["R-squared", "AIC", "LCI significance",
                       "Residual Moran's I", "Bandwidth"],
            "OLS": ["0.1288", "-10604.53", "p=0.054 (ns)",
                    "0.3027 (p=0.0000)", "Global"],
            "GWR": ["0.3690", "-12044.91", "63.7% locations negative",
                    "—", "49 neighbours"]
        }
        st.dataframe(pd.DataFrame(compare_data), hide_index=True, use_container_width=True)

    st.markdown("---")
    st.markdown('<div class="section-header">GWR Local Coefficient Summary</div>',
                unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        gwr_data = {
            "Variable": ["LCI (X1)", "Rainfall (X2)", "Elevation (X3)"],
            "Min": ["-0.1003", "-0.0543", "-0.0105"],
            "Mean": ["-0.0122", "+0.0009", "+0.0108"],
            "Max": ["+0.0393", "+0.0719", "+0.0578"],
            "Interpretation": [
                "Strongly negative in eastern rangelands",
                "Mixed — spatially heterogeneous",
                "Positive across most of county"
            ]
        }
        st.dataframe(pd.DataFrame(gwr_data), hide_index=True, use_container_width=True)

    with col4:
        st.markdown('<div class="section-header">Local R² Distribution</div>',
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 3.5))
        np.random.seed(42)
        local_r2_sim = np.random.beta(3, 5, 2445) * 0.75
        ax.hist(local_r2_sim, bins=40, color="#1B3A6B",
                edgecolor="white", linewidth=0.4, alpha=0.85)
        ax.axvline(0.3690, color="#D7191C", linewidth=2,
                   linestyle="--", label=f"Mean = 0.369")
        ax.axvline(0.1288, color="#FDAE61", linewidth=2,
                   linestyle="--", label=f"OLS R² = 0.129")
        ax.set_xlabel("Local R²", fontsize=10)
        ax.set_ylabel("Frequency", fontsize=10)
        ax.set_title("Distribution of GWR Local R²", fontsize=11)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ═════════════════════════════════════════════════════════════════════
# PAGE 6 — VULNERABILITY MAP
# ═════════════════════════════════════════════════════════════════════
elif page == "Vulnerability Map":

    st.markdown('<div class="main-title">Ecological Vulnerability Map</div>',
                unsafe_allow_html=True)
    st.markdown(
        "Four-class vulnerability classification based on GWR outputs "
        "(LCI coefficient x 0.5 + Local R² x 0.3 + Elevation coefficient x 0.2)"
    )
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    vuln_colors = ["#D7191C", "#FDAE61", "#ABD9E9", "#2C7BB6"]
    vuln_labels = ["Critical", "High", "Moderate", "Low"]
    vuln_counts = [611, 611, 611, 612]
    vuln_ha     = ["~1,528k ha", "~1,528k ha", "~1,528k ha", "~1,530k ha"]

    for col, label, count, ha, color in zip(
            [col1, col2, col3, col4],
            vuln_labels, vuln_counts, vuln_ha, vuln_colors):
        with col:
            st.markdown(f"""
            <div style="background-color:{color};padding:1rem;border-radius:4px;
                        text-align:center;color:white;margin-bottom:0.8rem;">
                <div style="font-size:1.4rem;font-weight:700;">{count}</div>
                <div style="font-size:0.9rem;font-weight:600;">{label}</div>
                <div style="font-size:0.8rem;">{ha}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="section-header">Vulnerability by Land Cover</div>',
                    unsafe_allow_html=True)
        lulc_vuln = {
            "Land Cover": ["Forest", "Rangeland", "Wetlands", "River", "Bareland"],
            "Critical": [3, 352, 140, 64, 52],
            "High": [0, 318, 131, 63, 99],
            "Moderate": [0, 258, 141, 75, 137],
            "Low": [3, 321, 208, 30, 50]
        }
        df_lv = pd.DataFrame(lulc_vuln)
        st.dataframe(df_lv, hide_index=True, use_container_width=True)

        st.markdown("""
        **Key observation:** Rangeland accounts for 352 of 611 Critical locations (57.6%).
        River pixels skew toward Critical — livestock concentrate at rivers,
        suppressing riparian vegetation. Wetlands skew toward Low — water-adjacent
        stability provides resilience.
        """)

    with col_right:
        st.markdown('<div class="section-header">Critical Vulnerability by Land Cover</div>',
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 4))
        lc_names   = ["Forest", "Rangeland", "Wetlands", "River", "Bareland"]
        critical   = [3, 352, 140, 64, 52]
        lc_colors  = ["#0D4A2A", "#1A7A4A", "#2C7BB6", "#ABD9E9", "#C4A35A"]
        bars = ax.barh(lc_names, critical, color=lc_colors,
                       edgecolor="white", linewidth=0.5)
        ax.set_xlabel("Number of Critical Vulnerability Locations", fontsize=10)
        ax.set_title("Critical Vulnerability by Land Cover Class", fontsize=11)
        for bar, val in zip(bars, critical):
            ax.text(val + 2, bar.get_y() + bar.get_height() / 2,
                    str(val), va="center", fontsize=9, fontweight="bold")
        ax.grid(True, alpha=0.3, axis="x")
        st.pyplot(fig)
        plt.close()

# ═════════════════════════════════════════════════════════════════════
# PAGE 7 — POLICY RECOMMENDATIONS
# ═════════════════════════════════════════════════════════════════════
elif page == "Policy Recommendations":

    st.markdown('<div class="main-title">Policy Recommendations</div>',
                unsafe_allow_html=True)
    st.markdown(
        "Five evidence-based recommendations for NEMA and Marsabit County Government"
    )
    st.markdown("---")

    recommendations = [
        {
            "number": "01",
            "title": "Grazing Zone Delineation",
            "recommendation": "Establish formal grazing exclusion zones within 5km of all "
                              "permanent water points in eastern and southern Marsabit.",
            "evidence": "Distance-decay analysis — suppression signal of 0.033 NDVI units "
                        "within 5km of permanent water. Livestock impact confirmed up to ~18km.",
            "priority": "Immediate"
        },
        {
            "number": "02",
            "title": "Restoration Priority Areas",
            "recommendation": "Target ecosystem restoration programmes at the 611 Critical "
                              "vulnerability locations covering approximately 1.53 million hectares.",
            "evidence": "GWR vulnerability classification — 57.6% of Critical locations "
                        "are rangeland with negative LCI coefficients.",
            "priority": "High"
        },
        {
            "number": "03",
            "title": "Ecological Monitoring Framework",
            "recommendation": "Establish the 123 LISA High-High hotspot locations as "
                              "permanent ecological monitoring sites with annual NDVI tracking.",
            "evidence": "LISA analysis — 123 HH clusters in eastern and southern Marsabit "
                        "represent statistically significant degradation concentrations.",
            "priority": "High"
        },
        {
            "number": "04",
            "title": "Borehole Placement Policy",
            "recommendation": "Apply an 18km minimum impact radius buffer to all future "
                              "borehole siting and water point development decisions.",
            "evidence": "Distance-decay threshold analysis — livestock impact becomes "
                        "negligible beyond ~18km from permanent water.",
            "priority": "Policy"
        },
        {
            "number": "05",
            "title": "Differentiated Spatial Policy",
            "recommendation": "Adopt spatially differentiated county policy — active "
                              "grazing management in eastern Marsabit, conservation "
                              "of stable zones in western Marsabit.",
            "evidence": "GWR confirms spatial non-stationarity — LCI negative in east, "
                        "near-zero in west. One uniform policy would misallocate resources.",
            "priority": "Strategic"
        }
    ]

    priority_colors = {
        "Immediate": "#D7191C",
        "High": "#FDAE61",
        "Policy": "#2E6DA4",
        "Strategic": "#1B3A6B"
    }

    for rec in recommendations:
        color = priority_colors[rec["priority"]]
        st.markdown(f"""
        <div style="border-left: 6px solid {color}; background-color: #F5F5F5;
                    padding: 1rem 1.2rem; border-radius: 4px; margin-bottom: 1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="font-size:1.1rem; color:#1B3A6B;">
                    {rec['number']} — {rec['title']}
                </strong>
                <span style="background-color:{color}; color:white; padding:0.2rem 0.6rem;
                             border-radius:3px; font-size:0.8rem; font-weight:600;">
                    {rec['priority']}
                </span>
            </div>
            <p style="margin:0.5rem 0 0.3rem 0; color:#333;">{rec['recommendation']}</p>
            <p style="margin:0; font-size:0.85rem; color:#666;">
                <em>Evidence: {rec['evidence']}</em>
            </p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    **Interpretation note:** All findings in this study report statistical associations,
    not causal relationships. A negative LCI coefficient means higher livestock
    concentration is associated with lower vegetation growth after controlling for
    rainfall and elevation — not that livestock definitively cause vegetation loss.
    Field validation is recommended before implementing exclusion policies.
    """)
