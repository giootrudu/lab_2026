from pydantic import BaseModel, Field
from typing import Annotated

#CLASSE RIFERIMENTO PER MODIFICARE IN MANIERA OPZIONALE TITOLO E AUTORE DEL LIBRO
#PROVARE A FARE L'API PER QUESTO
class BookPatch (BaseModel):
    title: str | None = None
    author: str | None = None


class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int, Field(ge = 1, le = 5)] = None

    model_config = {
        "json_schema_extra": {
            "example": [
                {
                    "id": 1,
                    "title": "Il nome della Rosa",
                    "author": "Umberto Eco",
                    "review": 5
                }
            ]
        }
    }

books = {
    0: Book (id =0, title = "Il nome della Rosa", author = "Umberto Eco", review= 5),
    1: Book (id =1, title = "Il gioco dei sei", author = "Umberto Eco", review= 1),
    2: Book (id =2, title = "Il piccolo principe", author = "Anna Frank", review= 2)
}

print (Book.model_json_schema())