from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

#INIZIALIZZAZIONE MOTORE DI TEMPLATING: importo la libreria
from fastapi.templating import Jinja2Templates

app = FastAPI ()
#con questa riga dico alla libreria dove trovare i file html
#il punto indica cartella corrente, ma posso anche scrivere solo il nome
templates = Jinja2Templates(directory = "./templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request ):
    """Renders the home page"""
    #MOTORE DI TEMPLATING, IL PRIMO PARAMETRO SI PASSA SEMPRE DI DEFAULT
    #IL SECONDO PARAMETRO INDICA IL NOME DEL FILE HTML DA CUI DEVE PESCARE IL CODICE
    #TERZO PARAMETRO DELLA TEMPLATE RESPONSE
    context =  {"text": "Welcome to the home page !"}

    return templates.TemplateResponse(request = request, name = "home.html", context = context)



