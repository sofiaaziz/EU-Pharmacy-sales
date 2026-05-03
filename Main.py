import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pharmacy Sales Dashboard", layout="wide")

st.title("💊 Pharmacy Sales Data Analysis")
st.markdown("""
This interactive dashboard explores pharmacy sales performance across multiple regions.
It highlights key trends in revenue, margins, and product categories.
""")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Cleaned_Pharmacy_Sales.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Quick Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"€{df['RevenueEUR'].sum():,.2f}")
col2.metric("Total Units Sold", f"{df['UnitsSold'].sum():,}")
col3.metric("Avg Margin %", f"{(df['MarginEUR'].sum() / df['RevenueEUR'].sum() * 100):.1f}%")
col4.metric("Active Pharmacies", df['PharmacyName'].nunique())

st.dataframe(df.head(10), use_container_width=True)