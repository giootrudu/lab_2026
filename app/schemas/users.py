from sqlmodel import SQLModel, Field
from datetime import date

# CLASSE BASE CON SCHELETRO COMUNE, sfruttando l'ereditarietà si evita la
#ripetizione di codice
class BaseUser(SQLModel):
    name: str
    birth_date: date
    city: str

# CLASSE CHE RAPPRESENTA L'OUTPUT DELLE API
# L'ID è OMESSO PER QUESTIONID ID PRIVACY
class UserPublic(BaseUser):
    pass

#CLASSE PER IL MODELLO RELAZIONALE: RAPPRESENTA LA TABELLA REALE
class UserDB(BaseUser, table=True):
    id: int = Field(default=None, primary_key=True)