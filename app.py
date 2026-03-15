import streamlit as st
import pandas as pd

st.title("Brew Haven Coffee Dashboard")

data = pd.read_csv("coffee_sales.csv")

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", data["Revenue"].sum())
col2.metric("Total Profit", data["Profit"].sum())
col3.metric("Total Orders", data["Order_ID"].count())

st.subheader("Revenue Trend")
st.line_chart(data.groupby("Month")["Revenue"].sum())

st.subheader("Revenue by Category")
st.bar_chart(data.groupby("Category")["Revenue"].sum())

st.subheader("Top Selling Products")
st.bar_chart(data.groupby("Product")["Quantity"].sum())
