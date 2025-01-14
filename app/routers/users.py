from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import UserModel
from app.database import get_session
from app.schemas import UserCreate, UserResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_users(session: Session = Depends(get_session)):
    query = select(UserModel)
    result = session.execute(query)
    users = result.scalars().all()
    return users


@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    result = session.execute(select(UserModel).filter(UserModel.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse)
def create_user(user_create: UserCreate, session: Session = Depends(get_session)):
    new_user = UserModel(
        username=user_create.username,
        email=user_create.email,
        age=user_create.age,
    )
    session.add(new_user)

    try:
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")

    return new_user
