import pandas as pd
import streamlit as st

st.subheader('Data')

df = pd.read_csv('./data/sell.csv', index_col='month')
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2023'])