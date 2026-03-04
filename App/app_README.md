# Marsabit Footprint — Dashboard

Streamlit dashboard for The Marsabit Footprint project.

## Running Locally

```bash
pip install streamlit pandas numpy matplotlib
streamlit run app/app.py
```

## Pages

| Page | Content |
|------|---------|
| Project Overview | Key metrics, pipeline summary, six findings |
| NDVI Trend Analysis | Decadal NDVI trends, LULC classification results |
| Spatial Clustering | Moran's I, LISA cluster summary |
| Distance-Decay Analysis | Livestock impact radius from water points |
| Regression Results | OLS vs GWR comparison, coefficient tables |
| Vulnerability Map | Four-class classification, land cover cross-tabulation |
| Policy Recommendations | Five evidence-based recommendations for NEMA |
