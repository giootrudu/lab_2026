'''INIZIALIZZAZIONE DEL DATABASE'''
from sqlmodel import create_engine, SQLmodel, Session

sqlite_file_name = "c:"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args= {"check_same_thread": False} )