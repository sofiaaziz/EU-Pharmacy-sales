import streamlit as st
import plotly.express as px
import pandas as pd

st.header("Sales & Performance Trends")
df = pd.read_csv("Cleaned_Pharmacy_Sales.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Monthly Revenue Trend
monthly_sales = df.groupby('MonthName')['RevenueEUR'].sum().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]).reset_index()

fig_line = px.line(monthly_sales, x='MonthName', y='RevenueEUR', title="Monthly Revenue Performance")
st.plotly_chart(fig_line, use_container_width=True)

# Promo vs Non-Promo
promo_impact = df.groupby('PromoFlag')['RevenueEUR'].mean().reset_index()
fig_bar = px.bar(promo_impact, x='PromoFlag', y='RevenueEUR', color='PromoFlag', 
                 title="Average Revenue: Promo vs. Regular")
st.plotly_chart(fig_bar)