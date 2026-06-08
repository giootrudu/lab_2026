from sqlmodel import SQLModel, Field

# RELAZIONE MOLTI A MOLTI: TABELLA PONTE CHE PERMETTE
# DI COLLEGARE DIRETTAMENTE DUE TABELLE:
# un utente può prendere in prestito molti libri diversi e
# un singolo libro può essere preso in prestito (in tempi diversi) da molti utenti diversi

# tabella con chiave primaria composta
class BookUserLink(SQLModel, table = True):
    book_id: int = Field(foreign_key = "bookdb.id", primary_key = True)
    user_id: int = Field(foreign_key ="userdb.id", primary_key = True)
