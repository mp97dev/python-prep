"""
Esempi di Funzioni Lambda in Python
"""

# ============================================
# 1. SINTASSI BASE LAMBDA
# ============================================

print("=== SINTASSI BASE LAMBDA ===\n")

# Funzione normale
def somma_normale(x, y):
    return x + y

# Funzione lambda equivalente
somma_lambda = lambda x, y: x + y

print(f"Somma normale: {somma_normale(5, 3)}")
print(f"Somma lambda: {somma_lambda(5, 3)}")

# Lambda con un solo argomento
quadrato = lambda x: x ** 2
print(f"Quadrato di 5: {quadrato(5)}")

# Lambda senza argomenti
saluto = lambda: "Ciao a tutti!"
print(f"Saluto: {saluto()}")

# ============================================
# 2. MAP() CON LAMBDA
# ============================================

print("\n=== MAP() CON LAMBDA ===\n")

# Applicare una funzione a tutti gli elementi di una lista
numeri = [1, 2, 3, 4, 5]

# Raddoppiare ogni numero
doppi = list(map(lambda x: x * 2, numeri))
print(f"Originale: {numeri}")
print(f"Raddoppiati: {doppi}")

# Calcolare quadrati
quadrati = list(map(lambda x: x ** 2, numeri))
print(f"Quadrati: {quadrati}")

# Convertire temperature da Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Map con più liste
numeri1 = [1, 2, 3]
numeri2 = [4, 5, 6]
somme = list(map(lambda x, y: x + y, numeri1, numeri2))
print(f"\nSomma di {numeri1} e {numeri2}: {somme}")

# ============================================
# 3. FILTER() CON LAMBDA
# ============================================

print("\n=== FILTER() CON LAMBDA ===\n")

# Filtrare numeri pari
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(f"Numeri: {numeri}")
print(f"Pari: {pari}")

# Filtrare numeri maggiori di 5
maggiori_5 = list(filter(lambda x: x > 5, numeri))
print(f"Maggiori di 5: {maggiori_5}")

# Filtrare stringhe che iniziano con 'P'
parole = ["Python", "Java", "PHP", "JavaScript", "Perl"]
con_p = list(filter(lambda x: x.startswith('P'), parole))
print(f"\nParole: {parole}")
print(f"Che iniziano con 'P': {con_p}")

# Filtrare numeri positivi
numeri_misti = [-5, -2, 0, 3, 7, -1, 9]
positivi = list(filter(lambda x: x > 0, numeri_misti))
print(f"\nNumeri misti: {numeri_misti}")
print(f"Positivi: {positivi}")

# ============================================
# 4. SORTED() CON LAMBDA
# ============================================

print("\n=== SORTED() CON LAMBDA ===\n")

# Ordinare una lista di tuple per il secondo elemento
studenti = [("Mario", 25), ("Luigi", 22), ("Anna", 28), ("Carlo", 20)]
print(f"Studenti originali: {studenti}")

# Ordinare per età
per_età = sorted(studenti, key=lambda x: x[1])
print(f"Ordinati per età: {per_età}")

# Ordinare per nome
per_nome = sorted(studenti, key=lambda x: x[0])
print(f"Ordinati per nome: {per_nome}")

# Ordinare lista di dizionari
prodotti = [
    {"nome": "Laptop", "prezzo": 999},
    {"nome": "Mouse", "prezzo": 25},
    {"nome": "Tastiera", "prezzo": 75},
    {"nome": "Monitor", "prezzo": 350}
]

print(f"\nProdotti originali:")
for p in prodotti:
    print(f"  {p}")

ordinati_prezzo = sorted(prodotti, key=lambda x: x["prezzo"])
print(f"\nOrdinati per prezzo:")
for p in ordinati_prezzo:
    print(f"  {p['nome']}: €{p['prezzo']}")

# ============================================
# 5. REDUCE() CON LAMBDA
# ============================================

print("\n=== REDUCE() CON LAMBDA ===\n")

from functools import reduce

# Somma di tutti gli elementi
numeri = [1, 2, 3, 4, 5]
somma = reduce(lambda x, y: x + y, numeri)
print(f"Numeri: {numeri}")
print(f"Somma totale: {somma}")

# Prodotto di tutti gli elementi
prodotto = reduce(lambda x, y: x * y, numeri)
print(f"Prodotto: {prodotto}")

# Trovare il massimo
massimo = reduce(lambda x, y: x if x > y else y, numeri)
print(f"Massimo: {massimo}")

# ============================================
# 6. LAMBDA CON CONDIZIONI (TERNARY)
# ============================================

print("\n=== LAMBDA CON CONDIZIONI ===\n")

# Valore assoluto
valore_assoluto = lambda x: x if x >= 0 else -x
print(f"Valore assoluto di -5: {valore_assoluto(-5)}")
print(f"Valore assoluto di 3: {valore_assoluto(3)}")

# Classificare età
classifica_età = lambda età: "Minorenne" if età < 18 else "Maggiorenne"
print(f"\n15 anni: {classifica_età(15)}")
print(f"25 anni: {classifica_età(25)}")

# Determinare pari o dispari
pari_dispari = lambda x: "pari" if x % 2 == 0 else "dispari"
for i in range(1, 6):
    print(f"{i} è {pari_dispari(i)}")

# ============================================
# 7. LAMBDA CON LISTE E DIZIONARI
# ============================================

print("\n=== LAMBDA CON STRUTTURE DATI ===\n")

# Estrarre valori da una lista di dizionari
studenti = [
    {"nome": "Mario", "voto": 28},
    {"nome": "Luigi", "voto": 30},
    {"nome": "Anna", "voto": 27}
]

nomi = list(map(lambda x: x["nome"], studenti))
voti = list(map(lambda x: x["voto"], studenti))
print(f"Nomi: {nomi}")
print(f"Voti: {voti}")

# Filtrare studenti con voto >= 28
bravi_studenti = list(filter(lambda x: x["voto"] >= 28, studenti))
print(f"\nStudenti con voto >= 28:")
for s in bravi_studenti:
    print(f"  {s['nome']}: {s['voto']}")

# ============================================
# 8. LAMBDA MULTIPLE COME DIZIONARIO
# ============================================

print("\n=== DIZIONARIO DI FUNZIONI LAMBDA ===\n")

# Creare un dizionario di operazioni
operazioni = {
    'somma': lambda x, y: x + y,
    'sottrazione': lambda x, y: x - y,
    'moltiplicazione': lambda x, y: x * y,
    'divisione': lambda x, y: x / y if y != 0 else "Errore: divisione per zero"
}

a, b = 10, 5
print(f"Numeri: a={a}, b={b}\n")
for op_nome, op_funzione in operazioni.items():
    risultato = op_funzione(a, b)
    print(f"{op_nome}: {risultato}")

# ============================================
# 9. LAMBDA ANNIDATA
# ============================================

print("\n=== LAMBDA ANNIDATA ===\n")

# Lambda che ritorna lambda
moltiplica_per = lambda x: lambda y: x * y

# Creare funzioni specializzate
raddoppia = moltiplica_per(2)
triplica = moltiplica_per(3)

print(f"Raddoppia 5: {raddoppia(5)}")
print(f"Triplica 5: {triplica(5)}")

# ============================================
# 10. ESERCIZI PRATICI
# ============================================

print("\n=== ESERCIZI PRATICI ===\n")

# Esercizio 1: Filtrare e trasformare
print("Esercizio 1: Quadrati dei numeri pari")
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati_pari = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeri)))
print(f"Numeri: {numeri}")
print(f"Quadrati dei pari: {quadrati_pari}")

print()

# Esercizio 2: Ordinare stringhe per lunghezza
print("Esercizio 2: Ordinare parole per lunghezza")
parole = ["Python", "è", "un", "linguaggio", "fantastico"]
ordinate = sorted(parole, key=lambda x: len(x))
print(f"Originale: {parole}")
print(f"Ordinate per lunghezza: {ordinate}")

print()

# Esercizio 3: Calcolare totali
print("Esercizio 3: Calcolare totale spesa")
acquisti = [
    {"prodotto": "Pane", "prezzo": 1.5, "quantità": 2},
    {"prodotto": "Latte", "prezzo": 1.2, "quantità": 1},
    {"prodotto": "Pasta", "prezzo": 0.9, "quantità": 3}
]

totale = sum(map(lambda x: x["prezzo"] * x["quantità"], acquisti))
print(f"Totale spesa: €{totale:.2f}")

print()

# Esercizio 4: Trasformare nomi
print("Esercizio 4: Trasformare nomi")
nomi = ["mario rossi", "luigi verdi", "anna bianchi"]
nomi_formattati = list(map(lambda x: x.title(), nomi))
print(f"Originale: {nomi}")
print(f"Formattati: {nomi_formattati}")

print()

# Esercizio 5: Combinare operazioni
print("Esercizio 5: Media voti superiori a 25")
voti = [22, 28, 30, 24, 27, 29, 23, 26]
voti_alti = list(filter(lambda x: x > 25, voti))
if voti_alti:
    media = sum(voti_alti) / len(voti_alti)
    print(f"Voti: {voti}")
    print(f"Voti > 25: {voti_alti}")
    print(f"Media voti alti: {media:.2f}")
