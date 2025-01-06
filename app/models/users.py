from .base import Base
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__: str = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, index=True, unique=True)
    age = Column(Integer, nullable=False)
