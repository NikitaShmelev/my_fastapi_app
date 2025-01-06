from .base import Base



from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class PostModel(Base):
    __tablename__ = 'posts'


    title = Column(String, nullable=False, index=True)
    body = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = relationship("UserModel", back_populates="posts")

