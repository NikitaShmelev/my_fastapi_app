from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def update_admin():
    return {"message": "Admin getting schwifty"}
