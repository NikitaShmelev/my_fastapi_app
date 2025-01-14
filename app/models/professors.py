from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .professor_directions import professors_directions

class ProfessorModel(Base):
    __tablename__: str = "professors"
    fullname: Mapped[str] = mapped_column(String(255), nullable=False)
    academic_directions = relationship(
        "AcademicDirectionModel",
        secondary=professors_directions,
        back_populates="professors",
    )
