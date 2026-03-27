from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#INIZIALIZZAZIONE MOTORE DI TEMPLATING: importo la libreria
from fastapi.templating import Jinja2Templates

app = FastAPI ()
#con questa riga dico alla libreria dove trovare i file html
#il punto indica cartella corrente, ma posso anche scrivere solo il nome
app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory = "./templates")

product_list = [
    {"name": "notebook LENOVO", "price": 2999.99, "location": "Cagliari"},
    {"name": "samsung 500", "price": 500, "location": "Sestu"}
]
@app.get("/", response_class=HTMLResponse)
def home(request: Request ):
    """Renders the home page"""
    #MOTORE DI TEMPLATING, IL PRIMO PARAMETRO SI PASSA SEMPRE DI DEFAULT
    #IL SECONDO PARAMETRO INDICA IL NOME DEL FILE HTML DA CUI DEVE PESCARE IL CODICE
    #TERZO PARAMETRO DELLA TEMPLATE RESPONSE


    return templates.TemplateResponse(request = request, name = "home.html", context = {"test": "Welcome to the store"})

@app.get ("/products", response_class = HTMLResponse)
def products (request: Request):
    return templates.TemplateResponse(request = request, name = "products.html", context = {"product_list": product_list})



