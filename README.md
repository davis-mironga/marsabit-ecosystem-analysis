# The Marsabit Footprint

**Spatio-Temporal Machine Learning and Spatial Econometric Analysis of Vegetation Dynamics in Marsabit County, Kenya (1990–2024)**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Research Question

Is vegetation change in Marsabit County driven by livestock pressure or climate variability — and where does livestock pressure matter most?

Marsabit County covers approximately 70,000 km² in northern Kenya, encompassing montane forest, extensive rangelands, wetlands, and the Chalbi Desert. Pastoralism is central to local livelihoods, but separating vegetation loss caused by grazing pressure from change driven by climate variability has remained a persistent scientific and policy challenge. This project addresses that question through a four-notebook analytical pipeline combining remote sensing, machine learning, spatial statistics, and spatial econometrics across 34 years of satellite data.

---

## Repository Structure

```
marsabit-ecosystem-analysis/
│
├── 01_GEE_Data_Preprocessing.ipynb   # Satellite processing, NDVI, initial LCI layer
├── 02_LULC_Classification.ipynb      # Random Forest land cover classification
├── 03_Spatial_Analysis.ipynb         # Moran's I, LISA, distance-decay, full LCI
├── 04_Regression_Modeling.ipynb      # OLS, GWR, vulnerability map
│
├── App/
│   ├── app.py                        # Streamlit dashboard
│   └── app_README.md                 # Dashboard documentation
│
├── data/                             # Input data (see sources below)
├── outputs/                          # Generated figures and exports
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## Analytical Pipeline

### Notebook 1 — GEE Data Preprocessing

Processes Landsat 5, 8, and 9 imagery across five time periods (1990, 2000, 2010, 2020, 2024). Computes NDVI composites and change layers, CHIRPS rainfall aggregates, SRTM elevation surfaces, and the distance-to-water component of the Livestock Concentration Index using JRC Global Surface Water.

**Key output:** 13 GEE raster assets exported to `projects/mironga-project-marsabit/assets/marsabit/`

---

### Notebook 2 — LULC Classification

Trains a Random Forest classifier on six spectral and terrain features to produce five-class land cover maps for all five time periods. Classification quality is validated against a held-out test set.

**Key results:**
- Overall Accuracy: **97.14%** (target ≥ 85%)
- Kappa Coefficient: **0.9641**
- Land cover classes: Forest, Rangeland, Wetlands, River, Bareland
- Top predictors: NDVI (1st), Elevation (2nd)

**Key output:** 5 GEE assets (LULC maps: 1990, 2000, 2010, 2020, 2024)

---

### Notebook 3 — Spatial Analysis

Tests whether vegetation degradation is spatially random or clustered, identifies hotspot and stable-zone locations, quantifies the livestock impact radius from water points, and constructs the full Livestock Concentration Index.

**Approach:** GEE handles all raster operations; spatial statistics (Moran's I, LISA) are computed in Python using PySAL/esda, which requires sampling pixel values onto a grid and building a spatial weights matrix.

**Key results:**
- Global Moran's I: **0.2288** (Z = 16.01, p < 0.0001) — significant positive clustering
- LISA High-High hotspots: **123 locations**, concentrated in eastern and southern Marsabit
- LISA Low-Low stable zones: **176 locations**, concentrated in western Marsabit
- Distance-decay threshold: approximately **18 km** from permanent water points
- LCI constructed with α = 0.6 (water proximity) + β = 0.4 (settlement density)
- LCI is robust across three weighting schemes (sensitivity analysis confirmed)

**LCI data sources:**
- Water component: JRC Global Surface Water v1.4, occurrence ≥ 10% — the ≥ 50% permanent-water threshold is too sparse for Marsabit's arid conditions; the ≥ 10% threshold captures seasonal luggas, boreholes, and ephemeral water that livestock actually use
- Settlement component: CIESIN GPWv4.11 population density, 2020 epoch

**Key output:** 4 GEE assets (lci_full, lci_water_fresh, lci_settlement, lisa_hotspots)

---

### Notebook 4 — Regression Modeling

Estimates OLS and Geographically Weighted Regression (GWR) models of the livestock-vegetation relationship, formally tests for spatial non-stationarity, and produces a four-class vulnerability map for policy use.

**Regression equation:**
```
NDVI_change = β₀ + β₁(LCI) + β₂(Rainfall_change) + β₃(Elevation) + ε
```

**Key results:**

| Metric | OLS | GWR |
|--------|-----|-----|
| R-squared | 0.1288 | 0.3690 |
| AIC | −10,604.53 | −12,044.91 |
| AIC improvement | — | +1,440 points |
| LCI coefficient | p = 0.054 (not significant globally) | Negative at 63.7% of locations |
| Residual Moran's I | 0.3027 (p < 0.0001) | Confirms spatial non-stationarity; GWR justified |

**Vulnerability map:** 611 Critical locations (~1.53 million ha), concentrated in eastern and central Marsabit rangelands.

---

## Six Key Findings

1. Marsabit County has net greened since 1990 (mean NDVI change = +0.0643), but this county-wide average conceals pronounced spatial heterogeneity.
2. Vegetation degradation is spatially clustered, not random (Moran's I = 0.2288, p < 0.0001).
3. Livestock impact extends approximately 18 km from permanent water points — the effective radius for grazing pressure on vegetation.
4. GWR decisively outperforms OLS (ΔR² = +0.24, ΔAIC = +1,440), confirming that the livestock-vegetation relationship varies significantly across space.
5. The LCI is negatively associated with vegetation recovery at 63.7% of sampled locations, concentrated in eastern Marsabit.
6. Rangeland is the most vulnerable land cover class, accounting for 352 of 611 Critical vulnerability locations.

---

## Policy Recommendations

1. Establish grazing exclusion or regulated-use zones within 5 km of permanent water points in eastern and southern Marsabit, where LISA hotspots and negative LCI coefficients overlap.
2. Target restoration programmes at the 611 Critical vulnerability locations (~1.53 million ha) identified by the GWR vulnerability map.
3. Designate the 123 LISA High-High hotspot locations as permanent ecological monitoring sites for ongoing degradation tracking.
4. Apply the 18 km impact radius as a minimum buffer distance in all future borehole and water-point siting decisions.
5. Adopt differentiated spatial policy: active intervention in eastern Marsabit where livestock pressure dominates; conservation and low-impact land management in western Marsabit where vegetation is stable.

---

## GEE Asset Inventory

All assets stored at: `projects/mironga-project-marsabit/assets/marsabit/`

| Notebook | Assets | Count |
|----------|--------|-------|
| Notebook 1 | ndvi_1990, ndvi_2000, ndvi_2010, ndvi_2020, ndvi_2024, ndvi_change_1990_2000, ndvi_change_2000_2010, ndvi_change_2010_2020, ndvi_change_2020_2024, ndvi_change_total, rainfall_change, elevation, lci_distance | 13 |
| Notebook 2 | lulc_1990, lulc_2000, lulc_2010, lulc_2020, lulc_2024 | 5 |
| Notebook 3 | lci_full, lci_water_fresh, lci_settlement, lisa_hotspots | 4 |
| **Total** | | **22** |

---

## Data Sources

| Dataset | Source | Resolution | Used for |
|---------|--------|------------|---------|
| Landsat 5, 8, 9 | USGS / Google Earth Engine | 30 m | NDVI time series and land cover classification |
| CHIRPS Rainfall | Climate Hazards Group | 5 km | Climate control variable (X₂) |
| JRC Global Surface Water v1.4 | EC Joint Research Centre | 30 m | Water proximity component of LCI |
| GPW Population Density v4.11 | CIESIN | 1 km | Settlement density component of LCI |
| SRTM Digital Elevation Model | NASA / USGS | 30 m | Terrain control variable (X₃) |
| FAO GAUL Level 2 | FAO / GEE | — | Marsabit County boundary |

---

## How to Run

### Requirements

```bash
pip install -r requirements.txt
```

### Google Earth Engine authentication

All four notebooks require a GEE account authenticated to the project `mironga-project-marsabit`. Update the `project` argument in `ee.Initialize()` in each notebook if running under a different GEE project.

### Notebook execution order

Notebooks must be run in sequence. Each depends on GEE assets exported by the previous notebook.

```
01_GEE_Data_Preprocessing
        ↓
02_LULC_Classification
        ↓
03_Spatial_Analysis
        ↓
04_Regression_Modeling
```

Allow GEE export tasks to reach **SUCCEEDED** status before proceeding to the next notebook. Monitor at: `console.cloud.google.com/earth-engine/tasks?project=mironga-project-marsabit`

### Streamlit dashboard

```bash
streamlit run App/app.py
```

---

## Interpretation Note

All results in this study report statistical associations, not causal relationships. A negative LCI coefficient means that higher livestock concentration is associated with lower vegetation recovery after controlling for rainfall and elevation — not that livestock definitively cause vegetation loss. Field validation is recommended before implementing exclusion or restriction policies.

---

## Live Dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://davis-mironga-marsabit-ecosystem-analysis-appapp-hcvf7e.streamlit.app)

Explore the interactive dashboard — NDVI trends, spatial clustering, distance-decay analysis, regression results, vulnerability map, and policy recommendations.

---

## Author

**Davis Mironga**
Marsabit Ecosystem Analysis, 2026

---

## License

MIT License — free to use with attribution.
