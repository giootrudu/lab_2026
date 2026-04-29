'''IN QUESTO FILE PYHTON VADO A DICHIARARE TUTTE LE MIE FASTAPI, OSSIA LE APPLICAZIONI RICHIESTE'''
from fastapi import APIRouter, Path, HTTPException, Query
from schemas.book import Book, books
from typing import Annotated
from schemas.review import Review


book_router = APIRouter(prefix="/books", tags = ["books"])

#PRIMA API CHE MI SERVE PER RECUPERARE LA LISTA DEI LIBRI
#IN UN SECONDO TEMPO UTILIZZIAMO LA FUNZIONE QUERY PER ORDINARE I LIBRI IN BASE ALLA RECENSIONE
@book_router.get("/")
def get_all_books(
        sort: Annotated[bool, Query(description= "Sort books by their review")] = False

) -> list[Book]:
    """Returns the list of aviable books"""
    if sort:
       sorted(books.values(), key = lambda book: book.review)
    return list(books.values())

#SECONDA API CHE RESTITUISCE UN SINGOLO LIBRO IN BASE ALL'ID
@book_router.get("/{id}")
def get_book_by_id(
        id: Annotated[int, Path(description = "The ID of the book retrieve")]
)  -> Book:
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
        books[id].review = review.review
        return "Review added succefully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")



#QUARTA API PER AGGIUNGERE UN LIBRO
@book_router.post("/")
def add_book (book: Book):
    """Adds a new book"""
    #CHECK PER NON SOSTITUIRE UN LIBRO
    if book.id in books:
        raise HTTPException(status_code = 403, detail = "Book already exists")
    books[book.id] = book
    return "Book added successfully"

@book_router.put("/{id}")
def replace_book (
        id: Annotated[int, Path (description= "The ID of the book to update")],
        book:Book
):
   """UPDATE A BOOK"""
   #per prima cosa devo verificare che il libro esista, altrimenti mando un errore
   if not id in books:
    raise HTTPException(status_code=404, detail = "Book not found")
   books[id] = book
   return "Book replaced successfully"

@book_router.delete("/")
def delete_book ():
    """DELETE A BOOK"""
    books.clear()
    return "All books are deleted successfully"

@book_router.delete("/{id}")
def delete_book (
        id: Annotated[int, Path(description =  "The ID of the book to delete")]):
    """Delete the book with the given id"""
    if not id in books:
        raise HTTPException(status_code = 404, detail = "Book not found")
    del books[id]
    return "Book deleted successfully"
