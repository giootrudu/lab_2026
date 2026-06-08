'''INIZIALIZZAZIONE DEL DATABASE'''
import os.path

from sqlalchemy.sql.annotation import Annotated
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from schemas.book import BookDB # noqa
from schemas.users import UserDB
from schemas.book_user_link import BookUserLink
from faker import Faker

# 1. Definizione del percorso del file di database
sqlite_file_name = "app/data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

# 2. Creazione del Motore (Engine)
engine = create_engine(
    sqlite_url,
    connect_args= connect_args,
    echo = True
)
def init_database() -> None:
    #Si controlla se il file del DB esiste già per evitare di inserire dati duplicati
    ds_exists = os.path.isfile(sqlite_file_name)
    # 3. Creazione fisica delel tabelle
    SQLModel.metadata.create_all(engine)
    if not ds_exists:
        # Qui usiamo il Faker per popolare il database con 10 utenti/libri fittizi
        f = Faker ("it_IT")
        with Session(engine) as session:
            for i in range(10):
                book = BookDB(
                    title = f.sentence(nb_words=5),
                    author = f.name(),
                    review = f.pyint(1, 5))
                session.add(book)
            session.commit()
            for i in range (10):
                user = UserDB(
                    name=f.name(),
                    birth_date = f.date_of_birth(),
                    city= f.city())
                session.add(user)
            session.commit()
            for i in range(5):
                link = BookUserLink(
                    book_id = f.pyint(1, 10),
                    user_id = f.pyint(1, 10))
                session.add(link)
            session.commit()

#DEPENDENCY INJECTION: DA RICHIAMARE OGNI VOLTA CHE SI HA NECESSITA' DI INTERAGIRE CON IL DATABASE
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
#session: SessionDep. session è una variabile che prende il formato SessionDep
#SessionDep è il Tipo che indica una sessione di database gestita e aperta automaticamente
#da fastAPI