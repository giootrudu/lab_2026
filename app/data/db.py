'''INIZIALIZZAZIONE DEL DATABASE'''
from sqlalchemy.sql.annotation import Annotated
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

sqlite_file_name = "c:"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(
    sqlite_url,
    connect_args= {"check_same_thread": False},
    Echo = True
)
def init_database():
    SQLModel.metatadata.create_all(engine)

#DEPENDENCIE: DA RICHIAMARE OGNI VOLTA CHE SI HA NECESSITA' DI INTERAGIRE CON IL DATABASE
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
#session: SessionDep