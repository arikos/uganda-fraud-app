import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('synthetic_uganda_mobile_money_dataset.csv')

# Page setup
st.set_page_config(page_title="Mobile Money Fraud Dataset", layout="wide")
st.title("Uganda Mobile Money Fraud Dataset (View Only)")

# Display table with pagination
st.dataframe(df, use_container_width=True)
