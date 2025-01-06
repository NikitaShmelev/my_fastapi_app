from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import PostModel
from app.database import get_session
from app.schemas import PostCreate, PostResponse
router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)




@router.get("/")
async def get_posts(session: Session = Depends(get_session)):
    query = select(PostModel)
    result = await session.execute(query)
    users = result.scalars().all()
    return users


@router.get("/{post_id}")
async def get_post(post_id: str, session: Session = Depends(get_session)):
    result = await session.execute(select(PostModel).filter(PostModel.id == post_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item



@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate, session: Session = Depends(get_session)):
    new_post = PostModel(
        title=post.title,
        body=post.body,
        user_id=post.user_id,
    )

    session.add(new_post)

    try:
        await session.commit()
        await session.refresh(new_post)  # Get the latest data including default fields
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="Error creating post. Ensure user exists.")

    return new_post