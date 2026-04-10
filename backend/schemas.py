from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# -----------------------------
# 🧩 Base Schema (Common Fields)
# -----------------------------
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., ge=1, le=120)
    email: EmailStr

# -----------------------------
# ➕ Create User Schema
# -----------------------------
class UserCreate(UserBase):
    pass

# -----------------------------
# 📤 Response Schema
# -----------------------------
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True   # Required for SQLAlchemy (Pydantic v2)

# -----------------------------
# ✏️ Update User Schema (Optional)
# -----------------------------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    age: Optional[int] = Field(None, ge=1, le=120)
    email: Optional[EmailStr]

# -----------------------------
# 🔍 Email Validation Response
# -----------------------------
class EmailValidationResponse(BaseModel):
    email: EmailStr
    exists: bool
