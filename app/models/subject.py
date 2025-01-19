from .base import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .direction_subjects import direction_subjects_per_year



class Subjects:
    choices: tuple[str] = (
        "Matematyka",
        "Fizyka",
        "WF",
        "Bazy Danych",
    )

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.choices):
            raise StopIteration
        res = self.choices[self.current_index]
        self.current_index += 1
        return res

class SubjectModel(Base):
    __tablename__: str = "subjects"
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    subjects = relationship(
        "AcademicDirectionModel",
        secondary=direction_subjects_per_year,
        back_populates="subjects"
    )
