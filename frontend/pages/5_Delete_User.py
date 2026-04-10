import streamlit as st
from utils import delete_user

st.title("❌ Delete User")

user_id = st.number_input("Enter User ID", min_value=1)

if st.button("Delete"):
    res = delete_user(user_id)

    if res.status_code == 200:
        st.success("User deleted successfully ✅")
    else:
        st.error("User not found ❌")
