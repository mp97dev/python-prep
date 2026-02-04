"""
Esempi di Cicli (Loops) in Python
"""

# ============================================
# 1. FOR LOOP - BASE
# ============================================

print("=== FOR LOOP BASE ===\n")

# Iterare su una lista
frutti = ["mela", "banana", "arancia", "pera"]
for frutto in frutti:
    print(f"Frutto: {frutto}")

print()

# Iterare su una stringa
parola = "Python"
for lettera in parola:
    print(lettera, end=" ")
print("\n")

# ============================================
# 2. FOR LOOP CON RANGE
# ============================================

print("=== FOR LOOP CON RANGE ===\n")

# Range da 0 a n-1
print("Range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

# Range con inizio e fine
print("Range(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print("\n")

# Range con step
print("Range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

# Range decrescente
print("Range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# ============================================
# 3. ENUMERATE
# ============================================

print("\n=== ENUMERATE ===\n")

linguaggi = ["Python", "Java", "JavaScript", "C++"]
for indice, linguaggio in enumerate(linguaggi):
    print(f"{indice}: {linguaggio}")

print()

# Enumerate con inizio personalizzato
for indice, linguaggio in enumerate(linguaggi, start=1):
    print(f"#{indice} - {linguaggio}")

# ============================================
# 4. ZIP
# ============================================

print("\n=== ZIP ===\n")

nomi = ["Mario", "Luigi", "Anna"]
voti = [28, 30, 27]
città = ["Roma", "Milano", "Napoli"]

for nome, voto, città in zip(nomi, voti, città):
    print(f"{nome} da {città} ha preso {voto}")

# ============================================
# 5. WHILE LOOP
# ============================================

print("\n=== WHILE LOOP ===\n")

# While base
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print()

# While con input dell'utente (simulato)
numero = 1
print("Somma numeri fino a 10:")
somma = 0
while numero <= 10:
    somma += numero
    numero += 1
print(f"Somma totale: {somma}")

# ============================================
# 6. BREAK
# ============================================

print("\n=== BREAK ===\n")

# Cercare un elemento
numeri = [1, 5, 8, 12, 15, 20, 25]
target = 12

for num in numeri:
    if num == target:
        print(f"Trovato {target}!")
        break
    print(f"Controllo {num}...")

print()

# While con break
print("Cerca primo numero divisibile per 7:")
numero = 50
while True:
    if numero % 7 == 0:
        print(f"Trovato: {numero}")
        break
    numero += 1

# ============================================
# 7. CONTINUE
# ============================================

print("\n=== CONTINUE ===\n")

# Saltare i numeri pari
print("Numeri dispari da 1 a 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta l'iterazione corrente
    print(i, end=" ")
print("\n")

# Saltare valori specifici
print("Numeri tranne multipli di 3:")
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# ============================================
# 8. ELSE CON CICLI
# ============================================

print("\n=== ELSE CON CICLI ===\n")

# For-else (eseguito se il ciclo completa normalmente)
numeri = [1, 3, 5, 7, 9]
for num in numeri:
    if num % 2 == 0:
        print("Trovato numero pari!")
        break
else:
    print("Nessun numero pari trovato")

print()

# While-else
count = 0
while count < 3:
    print(f"Iterazione {count}")
    count += 1
else:
    print("While completato normalmente")

# ============================================
# 9. CICLI ANNIDATI (NESTED LOOPS)
# ============================================

print("\n=== CICLI ANNIDATI ===\n")

# Tabellina pitagorica (3x3)
print("Tabella di moltiplicazione:")
for i in range(1, 4):
    for j in range(1, 4):
        risultato = i * j
        print(f"{i}x{j}={risultato:2d}", end="  ")
    print()

print()

# Matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elementi della matrice:")
for riga in matrice:
    for elemento in riga:
        print(elemento, end=" ")
    print()

# ============================================
# 10. LIST COMPREHENSION
# ============================================

print("\n=== LIST COMPREHENSION ===\n")

# Creare una lista di quadrati
numeri = [1, 2, 3, 4, 5]
quadrati = [x**2 for x in numeri]
print(f"Numeri: {numeri}")
print(f"Quadrati: {quadrati}")

# Con condizione (filtrare numeri pari)
pari = [x for x in range(10) if x % 2 == 0]
print(f"Numeri pari: {pari}")

# Nested list comprehension
matrice_2d = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrice: {matrice_2d}")

# ============================================
# 11. ITERARE SU DIZIONARI
# ============================================

print("\n=== ITERARE SU DIZIONARI ===\n")

studente = {
    "nome": "Mario",
    "età": 22,
    "corso": "Informatica",
    "matricola": "12345"
}

# Iterare su chiavi
print("Chiavi:")
for chiave in studente:
    print(chiave, end=" ")
print("\n")

# Iterare su valori
print("Valori:")
for valore in studente.values():
    print(valore, end=" ")
print("\n")

# Iterare su chiavi e valori
print("Chiavi e valori:")
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")

# ============================================
# 12. ESERCIZI PRATICI
# ============================================

print("\n=== ESERCIZI PRATICI ===\n")

# Esercizio 1: Calcolare la somma di numeri
print("Esercizio 1: Somma numeri da 1 a 100")
somma = 0
for i in range(1, 101):
    somma += i
print(f"Somma: {somma}")

print()

# Esercizio 2: Fattoriale
print("Esercizio 2: Fattoriale di 5")
n = 5
fattoriale = 1
for i in range(1, n + 1):
    fattoriale *= i
print(f"{n}! = {fattoriale}")

print()

# Esercizio 3: Numeri di Fibonacci
print("Esercizio 3: Primi 10 numeri di Fibonacci")
n = 10
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(fib)

print()

# Esercizio 4: Filtrare e trasformare una lista
print("Esercizio 4: Raddoppiare i numeri pari")
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
risultato = []
for num in numeri:
    if num % 2 == 0:
        risultato.append(num * 2)
print(f"Originale: {numeri}")
print(f"Risultato: {risultato}")

print()

# Esercizio 5: Contare occorrenze
print("Esercizio 5: Contare lettere in una parola")
parola = "programmazione"
conteggio = {}
for lettera in parola:
    if lettera in conteggio:
        conteggio[lettera] += 1
    else:
        conteggio[lettera] = 1

for lettera, count in sorted(conteggio.items()):
    print(f"'{lettera}': {count}")
