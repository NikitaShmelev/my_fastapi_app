from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class SubjectModel(Base):
    __tablename__: str = "subjects"
    name: Mapped[str] = mapped_column(nullable=False, max_length=255)
