
# ============================================================
# 🚦 URBAN TRAFFIC MOBILITY DASHBOARD
# STREAMLIT APPLICATION
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from pathlib import Path


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Urban Traffic Mobility Dashboard",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
    max-width: 100%;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* DASHBOARD HEADER */

.dashboard-header {
    background: #173f68;
    border-radius: 9px;
    padding: 17px 22px;
    min-height: 92px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    margin-bottom: 18px;
    box-sizing: border-box;
}

.dashboard-title {
    font-family: Arial, sans-serif;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 7px;
    line-height: 1.2;
}

.dashboard-subtitle {
    font-family: Arial, sans-serif;
    font-size: 12px;
    color: #dbeafe;
}

.analysis-period {
    text-align: right;
    font-family: Arial, sans-serif;
    font-size: 11px;
    color: #e2e8f0;
}

.analysis-year {
    font-size: 13px;
    font-weight: 600;
    color: white;
}

/* FILTERS */

.filter-heading {
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 5px;
}

.filter-label {
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: 600;
    color: #334155;
    margin-bottom: 5px;
}

div[data-testid="stSelectbox"] {
    margin-bottom: 12px;
}

/* KPI CARDS */

.kpi-card {
    height: 108px;
    border-radius: 9px;
    padding: 13px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    border: 1px solid;
    font-family: Arial, sans-serif;
    margin-bottom: 12px;
    width: 100%;
}

.kpi-icon {
    position: absolute;
    left: 12px;
    top: 17px;
    width: 42px;
    height: 42px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
}

.kpi-text {
    position: absolute;
    left: 65px;
    top: 15px;
}

.kpi-title {
    font-size: 11px;
    font-weight: 500;
    color: #334155;
    margin-bottom: 7px;
    white-space: nowrap;
}

.kpi-value {
    font-size: 25px;
    line-height: 26px;
    font-weight: 700;
}

.kpi-unit {
    font-size: 10px;
    color: #64748b;
    margin-top: 3px;
}

.kpi-spark {
    position: absolute;
    right: 7px;
    bottom: 7px;
    width: 95px;
    height: 40px;
}

/* CHART HEADINGS */

.chart-heading {
    font-family: Arial, sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: #1e293b;
    padding: 2px 0 7px 0;
}

/* RELIABILITY PANEL */

.reliability-panel {
    background: #f8fafc;
    border: 1px solid #dbe3ec;
    border-radius: 10px;
    padding: 17px 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 105px;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
    width: 100%;
}

.reliability-left {
    display: flex;
    align-items: center;
    gap: 15px;
}

.reliability-icon {
    width: 52px;
    height: 52px;
    border-radius: 9px;
    background: #eaf2ff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
}

.reliability-title {
    font-size: 13px;
    font-weight: 600;
    color: #334155;
    margin-bottom: 5px;
}

.reliability-value {
    font-size: 27px;
    font-weight: 700;
    color: #2563eb;
    line-height: 1.1;
}

.reliability-description {
    font-size: 10px;
    color: #64748b;
    margin-top: 4px;
}

.high-risk-title {
    font-size: 12px;
    color: #64748b;
    margin-bottom: 5px;
}

.high-risk-value {
    font-size: 25px;
    font-weight: 700;
    color: #dc2626;
}

/* CHART CONTAINERS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 9px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. LOAD PROCESSED DATASET
# ============================================================

PROJECT_DIR = Path(__file__).parent

DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "Bangalore_traffic_processed.csv"
)


@st.cache_data
def load_data():

    data = pd.read_csv(DATA_PATH)

    data['date'] = pd.to_datetime(data['date'])

    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_name'] = data['date'].dt.day_name()

    return data


try:

    df = load_data()

except Exception as e:

    st.error(f"Unable to load the processed dataset: {e}")
    st.stop()


# ============================================================
# 4. VALIDATE REQUIRED COLUMNS
# ============================================================

required_columns = [
    'date',
    'area_name',
    'traffic_volume',
    'congestion_level',
    'average_speed',
    'road_capacity_utilization',
    'road/intersection_name'
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(f"Missing required columns: {missing_columns}")
    st.stop()


# ============================================================
# 5. GET AREA NAMES AND YEARS
# ============================================================

areas = sorted(
    df['area_name']
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

years = sorted(
    df['year']
    .dropna()
    .astype(int)
    .unique()
    .tolist()
)


# ============================================================
# 6. INITIALIZE FILTER VALUES
# ============================================================

if "area_filter" not in st.session_state:
    st.session_state["area_filter"] = "All Areas"

if "year_filter" not in st.session_state:
    st.session_state["year_filter"] = "All Years"

if st.session_state["area_filter"] not in ["All Areas"] + areas:
    st.session_state["area_filter"] = "All Areas"

if st.session_state["year_filter"] not in ["All Years"] + years:
    st.session_state["year_filter"] = "All Years"

# ============================================================
# 7. DASHBOARD HEADER
# ============================================================

selected_area = st.session_state.get(
    "area_filter", "All Areas"
)

selected_year = st.session_state.get(
    "year_filter", "All Years"
)

st.html(
    f"""
    <div class="dashboard-header">

        <div>

            <div class="dashboard-title">
                🚦 Urban Traffic Mobility Dashboard
            </div>

            <div class="dashboard-subtitle">
                Traffic flow, congestion, capacity and reliability analysis
                &nbsp; • &nbsp;
                {selected_area}
                &nbsp; • &nbsp;
                {selected_year}
            </div>

        </div>

        <div class="analysis-period">

            <div>📅 Analysis Period</div>

            <div class="analysis-year">
                {selected_year}
            </div>

        </div>

    </div>
    """
)



# ============================================================
# 8. AREA AND YEAR FILTERS
# ============================================================

st.html(
    '<div class="filter-heading">Select Filters</div>'
)

filter_col1, filter_col2, empty_col = st.columns(
    [1, 1, 2],
    gap="small"
)

with filter_col1:

    st.html(
        '<div class="filter-label">📍 Area</div>'
    )

    selected_area = st.selectbox(
        "Area",
        options=["All Areas"] + areas,
        label_visibility="collapsed",
        key="area_filter"
    )


with filter_col2:

    st.html(
        '<div class="filter-label">📅 Year</div>'
    )

    selected_year = st.selectbox(
        "Year",
        options=["All Years"] + years,
        format_func=lambda x: str(x),
        label_visibility="collapsed",
        key="year_filter"
    )


# ============================================================
# 9. FILTER DATA
# ============================================================

data = df.copy()

if selected_area != "All Areas":

    data = data[
        data['area_name'].astype(str) == str(selected_area)
    ]

if selected_year != "All Years":

    data = data[
        data['year'] == int(selected_year)
    ]


if data.empty:

    st.warning("No data available for the selected filters.")
    st.stop()


# ============================================================
# 10. KPI CALCULATIONS
# ============================================================

avg_volume = data['traffic_volume'].mean()

avg_congestion = data['congestion_level'].mean()

avg_speed = data['average_speed'].mean()

avg_capacity = data['road_capacity_utilization'].mean()


# ============================================================
# 11. KPI SPARKLINE FUNCTION
# ============================================================

def create_sparkline(values, color):

    values = np.asarray(values, dtype=float)

    if len(values) == 0:
        return ""

    if len(values) == 1:

        points_string = "5,20 95,20"

    else:

        min_val = values.min()
        max_val = values.max()

        if max_val == min_val:

            normalized = np.full(len(values), 0.5)

        else:

            normalized = (
                (values - min_val)
                / (max_val - min_val)
            )

        points = []

        for i, value in enumerate(normalized):

            x = 5 + i * 90 / (len(normalized) - 1)
            y = 31 - value * 24

            points.append(f"{x:.1f},{y:.1f}")

        points_string = " ".join(points)

    return f"""
    <svg width="95" height="40" viewBox="0 0 100 40">

        <polygon
            points="{points_string} 95,40 5,40"
            fill="{color}"
            opacity="0.08"
        />

        <polyline
            points="{points_string}"
            fill="none"
            stroke="{color}"
            stroke-width="1.8"
            stroke-linecap="round"
            stroke-linejoin="round"
            opacity="0.65"
        />

    </svg>
    """


# ============================================================
# 12. KPI CARD FUNCTION
# ============================================================

def create_kpi_card(
    title,
    value,
    unit,
    icon,
    card_bg,
    border_color,
    icon_bg,
    value_color,
    spark_values
):

    sparkline = create_sparkline(
        spark_values,
        value_color
    )

    return f"""
    <div class="kpi-card"
         style="
            background:{card_bg};
            border-color:{border_color};
         ">

        <div class="kpi-icon"
             style="background:{icon_bg};">

            {icon}

        </div>

        <div class="kpi-text">

            <div class="kpi-title">
                {title}
            </div>

            <div class="kpi-value"
                 style="color:{value_color};">

                {value}

            </div>

            <div class="kpi-unit">
                {unit}
            </div>

        </div>

        <div class="kpi-spark">
            {sparkline}
        </div>

    </div>
    """


# ============================================================
# 13. KPI SPARKLINE DATA
# ============================================================

volume_spark = (
    data.groupby('date')['traffic_volume']
    .mean()
    .sort_index()
    .tail(30)
    .values
)

congestion_spark = (
    data.groupby('date')['congestion_level']
    .mean()
    .sort_index()
    .tail(30)
    .values
)

speed_spark = (
    data.groupby('date')['average_speed']
    .mean()
    .sort_index()
    .tail(30)
    .values
)

capacity_spark = (
    data.groupby('date')['road_capacity_utilization']
    .mean()
    .sort_index()
    .tail(30)
    .values
)


# ============================================================
# 14. DISPLAY FOUR KPI CARDS
# ============================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(
    4,
    gap="medium"
)


with kpi1:

    st.html(
        create_kpi_card(
            "Average Traffic Volume",
            f"{avg_volume:,.0f}",
            "vehicles",
            "🚗",
            "#eef6ff",
            "#bfdbfe",
            "#dbeafe",
            "#2563eb",
            volume_spark
        )
    )


with kpi2:

    st.html(
        create_kpi_card(
            "Average Congestion",
            f"{avg_congestion:.1f}%",
            "congestion level",
            "🚘",
            "#fff7ed",
            "#fed7aa",
            "#ffedd5",
            "#ea580c",
            congestion_spark
        )
    )


with kpi3:

    st.html(
        create_kpi_card(
            "Average Speed",
            f"{avg_speed:.1f}",
            "km/h",
            "⏱",
            "#effaf4",
            "#bbf7d0",
            "#dcfce7",
            "#15803d",
            speed_spark
        )
    )


with kpi4:

    st.html(
        create_kpi_card(
            "Capacity Utilization",
            f"{avg_capacity:.1f}%",
            "of road capacity",
            "🛣️",
            "#f7f3ff",
            "#ddd6fe",
            "#ede9fe",
            "#6d28d9",
            capacity_spark
        )
    )


# ============================================================
# 15. COMMON PLOTLY LAYOUT
# ============================================================

def apply_chart_layout(fig, height=300):

    fig.update_layout(

        height=height,

        autosize=True,

        template="plotly_white",

        margin=dict(
            l=55,
            r=18,
            t=5,
            b=45
        ),

        hovermode="x unified",

        showlegend=False,

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            family="Arial, sans-serif",
            color="#334155",
            size=10
        )

    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#edf2f7",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#edf2f7",
        zeroline=False
    )

    return fig


# ============================================================
# 16. CHART 1 - TRAFFIC VOLUME TREND
# ============================================================

volume_data = (
    data.groupby('date', as_index=False)
    ['traffic_volume']
    .mean()
    .sort_values('date')
)

fig_volume = go.Figure()

fig_volume.add_trace(

    go.Scatter(

        x=volume_data['date'],

        y=volume_data['traffic_volume'],

        mode='lines',

        fill='tozeroy',

        line=dict(
            color='#4169e1',
            width=2
        ),

        fillcolor='rgba(65,105,225,0.18)',

        hovertemplate=
        '<b>Date:</b> %{x|%d %b %Y}<br>'
        '<b>Traffic Volume:</b> %{y:,.0f}'
        '<extra></extra>'

    )

)

apply_chart_layout(fig_volume)

fig_volume.update_layout(
    xaxis_title="Date",
    yaxis_title="Traffic Volume"
)


# ============================================================
# 17. CHART 2 - CONGESTION TREND
# ============================================================

congestion_data = (
    data.groupby('date', as_index=False)
    ['congestion_level']
    .mean()
    .sort_values('date')
)

fig_congestion = go.Figure()

fig_congestion.add_trace(

    go.Scatter(

        x=congestion_data['date'],

        y=congestion_data['congestion_level'],

        mode='lines',

        line=dict(
            color='#dc2626',
            width=2
        ),

        hovertemplate=
        '<b>Date:</b> %{x|%d %b %Y}<br>'
        '<b>Congestion:</b> %{y:.1f}%'
        '<extra></extra>'

    )

)

apply_chart_layout(fig_congestion)

fig_congestion.update_layout(

    xaxis_title="Date",

    yaxis_title="Congestion (%)"

)

fig_congestion.update_yaxes(
    range=[0, 100]
)


# ============================================================
# 18. CHART 3 - AVERAGE SPEED TREND
# ============================================================

speed_data = (
    data.groupby('date', as_index=False)
    ['average_speed']
    .mean()
    .sort_values('date')
)

fig_speed = go.Figure()

fig_speed.add_trace(

    go.Scatter(

        x=speed_data['date'],

        y=speed_data['average_speed'],

        mode='lines',

        line=dict(
            color='#16a34a',
            width=2
        ),

        hovertemplate=
        '<b>Date:</b> %{x|%d %b %Y}<br>'
        '<b>Average Speed:</b> %{y:.1f} km/h'
        '<extra></extra>'

    )

)

apply_chart_layout(fig_speed)

fig_speed.update_layout(

    xaxis_title="Date",

    yaxis_title="Speed (km/h)"

)


# ============================================================
# 19. CHART 4 - TOP HIGH-RISK ROADS
# ============================================================

road_data = (
    data.groupby('road/intersection_name')
    ['congestion_level']
    .mean()
    .reset_index()
    .sort_values(
        'congestion_level',
        ascending=False
    )
    .head(10)
    .sort_values(
        'congestion_level',
        ascending=True
    )
)

fig_risk = go.Figure()

fig_risk.add_trace(

    go.Bar(

        x=road_data['congestion_level'],

        y=road_data['road/intersection_name'],

        orientation='h',

        marker=dict(
            color='#f97316'
        ),

        hovertemplate=
        '<b>%{y}</b><br>'
        'Average Congestion: %{x:.1f}%'
        '<extra></extra>'

    )

)

apply_chart_layout(fig_risk)

fig_risk.update_layout(

    margin=dict(
        l=125,
        r=18,
        t=5,
        b=45
    ),

    xaxis_title="Average Congestion (%)",

    yaxis_title=None

)

fig_risk.update_xaxes(
    range=[0, 100]
)

fig_risk.update_yaxes(
    showgrid=False
)


# ============================================================
# 20. DISPLAY CHARTS - FIRST ROW
# ============================================================

chart_col1, chart_col2 = st.columns(
    2,
    gap="large"
)


with chart_col1:

    with st.container(border=True):

        st.html(
            '<div class="chart-heading">📊 Traffic Volume Trend</div>'
        )

        st.plotly_chart(
            fig_volume,
            use_container_width=True,
            config={"displayModeBar": False},
            key="traffic_volume_chart"
        )


with chart_col2:

    with st.container(border=True):

        st.html(
            '<div class="chart-heading">🚘 Congestion Trend</div>'
        )

        st.plotly_chart(
            fig_congestion,
            use_container_width=True,
            config={"displayModeBar": False},
            key="congestion_chart"
        )


# ============================================================
# 21. DISPLAY CHARTS - SECOND ROW
# ============================================================

chart_col3, chart_col4 = st.columns(
    2,
    gap="large"
)


with chart_col3:

    with st.container(border=True):

        st.html(
            '<div class="chart-heading">📈 Average Speed Trend</div>'
        )

        st.plotly_chart(
            fig_speed,
            use_container_width=True,
            config={"displayModeBar": False},
            key="speed_chart"
        )


with chart_col4:

    with st.container(border=True):

        st.html(
            '<div class="chart-heading">⚠️ Top High-Risk Roads / Intersections</div>'
        )

        st.plotly_chart(
            fig_risk,
            use_container_width=True,
            config={"displayModeBar": False},
            key="risk_chart"
        )


# ============================================================
# 22. TRAFFIC RELIABILITY CALCULATION
# ============================================================

congestion_threshold = (
    df['congestion_level'].quantile(0.75)
)

high_congestion_pct = (
    data['congestion_level']
    .ge(congestion_threshold)
    .mean()
    * 100
)

reliability = 100 - high_congestion_pct


# ============================================================
# 23. TRAFFIC RELIABILITY PANEL
# ============================================================

st.html(
    f"""
    <div class="reliability-panel">

        <div class="reliability-left">

            <div class="reliability-icon">
                🛡️
            </div>

            <div>

                <div class="reliability-title">
                    Traffic Reliability
                </div>

                <div class="reliability-value">
                    {reliability:.1f}%
                </div>

                <div class="reliability-description">
                    Observations below the high-congestion threshold
                </div>

            </div>

        </div>

        <div style="
            display:flex;
            align-items:center;
            text-align:right;
            gap:15px;
        ">

            <div>

                <div class="high-risk-title">
                    High-congestion observations
                </div>

                <div class="high-risk-value">
                    {high_congestion_pct:.1f}%
                </div>

            </div>

            <div style="
                width:52px;
                height:52px;
                border-radius:9px;
                background:#fff0f0;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:24px;
            ">
                👥
            </div>

        </div>

    </div>
    """
)


# ============================================================
# 24. FOOTER
# ============================================================

st.html(
    """
    <div style="
        text-align:center;
        color:#94a3b8;
        font-size:10px;
        padding:15px 0 5px 0;
    ">
        Urban Traffic Analytics |
        Traffic Performance & Optimization
    </div>
    """
)
