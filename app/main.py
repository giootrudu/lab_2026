from fastapi import FastAPI
from routers.books import book_router

app = FastAPI()
app.include_router(book_router)