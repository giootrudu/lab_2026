'''IN QUESTO FILE PYHTON VADO A DICHIARARE TUTTE LE MIE FASTAPI, OSSIA LE APPLICAZIONI RICHIESTE'''
from fastapi import APIRouter, Path, HTTPException, Query
from schemas.book import BookCreate, BookPublic, BookDB
from typing import Annotated
from schemas.review import Review
from data.db import  SessionDep
from sqlmodel import select, delete


book_router = APIRouter(prefix="/books", tags = ["books"])
#Il collegamento al database avviene in ogni singola funzione
# grazie al parametro session: SessionDep
# la sessione verso il database viene aperta e salvata nella variabile locale session
#si usa session per interrogare, aggiungere o eliminare i dati
# al termine della funzione fastAPI invia il json al client e chiude la sessione

#PRIMA API: lettura di tutti i libri
#IN UN SECONDO TEMPO UTILIZZIAMO LA FUNZIONE QUERY PER ORDINARE I LIBRI IN BASE ALLA RECENSIONE
@book_router.get("/")
def get_all_books(
        session: SessionDep,
        sort: Annotated[bool, Query(description= "Sort books by their review")] = False,
) -> list[BookPublic]:
    """Returns the list of aviable books"""
    books = session.exec(select(BookDB)).all()
    if sort:
       return sorted(books, key = lambda book: book.review)
    else:
       return list(books)

#SECONDA API: lettura di un libro specifico tramite id
@book_router.get("/{id}")
def get_book_by_id(
        session: SessionDep,
        id: Annotated[int, Path(description = "The ID of the book retrieve")]
)  -> BookPublic:
    """Returns the book with the given id"""
    book = session.get(BookDB, id)
    if book:
        return book
    else:
        raise HTTPException(status_code = 404, detail = "Book not found")


#TERZA API: aggiunta di una recensione su uno specifico libro
@book_router.post("/{id}/review")
def add_review (
        session: SessionDep,
        id: Annotated[int, Path(description= "The ID of the book review to which add the review")],
        review: Review
):
    """Add a review to the book with the given ID"""
    #anche in questo caso se l'id non è valido mando l'errore
    book = session.get(BookDB, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.review = review.review
    session.add(book)
    session.commit()
    return "Review added successfully"

#QUARTA API: aggiungere un libro al database
@book_router.post("/")
def add_book (session: SessionDep, book: BookCreate):
    """Adds a new book"""
    #conversione del json/modello pydantic in un'entità del databas relazionale
    book_entry = BookDB.model_validate(book)
    session.add(book_entry)
    session.commit
    return ("Book successfully added")

# QUINTA API: aggiornare un libro dato un certo id
@book_router.put("/{id}")
def update_book (
        session: SessionDep,
        id: Annotated[int, Path (description= "The ID of the book to update")],
        new_book:BookCreate
):
   """UPDATES THE BOOK WITH THE GIVEN ID"""
   #per prima cosa devo verificare che il libro esista, altrimenti mando un errore
   book = session.get(BookDB, id)
   if not book:
     raise HTTPException(status_code=404, detail = "Book not found")
   book.title = new_book.title
   book.author = new_book.author
   book.review = new_book.review
   session.add(book)
   session.commit()
   return "Book replaced successfully"

# SESTA API: eliminare tutti i libri
@book_router.delete("/")
def delete_book (session: SessionDep):
    """DELETE A BOOK"""
    session.exec(delete(BookDB))
    session.commit()
    return "All books are deleted successfully"

# SETTIMA API: eliminare un libro dato lo specifico id
@book_router.delete("/{id}")
def delete_book (
        session: SessionDep,
        id: Annotated[int, Path(description =  "The ID of the book to delete")]):
    """Delete the book with the given id"""
    book = session.get(BookDB, id)
    if not book:
        raise HTTPException (status_code= 404, detail = "Book not found")
    session.delete(book)
    session.commit()
    return "Book deleted successfully"
