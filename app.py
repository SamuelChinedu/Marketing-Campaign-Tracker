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

# Dark modern theme + branding
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    h1, h2, h3 { color: #00d4ff !important; }
    .stMetric {
        background: #1e293b;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border-left: 5px solid #00d4ff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stMetric label { color: #94a3b8; font-size: 0.9rem; }
    .stMetric .stMetric-value { color: white; font-size: 2rem; font-weight: bold; }
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #0f172a;
        color: #94a3b8;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        border-top: 1px solid #334155;
    }
    .sidebar .sidebar-content { background-color: #1e293b; }
    hr { border-color: #334155; margin: 2rem 0; }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Marketing Campaign Tracker")
st.markdown("**Track performance, ROI & channel efficiency** — Powered by Update-24 Tech Services")

# Generate mock data
campaigns = ["Q1 Campaign", "Q2 Campaign", "Summer Promo", "Holiday Special"]
spend = [24500, 32000, 18000, 12500]
revenue = [78200, 98000, 45000, 38000]
roi = [((r - s) / s * 100) for r, s in zip(revenue, spend)]
ctr = [12.5, 8.5, 5.7, 4.2]

df = pd.DataFrame({
    "Campaign": campaigns,
    "Spend": spend,
    "Revenue": revenue,
    "ROI": roi,
    "CTR": ctr
})

# KPI cards with mini trends (mock small data for sparkline effect)
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Spend", f"${sum(spend):,}", delta="-5%", delta_color="inverse")
kpi2.metric("Revenue", f"${sum(revenue):,}", delta="+8.5%", delta_color="normal")
kpi3.metric("ROI", f"{np.mean(roi):.1f}x", delta="+4%", delta_color="normal")
kpi4.metric("Avg CTR", f"{np.mean(ctr):.1f}%", delta="+5.2%", delta_color="normal")

# Campaign Performance Bar Chart
st.markdown("### Campaign Performance Overview")
fig_bar = px.bar(
    df,
    x="Campaign",
    y=["Spend", "Revenue"],
    barmode="group",
    title="Spend vs Revenue by Campaign",
    color_discrete_sequence=["#475569", "#00d4ff"]
)
fig_bar.update_layout(showlegend=False, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_bar, use_container_width=True)

# Recent Activities (mock list)
st.markdown("### Recent Activities")
activities = [
    "Campaign Q2 launched",
    "Performance review meeting",
    "Budget allocation updated",
    "Q1 report shared with team",
    "Holiday Special scheduled"
]
for act in activities:
    st.markdown(f"• {act}")

# Top Channels Pie Chart
st.markdown("### Top Performing Channels")
fig_pie = px.pie(
    names=["Social Media", "Email", "SEO", "PPC"],
    values=[35, 25, 20, 20],
    title="Channel Contribution to Impressions",
    color_discrete_sequence=["#00d4ff", "#475569", "#94a3b8", "#334155"]
)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

# Footer
st.markdown("""
    <div class="footer">
        Built by <strong>Update-24 Tech Services</strong> — Intelligent Digital Solutions | Web • Mobile • AI • Data
    </div>
""", unsafe_allow_html=True)
