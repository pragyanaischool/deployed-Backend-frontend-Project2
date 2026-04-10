from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
from database import engine, SessionLocal

# -----------------------------
# 🚀 CREATE TABLES
# -----------------------------
models.Base.metadata.create_all(bind=engine)

# -----------------------------
# 🚀 INIT APP
# -----------------------------
app = FastAPI(
    title="User Management API",
    description="FastAPI + PostgreSQL + Render Deployment",
    version="1.0"
)

# -----------------------------
# 🌐 CORS (IMPORTANT for Streamlit)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to Streamlit URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# 🧠 DB SESSION DEPENDENCY
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# 🏠 ROOT
# -----------------------------
@app.get("/")
def home():
    return {"message": "FastAPI Backend Running 🚀"}

# -----------------------------
# ❤️ HEALTH CHECK
# -----------------------------
@app.get("/health")
def health():
    return {"status": "running"}

# -----------------------------
# ➕ CREATE USER
# -----------------------------
@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check duplicate email
    existing = db.query(models.User).filter(models.User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# -----------------------------
# 📋 GET ALL USERS
# -----------------------------
@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# -----------------------------
# 🔍 GET USER BY ID
# -----------------------------
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# -----------------------------
# 🔎 VALIDATE EMAIL
# -----------------------------
@app.get("/validate/{email}")
def validate_user(email: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == email).first()

    return {
        "email": email,
        "exists": bool(user)
    }

# -----------------------------
# ❌ DELETE USER (OPTIONAL)
# -----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}

# -----------------------------
# ✏️ UPDATE USER (OPTIONAL)
# -----------------------------
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_user.name
    user.age = updated_user.age
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    return user
