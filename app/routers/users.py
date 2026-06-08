from email.policy import HTTP
from http.client import HTTPException

from fastapi import APIRouter
from data.db import SessionDep
from schemas.users import UserDB, UserPublic
from schemas.book import BookDB, BookPublic
from schemas.book_user_link import BookUserLink
from sqlmodel import select

users_router = APIRouter(prefix = "/users")

#API 1: Recuperare tutti gli utenti
@users_router.get("/")
def get_all_users(session: SessionDep) -> list[UserPublic]:
    """Return all users"""
    users = session.exec(select(UserDB)).all()
    return users


#API 2: Restituisce i libri presi in prestito da un utente dato l'id
@users_router.get("/{id}/books")
def get_user_books(
        id:int,
        session: SessionDep
)-> list[BookPublic]:
    """"Return all books held by the given user"""
    user = session.get(UserDB, id)
    if not user:
        raise HTTPException(404, detail = "User not found.")
    statement = select(BookDB).join(BookUserLink).where(BookUserLink.user_id == id)
    result = session.exec(statement).all()
    return result
