import time
import streamlit as st

with st.spinner("Loading User's information..."):
    time.sleep(1)
    with open("Account.csv", 'r') as f:
        content = f.readlines()
st.table(content)