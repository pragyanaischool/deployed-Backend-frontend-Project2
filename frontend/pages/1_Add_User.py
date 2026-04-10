import streamlit as st
from utils import create_user

st.title("➕ Add New User")

name = st.text_input("Name")
age = st.number_input("Age", 1, 120)
email = st.text_input("Email")

if st.button("Create User"):
    payload = {"name": name, "age": age, "email": email}
    
    res = create_user(payload)

    if res.status_code == 200:
        st.success("User created successfully ✅")
        st.json(res.json())
    else:
        st.error(res.text)
