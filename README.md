# Urban Traffic Flow, Congestion Management & Mobility Optimization

**Author:** T Harshalatha

## About the Project

This project focuses on analyzing urban traffic data to understand traffic volume, congestion, road capacity, speed, and other factors related to urban mobility.

Using Python and data analysis techniques, I cleaned and explored the dataset, identified high-congestion areas and bottlenecks, studied relationships between traffic factors, and developed an interactive dashboard using Streamlit.

The project aims to transform raw traffic data into meaningful insights that can support better traffic management and mobility optimization.

## Project Objectives

- Understand the overall traffic and congestion situation.
- Compare traffic conditions across different areas and roads.
- Identify high-congestion and high-risk locations.
- Study the relationship between traffic volume, speed, capacity, and congestion.
- Create useful traffic KPIs.
- Perform a traffic-reduction scenario analysis.
- Build an interactive dashboard.
- Suggest practical improvement areas based on the analysis.

## Dataset

The dataset contains:

- **Records:** 8,936
- **Areas:** 8
- **Roads / Intersections:** 16
- **Analysis Period:** 01 January 2022 – 09 August 2024

The dataset includes traffic volume, average speed, travel time index, congestion level, road capacity utilization, incident reports, environmental impact, public transport usage, traffic signal compliance, parking usage, pedestrian and cyclist count, weather conditions, and roadwork activity.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- ipywidgets
- Streamlit
- Jupyter Notebook
- Git
- GitHub

## Project Work

The main steps completed in this project were:

1. Loaded and understood the traffic dataset.
2. Cleaned and validated the data.
3. Created date-based features.
4. Calculated important traffic KPIs.
5. Analyzed traffic conditions by area, day, month, year, weather, and roadwork activity.
6. Studied correlations between important traffic variables.
7. Identified high-risk roads and recurring bottlenecks.
8. Performed a 15% traffic-volume reduction scenario.
9. Built an interactive traffic dashboard.
10. Prepared recommendations based on the analysis.
11. Developed a Streamlit application to present traffic insights interactively.
12. Used Git and GitHub for version control and project management.

## Key Findings

- Average traffic volume was about **29,236 vehicles**.
- Average congestion level was about **80.82%**.
- Average road capacity utilization was about **92.03%**.
- Average speed was about **39.45 km/h**.
- **Koramangala** had the highest average congestion at about **93.99%**.
- Koramangala also had the lowest average speed at about **36.06 km/h**.
- Traffic volume and congestion had a strong positive correlation of about **0.84**.
- Road capacity utilization and congestion had a strong positive correlation of about **0.87**.

## Scenario Analysis

I tested a simple scenario where traffic volume was reduced by **15%**.

In this scenario:

- Average traffic volume reduced from about **29,236 to 24,851 vehicles**.
- Estimated congestion reduced from about **80.82% to 70.67%**.

This is an analytical estimate based on historical data and should not be considered a guaranteed real-world result.

## Interactive Dashboard

I developed an interactive **Urban Traffic Mobility Dashboard** using Python, Plotly, and Streamlit.

The dashboard allows users to filter the analysis by:

- Area
- Year

It displays:

- Average traffic volume
- Average congestion
- Average speed
- Road capacity utilization
- Traffic volume trend
- Congestion trend
- Average speed trend
- Top high-risk roads/intersections
- Traffic reliability

The dashboard provides a visual overview of traffic conditions and helps users explore traffic patterns across different areas and years.

## Project Structure

```text
Urban Traffic Analytics/
│
├── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── Bangalore_traffic_processed.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── src/
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Project Deliverables

- Jupyter Notebook containing the analysis
- Cleaned and enriched traffic dataset
- Interactive Streamlit traffic dashboard
- Traffic Performance & Optimization Report
- Charts and analysis outputs
- GitHub repository containing the project files

## Conclusion

This project helped me understand how Python and data analysis can be used to study a real-world problem such as urban traffic.

The analysis identified areas with high congestion and capacity pressure and highlighted practical improvement areas such as traffic signal coordination, bottleneck management, public transport support, demand management, and data-driven traffic monitoring.

The interactive dashboard makes it easier to explore traffic KPIs, trends, and high-risk locations, supporting data-driven decision-making for urban mobility optimization.