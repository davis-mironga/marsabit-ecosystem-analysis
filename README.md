# The Marsabit Footprint

**Spatio-Temporal Machine Learning and Spatial Econometric Analysis of
Vegetation Dynamics in Marsabit County, Kenya (1990–2024)**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Research Question

Is vegetation change in Marsabit County driven by livestock pressure or
climate variability — and where does livestock pressure matter most?

Marsabit County covers approximately 70,000 km² in northern Kenya and
encompasses montane forest, extensive rangelands, wetlands, and the Chalbi
Desert. Pastoralism is central to local livelihoods, but distinguishing
vegetation loss caused by livestock pressure from climate variability has
remained a scientific and policy challenge. This project addresses that
challenge using a four-notebook analytical pipeline combining remote sensing,
machine learning, spatial statistics, and spatial econometrics over 36 years
of satellite data.

---

## Repository Structure
```
marsabit-ecosystem-analysis/
│
├── 01_GEE_Data_Preprocessing.ipynb   # Satellite processing, NDVI, LCI
├── 02_LULC_Classification.ipynb      # Random Forest land cover maps
├── 03_Spatial_Analysis.ipynb         # Moran's I, LISA, distance-decay, LCI
├── 04_Regression_Modeling.ipynb      # OLS, GWR, vulnerability map
│
├── App/
│   ├── app.py                        # Streamlit dashboard
│   └── app_README.md                 # Dashboard documentation
│
├── data/                             # Input data (see sources below)
├── outputs/                          # Generated outputs
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## Analytical Pipeline

### Notebook 1 — GEE Data Preprocessing
Processes Landsat 5, 8, and 9 imagery across five decadal periods
(1990, 2000, 2010, 2020, 2024). Computes NDVI composites, CHIRPS
rainfall aggregates, SRTM elevation surfaces, and the distance-to-water
component of the Livestock Concentration Index.

**Key output:** 13 GEE assets exported to
`projects/mironga-project-marsabit/assets/marsabit/`

---

### Notebook 2 — LULC Classification
Trains a Random Forest classifier on six spectral and terrain features
to produce five-class land cover maps for all five time periods.

**Key results:**
- Overall Accuracy: **97.14%** (target ≥ 85%)
- Kappa Coefficient: **0.9641**
- Classes: Forest, Rangeland, Wetlands, River, Bareland
- Feature importance: NDVI (1st), Elevation (2nd)

---

### Notebook 3 — Spatial Analysis
Tests whether vegetation degradation is spatially random or clustered,
identifies degradation hotspots, quantifies the livestock impact radius
from water points, and constructs the full Livestock Concentration Index.

**Key results:**
- Global Moran's I: **0.2288** (Z=16.01, p=0.0000) — significant clustering
- LISA High-High hotspots: **123 locations** in eastern and southern Marsabit
- LISA Low-Low stable zones: **176 locations** in western Marsabit
- Distance-decay threshold: **~18km** from permanent water points
- LCI constructed: α=0.6 (water) + β=0.4 (settlement density)

---

### Notebook 4 — Regression Modeling
Estimates OLS and Geographically Weighted Regression (GWR) models of
the livestock-vegetation relationship, formally tests spatial
non-stationarity, and produces a four-class vulnerability map.

**Key results:**

| Metric | OLS | GWR |
|--------|-----|-----|
| R-squared | 0.1288 | 0.3690 |
| AIC | -10604.53 | -12044.91 |
| AIC Improvement | — | +1,440 points |
| LCI significance | p=0.054 (ns globally) | 63.7% locations negative |
| Residual Moran's I | 0.3027 (p=0.0000) | GWR formally justified |

**Vulnerability map:** 611 Critical locations (~1.53M ha) concentrated
in eastern and central Marsabit rangelands.

---

## Six Key Findings

1. Marsabit County has net greened since 1990 (mean NDVI change = +0.0643)
2. Degradation is spatially clustered — not random (Moran's I = 0.2288, p=0.0000)
3. Livestock impact extends ~18km from permanent water points
4. GWR decisively outperforms OLS — relationship is spatially non-stationary
5. LCI is negatively associated with vegetation at 63.7% of locations
6. Rangeland is the most vulnerable land cover class (352/611 Critical locations)

---

## Policy Recommendations

1. Establish grazing exclusion zones within 5km of permanent water points
   in eastern and southern Marsabit
2. Target restoration programmes at 611 Critical vulnerability locations
   (~1.53M ha)
3. Establish 123 LISA High-High hotspot locations as permanent ecological
   monitoring sites
4. Apply 18km impact radius as minimum buffer in all future borehole
   placement decisions
5. Adopt differentiated spatial policy — active intervention in eastern
   Marsabit, conservation in western Marsabit

---

## Data Sources

| Dataset | Source | Resolution | Purpose |
|---------|--------|------------|---------|
| Landsat 5, 8, 9 | USGS / GEE | 30m | Land cover and NDVI |
| CHIRPS Rainfall | Climate Hazards Group | 5km | Climate control variable |
| JRC Global Surface Water | EC Joint Research Centre | 30m | Water point proxy |
| GPW Population Density | CIESIN | 1km | Settlement density proxy |
| SRTM DEM | NASA / USGS | 30m | Elevation and slope |

---

## How to Run

### Requirements
```bash
pip install -r requirements.txt
```

### Google Earth Engine
All four notebooks require a GEE account authenticated to the project
`mironga-project-marsabit`. Update the project ID in each notebook
if running under a different GEE project.

### Notebook order
Run notebooks in sequence — each depends on GEE assets exported
by the previous notebook.
```
01 → 02 → 03 → 04
```

### Streamlit Dashboard
```bash
streamlit run App/app.py
```

---

## Interpretation Note

All findings in this study report statistical associations, not causal
relationships. A negative LCI coefficient means higher livestock
concentration is associated with lower vegetation growth after controlling
for rainfall and elevation — not that livestock definitively cause
vegetation loss. Field validation is recommended before implementing
exclusion policies.

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
