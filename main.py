from fastapi import FastAPI
app = FastAPI ()

@app.get("/")
#cioò all'interno delle parentesi della funzione endpoint, sono i parametri d'ingresso della richiesta
#si possono inserire anche parametri di default e quindi facoltativi
#TYPING--->in FASTAPI rispetto PYTHON è reso obbligatorio in runtime, e segnala errore in presenza di errore
def hello_world(q: str, sort: bool = False) -> dict[str, bool | str]:
    return {"q": q, "sort": sort}

@app.get("/home")
def homepage ():
    return "This is the homepage"

#endpoint
#anche devo usare il typing e specificare che username deve essere una stringa
@app.get("/{username}")
def username_webpage (username: str):
    return f"This is the webpage of user {username}"
#f sta er format, se non lo mettessi l'output risulterebbe una semplice stringa
#mentre con la f, appena trova le parentesi grafe, prende il parametro all'interno e lo stampa

#endpoint
#devo usare il typing e specificare che username deve essere una stringa
#username è parametrico e dev'essere una stringa, orders è una pagina fissa, e order_id è parametrico e dev'essere un intero

#N.B. POSSO ANCHE COMBINARE PARAMETRI DI DIVERSE APPLICAZIONI, E L'ORDINE NON CONTA PERCHE' FASTAPI RICONOSCE IN BASE AI NOMI
#L'UNICO ORDINE DA RISPETTARE E' CHE IN PYTHON I PARAMETRI OPZIONALI DEVONO ESSERE INSERITI PER FORZA PER ULTIMI
@app.get("/{username}/orders/{order_id}")
def orders_webpage (username: str, order_id: int, q: int, sort:bool = False):
    return f"This is the order {order_id} of user {username}. q: {q}, Sorted: {sort}"
#f sta er format, se non lo mettessi l'output risulterebbe una semplice stringa
#mentre con la f, appena trova le parentesi grafe, prende il parametro all'interno e lo stampa


