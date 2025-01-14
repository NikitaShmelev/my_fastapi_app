import random

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import StudentModel, UserModel, ProfessorModel, AcademicDirectionModel, Base
from app.database import get_session
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

fake = Faker()
router = APIRouter(
    prefix="/setup",
    # tags=["utils"],
)


def create_academic_directions(session: Session):
    directions = (
        "Informatyka Techniczna",
        "Informatyka Stosowana",
    )

    for direction in directions:
        direction_obj = AcademicDirectionModel(name=direction)
        session.add(direction_obj)

    session.commit()


def assign_professors_to_academic_directions(session: Session):
    professors = session.execute(select(ProfessorModel)).scalars().all()
    directions = session.execute(select(AcademicDirectionModel)).scalars().all()

    for professor in professors:
        direction = random.choice(directions)
        professor.academic_directions.append(direction)
    session.commit()

def create_users(session: Session, count: int):
    for _ in range(count):
        new_user = UserModel(
            username=fake.user_name(),
            email=fake.email(),
            age=fake.random_int(min=18, max=90),
        )
        session.add(new_user)
    session.commit()


def create_students(session: Session, count: int):
    for _ in range(count):
        student = StudentModel(
            fullname=fake.user_name(),
        )
        session.add(student)
    session.commit()


def create_professors(session: Session, count: int):
    for _ in range(count):
        professor = ProfessorModel(
            fullname=fake.user_name(),
        )
        session.add(professor)
    session.commit()


def add_directions_to_students(session: Session):
    students = session.execute(select(StudentModel)).scalars().all()
    directions = session.execute(select(AcademicDirectionModel)).scalars().all()

    for student in students:
        direction = random.choice(directions)
        student.academic_directions.append(direction)
    session.commit()


@router.get("/populate_data")
def populate_data(session: Session = Depends(get_session)):
    create_academic_directions(session)

    create_users(session=session, count=10)
    create_students(session=session, count=50)
    create_professors(session=session, count=7)

    add_directions_to_students(session=session)
    assign_professors_to_academic_directions(session=session)

    return {"success": True}
