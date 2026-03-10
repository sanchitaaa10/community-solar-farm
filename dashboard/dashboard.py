import streamlit as st
import pandas as pd

# 1. Layout Configuration
st.set_page_config(page_title="Solar Analytics", layout="wide")

# 2. Minimalist Professional CSS
st.markdown("""
    <style>
    /* Clean Dark Background */
    [data-testid="stAppViewContainer"] {
        background-color: #0E1117;
    }
    
    /* Remove Border around charts for a seamless look */
    .stChart {
        border: none !important;
    }

    /* Metric Styling: Clean and Bold */
    [data-testid="stMetric"] {
        background: #161B22;
        border: 1px solid #30363D;
        padding: 1rem;
        border-radius: 8px;
    }

    /* Title Styling */
    h1 {
        font-weight: 700 !important;
        color: #F0F6FC !important;
    }
    
    /* Sidebar Cleanup */
    [data-testid="stSidebar"] {
        background-color: #010409;
        border-right: 1px solid #30363D;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Data Processing
df = pd.read_csv("dataset/solar_dataset.csv")

# Calculations for Metrics
total_gen = df["Solar_Generation_kWh"].sum()
total_cons = df["Consumption_kWh"].sum()
avg_grid = df["Grid_Usage_kWh"].mean()

# --- HEADER ---
st.title("☀️ Community Solar Farm")
st.markdown("---")

# --- KPI ROW ---
m1, m2, m3 = st.columns(3)
m1.metric("⚡ Generation", f"{total_gen:,.0f} kWh")
m2.metric("🏠 Consumption", f"{total_cons:,.0f} kWh")
m3.metric("🔌 Avg Grid Load", f"{avg_grid:,.1f} kWh")

st.write("##")

# --- VISUALIZATION GRID ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Solar Generation Trend")
    # Using 'color' parameter for a professional "Solar Gold"
    st.line_chart(df["Solar_Generation_kWh"], color="#FFD700")

with col_right:
    st.subheader("📉 Energy Consumption Trend")
    # Using a professional "Corporate Blue"
    st.line_chart(df["Consumption_kWh"], color="#58A6FF")

st.subheader("📊 Grid Usage Overview")
# Using a "Neutral Slate" for grid data
st.bar_chart(df["Grid_Usage_kWh"], color="#8B949E")

st.markdown("---")

# --- DATA PREVIEW ---
with st.expander("🔍 View Raw Dataset Details"):
    st.dataframe(df, use_container_width=True)