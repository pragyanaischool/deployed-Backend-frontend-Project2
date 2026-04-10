from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    # -----------------------------
    # 🔑 Primary Key
    # -----------------------------
    id = Column(Integer, primary_key=True, index=True)

    # -----------------------------
    # 👤 User Fields
    # -----------------------------
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)

    # -----------------------------
    # 🧾 Representation (Optional)
    # -----------------------------
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
