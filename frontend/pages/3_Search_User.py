import streamlit as st
from utils import get_user

st.title("🔍 Search User by ID")

user_id = st.number_input("Enter User ID", min_value=1)

if st.button("Search"):
    res = get_user(user_id)

    if res.status_code == 200:
        st.success("User Found ✅")
        st.json(res.json())
    else:
        st.error("User not found ❌")
