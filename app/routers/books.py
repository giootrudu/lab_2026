'''IN QUESTO FILE PYHTON VADO A DICHIARARE TUTTE LE MIE FASTAPI, OSSIA LE APPLICAZIONI RICHIESTE'''
from fastapi import APIRouter, Path, HTTPException
from schemas.book import Book, books
from typing import Annotated
from schemas.review import Review


book_router = APIRouter(prefix="/books", tags = ["books"])

#PRIMA API CHE MI SERVE PER RECUPERARE LA LISTA DEI LIBRI
@book_router.get("/")
def get_all_books() -> list[Book]:
    """Returns the list of aviable books"""
    return books.values()

#SECONDA API CHE RESTITUISCE UN SINGOLO LIBRO IN BASE ALL'ID
@book_router.get("/{id}")
def get_book_by_id(
        id: Annotated[int, Path(description = "The ID of the book retrieve")]) \
        -> Book:
    """Returns the book with the given id"""
    try:
        books[id].review = Review.review
        return ("Review added successfully")
    except KeyError:
        raise HTTPException(status_code = 404, detail = "Book not found")

#TERZA API CHE PERMETTE DI INSERIRE UNA RECENSIONE
@book_router.post("/{id}/review")
def add_review (
        id: Annotated[int, Path(description= "The ID of the book review")],
        review: Review
):
    """Add a review to the book"""
    #anche in questo caso de l'id non è valido mando l'errore
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
