from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import StudentModel, AcademicDirectionModel
from app.database import get_session
from app.schemas import StudentCreate, StudentUpdate, AssignDirections
router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_students(session: Session = Depends(get_session)):
    query = select(StudentModel)
    result = session.execute(query)
    users = result.scalars().all()
    return users


@router.get("/{id}")
def get_student(id: str, session: Session = Depends(get_session)):
    result = session.execute(select(StudentModel).filter(StudentModel.id == id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, session: Session = Depends(get_session)):
    new_student = StudentModel(fullname=student.fullname)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    return new_student

@router.put("/{id}")
def update_student(
    id: int, student: StudentUpdate, session: Session = Depends(get_session)
):
    existing_student = (
        session.execute(select(StudentModel).filter_by(id=id))
        .scalars()
        .first()
    )
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    if student.fullname:
        existing_student.fullname = student.fullname

    session.commit()
    session.refresh(existing_student)
    return existing_student


@router.post("/{id}/assign_directions")
def assign_directions_to_student(
        id: int,
        assign_directions: AssignDirections,
        session: Session = Depends(get_session)
):
    student = (
        session.execute(select(StudentModel).filter_by(id=id))
        .scalars()
        .first()
    )
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Get the directions by the provided ids
    directions = (
        session.execute(select(AcademicDirectionModel).filter(
            AcademicDirectionModel.id.in_(assign_directions.academic_direction_ids)))
        .scalars()
        .all()
    )

    if len(directions) != len(assign_directions.academic_direction_ids):
        raise HTTPException(status_code=404, detail="Some directions not found")

    # Add the directions to the student
    student.academic_directions.extend(directions)

    session.commit()
    session.refresh(student)
    return {"message": "Directions assigned successfully",
            "academic_directions": [direction.name for direction in directions]}


@router.post("/{id}/remove_directions")
def remove_directions_from_student(
        id: int,
        remove_directions: AssignDirections,
        session: Session = Depends(get_session)
):
    student = (
        session.execute(select(StudentModel).filter_by(id=id))
        .scalars()
        .first()
    )
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Get the directions by the provided ids
    directions = (
        session.execute(select(AcademicDirectionModel).filter(
            AcademicDirectionModel.id.in_(remove_directions.academic_direction_ids)))
        .scalars()
        .all()
    )

    # Remove the directions from the student's academic_directions relationship
    directions_to_remove = set(directions)
    student.academic_directions = [d for d in student.academic_directions if d not in directions_to_remove]

    session.commit()
    session.refresh(student)
    return {"message": "Directions removed successfully",
            "academic_directions": [direction.name for direction in student.academic_directions]}