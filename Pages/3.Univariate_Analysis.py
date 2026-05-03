import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.header("Individual Variable Distribution")

df = pd.read_csv("Cleaned_Pharmacy_Sales.csv")
num_cols = ['UnitsSold', 'RevenueEUR', 'CostEUR', 'MarginEUR', 'ListPriceEUR', 'StandardCostEUR']

# Sidebar Selection
target_var = st.selectbox("Select variable to analyze:", num_cols)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Distribution of {target_var}")
    fig_hist = px.histogram(df, x=target_var, marginal="box", 
                            title=f"Histogram & Boxplot of {target_var}",
                            color_discrete_sequence=['#00CC96'])
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.subheader("Descriptive Statistics")
    st.write(df[target_var].describe())

# Categorical Analysis
st.divider()
st.subheader("Categorical Frequency")
cat_var = st.selectbox("Select category to analyze:", ["Category", "Country", "IsGeneric", "PromoFlag"])
cat_counts = df[cat_var].value_counts().reset_index()
fig_bar = px.bar(cat_counts, x=cat_var, y='count', color=cat_var, 
                 title=f"Frequency of {cat_var}")
st.plotly_chart(fig_bar, use_container_width=True)