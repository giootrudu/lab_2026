from pydantic import BaseModel, Field
from typing import Annotated
from sqlmodel import SQLModel, Field

#classe radice che ha gli attributi che ripetono e che eriditano gli altri modelli
class BookBase(SQLModel):
    title: str
    author: str
    review: Annotated[int | None, Field(ge=1, le = 5)] = None


#modello relazionale che rappresenta la tabella del database
class Book(BookBase, table = True):
    id: Annotated[int, Field(default = None, primary_key = True)]

#schema per creare un nuovo libro
class BookCreate(BookBase):
    pass

#schema per restiruire le infro di un libro
class BookPublic(BookBase):
    id: int

#classe che utilizzerò quando voglio accedere al database tramite query
#passaggio da classe python a tabella database
class BookDB(BookBase, table = True):
    #nel database deve essere presente anche l'id, che deve essere la chiave primaria
    #è di default
    id: int = Field(default = None, primary_key = True)
