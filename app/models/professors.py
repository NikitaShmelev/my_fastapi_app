from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProfessorModels(Base):
    __tablename__: str = "professor"
    fullname: Mapped[str] = mapped_column(nullable=False, max_length=255)
