import streamlit as st
import time

with st.spinner("Loading payment history..."):
    time.sleep(1)
with open("Payments.csv", encoding="utf-8") as f:
    content = f.readlines()

st.table(content)