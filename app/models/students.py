from .base import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .students_directions import students_directions


class StudentModel(Base):
    __tablename__: str = "students"
    fullname: Mapped[str] = mapped_column(String(255), nullable=False)
    academic_directions = relationship(
        "AcademicDirectionModel",
        secondary=students_directions,
        back_populates="students",
    )
