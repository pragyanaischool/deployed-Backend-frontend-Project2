import streamlit as st
import pandas as pd
from utils import get_users

st.title("📋 All Users")

if st.button("Fetch Users"):
    res = get_users()

    if res.status_code == 200:
        data = res.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.error("Failed to fetch users")
