import streamlit as st
import pandas as pd

st.title('Simple Streamlit App')

# Minimal example to test file loading and matplotlib
try:
    data = pd.read_csv(r'C:\Users\User\Desktop\Fertility.csv')
    st.write(data.head())

    st.write("Data Loaded Successfully!")
except Exception as e:
    st.error(f"An error occurred: {e}")
