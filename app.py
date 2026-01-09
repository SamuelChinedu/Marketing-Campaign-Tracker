import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page config
st.set_page_config(
    page_title="Marketing Campaign Tracker - Update-24 Tech",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# True dark/black theme with teal glow
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; padding-bottom: 100px; }
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #00d4ff !important; font-family: 'Segoe UI', sans-serif; }
    .metric-card {
        background: #0d1117;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border-left: 5px solid #00d4ff;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.15);
        margin-bottom: 1rem;
    }
    .metric-label { color: #94a3b8; font-size: 0.9rem; }
    .metric-value { color: white; font-size: 2.2rem; font-weight: bold; }
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #000000;
        color: #94a3b8;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        border-top: 1px solid #1e293b;
        z-index: 100;
    }
    hr { border-color: #1e293b; margin: 2rem 0; }
    </style>
""", unsafe_allow_html=True)

# Title with branding
st.title("Marketing Campaign Tracker")
st.markdown("**Track performance, ROI & channel efficiency** — Powered by Update-24 Tech Services")

# Generate mock data
campaigns = ["Q1 Campaign", "Q2 Campaign", "Summer Promo", "Holiday Special"]
spend = [24500, 32000, 18000, 12500]
revenue = [78200, 98000, 45000, 38000]
roi = [((r - s) / s * 100) for r, s in zip(revenue, spend)]

df = pd.DataFrame({
    "Campaign": campaigns,
    "Spend": spend,
    "Revenue": revenue,
    "ROI": roi
})

# KPI cards (with teal glow)
col1, col2, col3 = st.columns(3)
col1.markdown('<div class="metric-card">'
              '<div class="metric-label">Total Spend</div>'
              f'<div class="metric-value">${sum(spend):,}</div>'
              '<div class="metric-label">↑ 12%</div></div>', unsafe_allow_html=True)

col2.markdown('<div class="metric-card">'
              '<div class="metric-label">Revenue</div>'
              f'<div class="metric-value">${sum(revenue):,}</div>'
              '<div class="metric-label">↑ 8.5%</div></div>', unsafe_allow_html=True)

col3.markdown('<div class="metric-card">'
              '<div class="metric-label">ROI</div>'
              f'<div class="metric-value">{np.mean(roi):.1f}x</div>'
              '<div class="metric-label">↑ 4%</div></div>', unsafe_allow_html=True)

# Campaign Performance Bar
st.markdown("### Campaign Performance Overview")
fig_bar = px.bar(
    df,
    x="Campaign",
    y=["Spend", "Revenue"],
    barmode="group",
    title="Spend vs Revenue by Campaign",
    color_discrete_sequence=["#1e293b", "#00d4ff"]
)
fig_bar.update_layout(
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)
st.plotly_chart(fig_bar, use_container_width=True)

# Recent Activities
st.markdown("### Recent Activities")
activities = [
    "Campaign Q2 launched",
    "Performance review meeting",
    "Budget allocation updated",
    "Q1 report shared with team",
    "Holiday Special scheduled"
]
for act in activities:
    st.markdown(f'<div style="color: #94a3b8; margin: 0.5rem 0;">• {act}</div>', unsafe_allow_html=True)

# Top Channels Pie
st.markdown("### Top Performing Channels")
fig_pie = px.pie(
    names=["Social Media", "Email", "SEO", "PPC"],
    values=[35, 25, 20, 20],
    title="Channel Contribution to Impressions",
    color_discrete_sequence=["#00d4ff", "#475569", "#94a3b8", "#334155"]
)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
fig_pie.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)
st.plotly_chart(fig_pie, use_container_width=True)

# Footer
st.markdown("""
    <div class="footer">
        Built by <strong>Update-24 Tech Services</strong> — Intelligent Digital Solutions | Web • Mobile • AI • Data
    </div>
""", unsafe_allow_html=True)
