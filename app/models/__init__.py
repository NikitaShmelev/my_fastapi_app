from .base import Base
from .students import StudentModel
from .subject import SubjectModel, Subjects
from .professors import ProfessorModel
from .academic_directions import AcademicDirectionModel, Directions
from .students_directions import students_directions


__all__ = [
    "Base",
    "StudentModel",
    "SubjectModel",
    "ProfessorModel",
    "AcademicDirectionModel",
    "students_directions",
    "Directions",
    "Subjects",
]
