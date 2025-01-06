from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import StudentModel
from app.database import get_session

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_students(session: Session = Depends(get_session)):
    query = select(StudentModel)
    result = await session.execute(query)
    users = result.scalars().all()
    return users


@router.get("/{id}")
async def get_post(id: str, session: Session = Depends(get_session)):
    result = await session.execute(select(StudentModel).filter(StudentModel.id == id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
