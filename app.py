import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page config
st.set_page_config(
    page_title="Marketing Campaign Tracker - Update-24 Tech",
    page_icon="📈",
    layout="wide"
)

# Custom branding CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; padding-bottom: 100px; }
    h1, h2, h3 { color: #0A2540 !important; }
    .stMetric {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        padding: 1.5rem;
        text-align: center;
        border-left: 5px solid #00B4D8;
    }
    .stMetric label { color: #555; font-size: 0.95rem; }
    .stMetric .stMetric-value { color: #0A2540; font-size: 2rem; font-weight: bold; }
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #0A2540;
        color: white;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        z-index: 100;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📈 Marketing Campaign Tracker")
st.markdown("**Track performance, ROI & channel efficiency** — Built by Update-24 Tech Services")

# Generate mock campaign data (Q1 2025)
np.random.seed(42)
campaigns = ["Social Media Blast", "Google Ads", "Email Newsletter", "Influencer Collab", "Content Marketing"]
data = pd.DataFrame({
    "Campaign": campaigns,
    "Spend": np.random.randint(8000, 35000, 5),
    "Revenue": np.random.randint(15000, 80000, 5),
    "Impressions": np.random.randint(50000, 300000, 5),
    "Clicks": np.random.randint(2000, 15000, 5),
})

data["ROI"] = ((data["Revenue"] - data["Spend"]) / data["Spend"] * 100).round(1)
data["CTR"] = (data["Clicks"] / data["Impressions"] * 100).round(2)

# Daily trend (mock 30 days)
dates = pd.date_range("2025-01-01", periods=30)
daily_trend = pd.DataFrame({
    "Date": dates,
    "Total Revenue": np.random.normal(5000, 1200, 30).cumsum().round(0)
})

# KPI cards
col1, col2, col3, col4, col5 = st.columns(5)
total_spend = data["Spend"].sum()
total_revenue = data["Revenue"].sum()
total_roi = ((total_revenue - total_spend) / total_spend * 100).round(1)

col1.metric("Total Spend", f"₦{total_spend:,.0f}")
col2.metric("Total Revenue", f"₦{total_revenue:,.0f}")
col3.metric("Overall ROI", f"{total_roi}%")
col4.metric("Total Impressions", f"{data['Impressions'].sum():,}")
col5.metric("Avg CTR", f"{data['CTR'].mean():.2f}%")

# Main charts
st.markdown("### Campaign Performance Comparison")
fig_bar = px.bar(
    data,
    x="Campaign",
    y=["Spend", "Revenue"],
    barmode="group",
    title="Spend vs Revenue by Campaign",
    color_discrete_sequence=["#0A2540", "#00B4D8"]
)
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("### Daily Revenue Trend (Last 30 Days)")
fig_line = px.line(
    daily_trend,
    x="Date",
    y="Total Revenue",
    title="Daily Revenue Performance",
    color_discrete_sequence=["#00B4D8"]
)
fig_line.update_traces(line=dict(width=3))
st.plotly_chart(fig_line, use_container_width=True)

st.markdown("### Channel Breakdown (Impressions)")
fig_pie = px.pie(
    data,
    values="Impressions",
    names="Campaign",
    title="Impressions Share by Campaign",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_pie, use_container_width=True)

# Footer
st.markdown("""
    <div class="footer">
        Built by <strong>Update-24 Tech Services</strong> — Intelligent Digital Solutions | Web • Mobile • AI • Data
    </div>
""", unsafe_allow_html=True)
