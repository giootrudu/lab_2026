from fastapi import FastAPI
from routers.books import book_router
from contextlib import asynccontextmanager
from data.db import init_database
from routers.users import users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #on start
    init_database()
    yield
    #on close
app = FastAPI(lifespan= lifespan)
app.include_router(book_router)
app.include_router(users_router)