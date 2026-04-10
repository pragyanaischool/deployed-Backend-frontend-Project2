import requests
from config import API_URL

# -----------------------------
# CREATE USER
# -----------------------------
def create_user(data):
    return requests.post(f"{API_URL}/users", json=data)

# -----------------------------
# GET ALL USERS
# -----------------------------
def get_users():
    return requests.get(f"{API_URL}/users")

# -----------------------------
# GET USER BY ID
# -----------------------------
def get_user(user_id):
    return requests.get(f"{API_URL}/users/{user_id}")

# -----------------------------
# VALIDATE EMAIL
# -----------------------------
def validate_email(email):
    return requests.get(f"{API_URL}/validate/{email}")

# -----------------------------
# DELETE USER
# -----------------------------
def delete_user(user_id):
    return requests.delete(f"{API_URL}/users/{user_id}")
