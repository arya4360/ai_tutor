from sqlalchemy import Column, Integer, String
from app.core.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, index=True)