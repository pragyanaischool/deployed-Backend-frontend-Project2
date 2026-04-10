import streamlit as st
from utils import validate_email

st.title("✅ Validate Email")

email = st.text_input("Enter Email")

if st.button("Validate"):
    res = validate_email(email)

    if res.status_code == 200:
        data = res.json()
        
        if data["exists"]:
            st.warning("Email already exists ⚠️")
        else:
            st.success("Email available ✅")
    else:
        st.error("Error checking email")
