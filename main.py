from fastapi import FastAPI
app = FastAPI ()

@app.get("/")
#cioò all'interno delle parentesi della funzione endpoint, sono i parametri d'ingresso della richiesta
#si possono inserire anche parametri di default e quindi facoltativi
#TYPING--->in FASTAPI rispetto PYTHON è reso obbligatorio in runtime, e segnala errore in presenza di errore
def home():
    """Renders the home page"""
    html = """
    <!DOCTYPE html>
    <html>
    <body> 
    <h1> Hello World! </h1>
    <p> This is a simple FASTAPI app.</p>
    </body>
    </html>
    """

    return html



