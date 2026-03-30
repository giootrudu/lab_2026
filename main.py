from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel

#INIZIALIZZAZIONE MOTORE DI TEMPLATING: importo la libreria
from fastapi.templating import Jinja2Templates

#MODELLO PYDANTIC PER RAPPRESENTARE UN PRODOTTO

class Product (BaseModel):
    name: Annotated[str, Field(min_length=3, max_length= 30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3)]


app = FastAPI ()
#con questa riga dico alla libreria dove trovare i file html
#il punto indica cartella corrente, ma posso anche scrivere solo il nome
app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory = "./templates")

#LISTA DI PRODOTTI INSERITI IN BACKEND
product_list = [Product(name = "Notebook", price = 50.00, location = "Cagliari"),
                Product(name = "Smartphone Samsung", price = 250.00, location = "Sestu")
]
@app.get("/", response_class=HTMLResponse)
def home(request: Request ):
    """Renders the home page"""
    #MOTORE DI TEMPLATING, IL PRIMO PARAMETRO SI PASSA SEMPRE DI DEFAULT
    #IL SECONDO PARAMETRO INDICA IL NOME DEL FILE HTML DA CUI DEVE PESCARE IL CODICE
    #TERZO PARAMETRO DELLA TEMPLATE RESPONSE


    return templates.TemplateResponse(request = request,
                                      name = "home.html",
                                      context = {"text": "Welcome to the store"}
                                      )

@app.get ("/products", response_class = HTMLResponse)
def products (request: Request):
    return templates.TemplateResponse(request = request,
                                      name = "products.html",
                                      context = {"product_list": product_list})

@app.get ("/products_form", response_class = HTMLResponse)
def products_form (request: Request):
        return templates.TemplateResponse(request = request,
                                          name = "products_form.html"
                                          )

#END POINT CHE RACCOGLIE I DATI DEL FORM CHE UTILIZZA IL MODELLO PYDANTIC
@app.post ("/insert_product")
def insert_product (product: Annotated[Product, Form()]
                    ):
    product_list.append(product)
    return "Product added successfully"


