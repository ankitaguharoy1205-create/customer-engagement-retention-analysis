import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Retention Dashboard", layout="wide")

st.title("Customer Engagement & Product Utilization Analytics")
st.write("Customer churn analysis and retention insights")

st.subheader("Project Overview")

a, b, c = st.columns(3)
a.metric("Total Customers", "10,000")
b.metric("Customers Exited", "2,037")
c.metric("Overall Churn Rate", "20.37%")

st.subheader("Churn Rate by Number of Products")

products = pd.DataFrame({
    "Number of Products": ["1", "2", "3", "4"],
    "Churn Rate (%)": [27.71, 7.58, 82.71, 100.00]
})
st.bar_chart(products.set_index("Number of Products"))

st.subheader("Single Product vs Multi Product")

categories = pd.DataFrame({
    "Customer Type": ["Single Product", "Multi Product"],
    "Churn Rate (%)": [27.71, 12.77]
})
st.bar_chart(categories.set_index("Customer Type"))

st.subheader("Churn by Engagement Profile")

engagement = pd.DataFrame({
    "Profile": [
        "Active Engaged",
        "Active Low-Product",
        "Inactive Disengaged",
        "Inactive High-Balance"
    ],
    "Churn Rate (%)": [9.06, 18.97, 21.21, 37.33]
})
st.bar_chart(engagement.set_index("Profile"))

st.info(
    "Key insight: Customers with three or four products "
    "showed especially high churn rates in this dataset. "
    "These patterns show association, not proof of cause."
)

st.caption("Created for the Unified Mentor Data Analytics Project.")
