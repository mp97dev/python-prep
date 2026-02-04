"""
Esempi di Variabili e Tipi di Dati in Python
"""

# ============================================
# 1. TIPI DI DATI PRIMITIVI
# ============================================

# Interi
numero_intero = 42
età = 25
anno = 2024

print(f"Numero intero: {numero_intero}, tipo: {type(numero_intero)}")

# Float (numeri decimali)
pi_greco = 3.14159
temperatura = -15.5
prezzo = 19.99

print(f"Float: {pi_greco}, tipo: {type(pi_greco)}")

# Stringhe
nome = "Mario Rossi"
messaggio = 'Benvenuto in Python!'
testo_multiriga = """Questo è un testo
che si estende su
più righe"""

print(f"Stringa: {nome}, tipo: {type(nome)}")

# Booleani
is_studente = True
ha_superato_esame = False

print(f"Booleano: {is_studente}, tipo: {type(is_studente)}")

# ============================================
# 2. STRUTTURE DATI
# ============================================

# Liste (mutabili)
numeri = [1, 2, 3, 4, 5]
frutti = ["mela", "banana", "arancia"]
mista = [1, "due", 3.0, True]

print(f"\nLista: {numeri}")
numeri.append(6)  # Aggiunge elemento
print(f"Lista dopo append: {numeri}")

# Tuple (immutabili)
coordinate = (10, 20)
giorni_settimana = ("Lunedì", "Martedì", "Mercoledì")

print(f"\nTupla: {coordinate}, tipo: {type(coordinate)}")

# Dizionari
studente = {
    "nome": "Mario",
    "cognome": "Rossi",
    "età": 22,
    "matricola": "12345"
}

print(f"\nDizionario: {studente}")
print(f"Nome studente: {studente['nome']}")

# Set (insiemi)
numeri_unici = {1, 2, 3, 4, 5}
colori = {"rosso", "verde", "blu"}

print(f"\nSet: {numeri_unici}, tipo: {type(numeri_unici)}")

# ============================================
# 3. OPERAZIONI SU VARIABILI
# ============================================

# Operazioni aritmetiche
a = 10
b = 3

somma = a + b
differenza = a - b
prodotto = a * b
divisione = a / b
divisione_intera = a // b
resto = a % b
potenza = a ** b

print(f"\n--- Operazioni Aritmetiche ---")
print(f"{a} + {b} = {somma}")
print(f"{a} - {b} = {differenza}")
print(f"{a} * {b} = {prodotto}")
print(f"{a} / {b} = {divisione}")
print(f"{a} // {b} = {divisione_intera}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {potenza}")

# Operazioni su stringhe
nome = "Mario"
cognome = "Rossi"

nome_completo = nome + " " + cognome  # Concatenazione
ripetuto = nome * 3  # Ripetizione

print(f"\n--- Operazioni su Stringhe ---")
print(f"Nome completo: {nome_completo}")
print(f"Ripetuto: {ripetuto}")
print(f"Lunghezza: {len(nome_completo)}")
print(f"Maiuscolo: {nome_completo.upper()}")
print(f"Minuscolo: {nome_completo.lower()}")

# ============================================
# 4. CONVERSIONE DI TIPO (TYPE CASTING)
# ============================================

# String to int
stringa_numero = "42"
numero = int(stringa_numero)
print(f"\n--- Type Casting ---")
print(f"Stringa '{stringa_numero}' -> int {numero}")

# String to float
stringa_float = "3.14"
numero_float = float(stringa_float)
print(f"Stringa '{stringa_float}' -> float {numero_float}")

# Int to string
numero_originale = 100
stringa = str(numero_originale)
print(f"Int {numero_originale} -> string '{stringa}'")

# ============================================
# 5. ASSEGNAZIONE MULTIPLA
# ============================================

# Assegnazione simultanea
x, y, z = 1, 2, 3
print(f"\n--- Assegnazione Multipla ---")
print(f"x={x}, y={y}, z={z}")

# Swap di variabili
x, y = y, x
print(f"Dopo lo swap: x={x}, y={y}")

# Unpacking
coordinate = (5, 10)
lat, lon = coordinate
print(f"Latitudine: {lat}, Longitudine: {lon}")

# ============================================
# 6. VARIABILI NONE
# ============================================

risultato = None
print(f"\n--- None Type ---")
print(f"Risultato: {risultato}, tipo: {type(risultato)}")

# Controllo se una variabile è None
if risultato is None:
    print("La variabile è None")

# ============================================
# 7. SCOPE DELLE VARIABILI
# ============================================

# Variabile globale
variabile_globale = "Sono globale"

def esempio_scope():
    # Variabile locale
    variabile_locale = "Sono locale"
    print(f"Dentro la funzione: {variabile_locale}")
    print(f"Accesso alla globale: {variabile_globale}")

print(f"\n--- Scope ---")
esempio_scope()
print(f"Fuori dalla funzione: {variabile_globale}")
# print(variabile_locale)  # Questo darebbe errore!

# ============================================
# 8. CONSTANTI (convenzione)
# ============================================

# In Python non esistono vere costanti, ma per convenzione
# si usano nomi in MAIUSCOLO per indicare valori che non dovrebbero cambiare
PI = 3.14159
VELOCITA_LUCE = 299792458  # m/s
MAX_STUDENTI = 100

print(f"\n--- Costanti (convenzione) ---")
print(f"PI = {PI}")
print(f"Velocità della luce = {VELOCITA_LUCE} m/s")

# ============================================
# 9. ESERCIZIO PRATICO
# ============================================

print(f"\n--- Esercizio Pratico ---")

# Calcolare l'area e il perimetro di un rettangolo
base = 5
altezza = 3

area = base * altezza
perimetro = 2 * (base + altezza)

print(f"Rettangolo con base={base} e altezza={altezza}")
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

# Gestire i dati di uno studente
studente = {
    "nome": "Anna",
    "cognome": "Verdi",
    "voti": [28, 30, 27, 29],
    "crediti": 120
}

media_voti = sum(studente["voti"]) / len(studente["voti"])
print(f"\nStudente: {studente['nome']} {studente['cognome']}")
print(f"Media voti: {media_voti:.2f}")
print(f"Crediti acquisiti: {studente['crediti']}")
