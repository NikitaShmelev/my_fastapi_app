import uvicorn
import os
from fastapi import FastAPI

from app.internal import admin
from app.routers import posts, users, students

from app.models import Base
from app.database import engine


app = FastAPI()


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(students.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.post("/setup")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"created database with following tables":
                [table for table in Base.metadata.tables]
            }


@app.get("/")
async def root():
    return {"message": "Hello There!"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
