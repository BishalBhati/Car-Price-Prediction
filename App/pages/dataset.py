import streamlit as st
import pandas as pd

st.title("Dataset")

df = pd.read_csv("car data.csv")

st.write(df.sample(8))