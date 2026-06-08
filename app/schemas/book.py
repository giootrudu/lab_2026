from typing import Annotated
from sqlmodel import SQLModel, Field

#classe radice che ha gli attributi che ripetono e che eriditano gli altri modelli
class BookBase(SQLModel):
    title: str
    author: str
    review: Annotated[int | None, Field(ge=1, le = 5)] = None


#schema per creare un nuovo libro
#INPUT DELLE API: al momento dell'invio del JSON tramite richiesta POST
# l'utente non deve inviare l'ID in quanto lo genera automaticamente il server (database)
class BookCreate(BookBase):
    pass

#schema per restiruire le infro di un libro
#ha accesso al DATABASE E DEVE poter inviare un ID per effettuare la ricerca
class BookPublic(BookBase):
    id: int

#CLASSE CHE RAPPRESENTA IL MODELLO RELAZIONALE
#classe che utilizzerò quando voglio accedere al database tramite query
#passaggio da classe python a tabella database

class BookDB(BookBase, table = True):
    #nel database deve essere presente anche l'id, che deve essere la chiave primaria
    #è di default
    id: int = Field(default = None, primary_key = True)
