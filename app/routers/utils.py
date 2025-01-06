from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import StudentModel, UserModel
from app.database import get_session
from faker import Faker

fake = Faker()
router = APIRouter(
    prefix="/utils",
    tags=["utils"],
    responses={404: {"description": "Not found"}},
)


async def create_users(session: Session, count: int):
    for _ in range(count):
        new_user = UserModel(
            username=fake.user_name(),
            email=fake.email(),
            age=fake.random_int(min=18, max=90),
        )
        session.add(new_user)
    await session.commit()


@router.get("/populate_data")
async def populate_data(session: Session = Depends(get_session)):
    await create_users(session=session, count=10)
    return {"success": True}
