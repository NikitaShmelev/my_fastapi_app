import uvicorn
from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from internal import admin
from routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8080))  # Default to 8080 if PORT is unset
    uvicorn.run("main:app", host="0.0.0.0", port=port)

