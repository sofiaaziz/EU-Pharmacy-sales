import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Variable Relationships & Correlations")

# Referencing the file verbatim as requested
df = pd.read_csv("Cleaned_Pharmacy_Sales.csv")
num_cols = ['UnitsSold', 'RevenueEUR', 'CostEUR', 'MarginEUR', 'ListPriceEUR', 'StandardCostEUR']

# 1. Correlation Heatmap
st.subheader("Feature Correlation Matrix")
corr = df[num_cols].corr()
fig_heat = px.imshow(corr, text_auto=True, aspect="auto", 
                     color_continuous_scale='RdBu_r',
                     title="Correlation between Financial Metrics")
st.plotly_chart(fig_heat, use_container_width=True)

# 2. Scatter Analysis (Trendline Removed)
st.divider()
st.subheader("Revenue vs. Cost Relationship")
color_opt = st.selectbox("Color code by:", ["Category", "Country", "PromoFlag"])

fig_scatter = px.scatter(
    df, 
    x="CostEUR", 
    y="RevenueEUR", 
    color=color_opt, 
    hover_data=['ProductName'],
    title="Revenue vs. Cost (Colored by Group)"
    # trendline="ols" has been removed to avoid statsmodels dependency
)
st.plotly_chart(fig_scatter, use_container_width=True)

# 3. Box Plot Comparisons
st.divider()
st.subheader("Margin Distribution by Group")
fig_box = px.box(df, x="Category", y="MarginEUR", color="IsGeneric",
                 title="Margin Variances: Branded vs. Generic across Categories",
                 notched=True)
st.plotly_chart(fig_box, use_container_width=True)