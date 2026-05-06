from pydantic import BaseModel, Field
from typing import Annotated
from sqlmodel import SQLModel, Field

#CLASSE RIFERIMENTO PER MODIFICARE IN MANIERA OPZIONALE TITOLO E AUTORE DEL LIBRO
#AGGIORNARE IN MANIERA PARZIALE LA CLASSE
#PROVARE A FARE L'API PER QUESTO
class BookPatch (BaseModel):
    title: str | None = None
    author: str | None = None

#classe radice che ha gli attributi che ripetono e che eriditano gli altri modelli
class BookBase(SQLModel):
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le = 5)] = None

class BookCreate(BookBase):
    pass

#schema che viene utilizzato nelle get, in cui voglio che ci sia anche l'id delle risorse
class BookPublic(BookBase):
    id: int

#classe che utilizzerò quando voglio accedere al database tramite query
#passaggio da classe python a tabella database
class BookDB(BookBase, table = True):
    #nel database deve essere presente anche l'id, che deve essere la chiave primaria
    #è di default
    id: int = Field(default = None, primary_key = True)
