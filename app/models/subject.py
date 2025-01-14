from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class SubjectModel(Base):
    __tablename__: str = "subjects"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
