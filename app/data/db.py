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

sqlite_file_name = "app/data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(
    sqlite_url,
    connect_args= connect_args,
    echo = True
)
def init_database() -> None:
    ds_exists = os.path.isfile(sqlite_file_name)
    SQLModel.metadata.create_all(engine)
    if not ds_exists:
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

#DEPENDENCIE: DA RICHIAMARE OGNI VOLTA CHE SI HA NECESSITA' DI INTERAGIRE CON IL DATABASE
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
#session: SessionDep