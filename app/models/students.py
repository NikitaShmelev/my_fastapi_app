from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class StudentModel(Base):
    __tablename__: str = "students"
    fullname: Mapped[str] = mapped_column(nullable=False, max_length=255)
