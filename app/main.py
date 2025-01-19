import uvicorn
import os

from fastapi import FastAPI, HTTPException, Depends
import httpx
from app.internal import admin
from app.routers import students, utils, professors, academic_directions

from app.models import Base
from app.database import engine


app = FastAPI()


# app.include_router(users.router)
# app.include_router(students.router)
app.include_router(utils.router)
app.include_router(academic_directions.router)
# app.include_router(professors.router)

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.post("/setup")
def setup_database():
    with engine.begin() as conn:
        Base.metadata.drop_all(bind=conn)
        Base.metadata.create_all(bind=conn)

    return {
        "created database with following tables": [
            table for table in Base.metadata.tables
        ]
    }


@app.get("/")
def root():
    return {"message": "Hello There!"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
