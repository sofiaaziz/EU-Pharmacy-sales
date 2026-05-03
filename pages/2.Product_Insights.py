import streamlit as st
import plotly.express as px
import pandas as pd

st.header("Product & Category Deep-Dive")
df = pd.read_csv("Cleaned_Pharmacy_Sales.csv")

# Category Breakdown
cat_perf = df.groupby('Category')['RevenueEUR'].sum().sort_values(ascending=False).reset_index()
fig_pie = px.pie(cat_perf, values='RevenueEUR', names='Category', title="Revenue Distribution by Category")
st.plotly_chart(fig_pie)

# Generic vs. Branded Performance
gen_df = df.groupby(['Category', 'IsGeneric'])['UnitsSold'].sum().reset_index()
fig_sun = px.sunburst(gen_df, path=['Category', 'IsGeneric'], values='UnitsSold', 
                      title="Units Sold: Category > Generic vs Brand")
st.plotly_chart(fig_sun)