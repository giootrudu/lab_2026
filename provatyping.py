x: int = "ciao"

print(x)

#funzione con passaggio dei parametri con aspettativa, che si possono applicare anche ai parametri opzionali (default)
def compute_sum ( x: float, y: float, z: float = 0.0) -> float:
    return x + y

#genera warning perchè str significa che s si aspetta sia una stringa, ma la funzione genera un float
s: str = compute_sum(1, 4)

#stiamo specificando che la lista dovrà contenere interi
a: list[int]

#dizionario

#serie di dati
a: list | tuple | None | int