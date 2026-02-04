"""
Esempi di Lettura e Scrittura File in Python
"""

import os

# ============================================
# 1. LETTURA FILE DI TESTO
# ============================================

print("=== LETTURA FILE DI TESTO ===\n")

# Creare un file di esempio
with open('/tmp/esempio.txt', 'w') as f:
    f.write("Questa è la prima riga\n")
    f.write("Questa è la seconda riga\n")
    f.write("Questa è la terza riga\n")

# Metodo 1: Leggere tutto il contenuto
print("Metodo 1: read()")
with open('/tmp/esempio.txt', 'r') as f:
    contenuto = f.read()
    print(contenuto)

# Metodo 2: Leggere tutte le righe in una lista
print("Metodo 2: readlines()")
with open('/tmp/esempio.txt', 'r') as f:
    righe = f.readlines()
    print(righe)

# Metodo 3: Iterare riga per riga
print("Metodo 3: iterazione")
with open('/tmp/esempio.txt', 'r') as f:
    for numero_riga, riga in enumerate(f, 1):
        print(f"Riga {numero_riga}: {riga.strip()}")

# Metodo 4: readline() - legge una riga alla volta
print("\nMetodo 4: readline()")
with open('/tmp/esempio.txt', 'r') as f:
    prima_riga = f.readline()
    seconda_riga = f.readline()
    print(f"Prima: {prima_riga.strip()}")
    print(f"Seconda: {seconda_riga.strip()}")

# ============================================
# 2. SCRITTURA FILE DI TESTO
# ============================================

print("\n=== SCRITTURA FILE DI TESTO ===\n")

# Modalità 'w' - sovrascrive il file
with open('/tmp/output.txt', 'w') as f:
    f.write("Prima riga\n")
    f.write("Seconda riga\n")
print("File scritto con modalità 'w'")

# Modalità 'a' - append, aggiunge in fondo
with open('/tmp/output.txt', 'a') as f:
    f.write("Terza riga (append)\n")
    f.write("Quarta riga (append)\n")
print("Righe aggiunte con modalità 'a'")

# Verificare il contenuto
with open('/tmp/output.txt', 'r') as f:
    print(f.read())

# Scrivere liste di stringhe
righe = ["Riga 1\n", "Riga 2\n", "Riga 3\n"]
with open('/tmp/lista.txt', 'w') as f:
    f.writelines(righe)
print("Liste scritte con writelines()")

# ============================================
# 3. MODALITÀ DI APERTURA FILE
# ============================================

print("=== MODALITÀ DI APERTURA ===\n")

modalità = {
    "'r'": "Lettura (default) - errore se file non esiste",
    "'w'": "Scrittura - crea o sovrascrive",
    "'a'": "Append - crea o aggiunge alla fine",
    "'x'": "Creazione esclusiva - errore se esiste",
    "'r+'": "Lettura e scrittura",
    "'w+'": "Scrittura e lettura - sovrascrive",
    "'a+'": "Append e lettura",
    "'rb'": "Lettura binaria",
    "'wb'": "Scrittura binaria"
}

for modo, descrizione in modalità.items():
    print(f"{modo:6}: {descrizione}")

# ============================================
# 4. GESTIONE ERRORI CON FILE
# ============================================

print("\n=== GESTIONE ERRORI ===\n")

# Try-except per file non esistente
try:
    with open('/tmp/non_esiste.txt', 'r') as f:
        contenuto = f.read()
except FileNotFoundError:
    print("Errore: File non trovato!")

# Try-except per permessi
try:
    with open('/tmp/test_permessi.txt', 'w') as f:
        f.write("test")
    os.chmod('/tmp/test_permessi.txt', 0o000)
    with open('/tmp/test_permessi.txt', 'r') as f:
        contenuto = f.read()
except PermissionError:
    print("Errore: Permessi insufficienti!")
finally:
    # Ripristina permessi per cleanup
    if os.path.exists('/tmp/test_permessi.txt'):
        os.chmod('/tmp/test_permessi.txt', 0o644)

# ============================================
# 5. LAVORARE CON PERCORSI
# ============================================

print("\n=== LAVORARE CON PERCORSI ===\n")

# Ottenere informazioni su file
file_path = '/tmp/esempio.txt'
if os.path.exists(file_path):
    print(f"File esiste: {file_path}")
    print(f"Dimensione: {os.path.getsize(file_path)} bytes")
    print(f"È un file? {os.path.isfile(file_path)}")
    print(f"È una directory? {os.path.isdir(file_path)}")

# Path operations
percorso = "/home/user/documenti/file.txt"
print(f"\nPercorso completo: {percorso}")
print(f"Directory: {os.path.dirname(percorso)}")
print(f"Nome file: {os.path.basename(percorso)}")
print(f"Nome senza estensione: {os.path.splitext(percorso)[0]}")
print(f"Estensione: {os.path.splitext(percorso)[1]}")

# ============================================
# 6. LETTURA FILE CSV MANUALE
# ============================================

print("\n=== LETTURA FILE CSV ===\n")

# Creare un file CSV di esempio
csv_content = """nome,età,città
Mario,25,Roma
Luigi,30,Milano
Anna,28,Napoli
Carlo,22,Torino"""

with open('/tmp/studenti.csv', 'w') as f:
    f.write(csv_content)

# Leggere CSV manualmente
print("Metodo manuale:")
with open('/tmp/studenti.csv', 'r') as f:
    # Leggere header
    header = f.readline().strip().split(',')
    print(f"Colonne: {header}\n")
    
    # Leggere dati
    for riga in f:
        dati = riga.strip().split(',')
        print(f"Nome: {dati[0]}, Età: {dati[1]}, Città: {dati[2]}")

# Usare il modulo csv
print("\nUsando il modulo csv:")
import csv

with open('/tmp/studenti.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(f"{row['nome']} ha {row['età']} anni e vive a {row['città']}")

# Scrivere CSV
print("\nScrivere CSV:")
studenti = [
    {'nome': 'Paolo', 'età': 24, 'città': 'Bologna'},
    {'nome': 'Sara', 'età': 26, 'città': 'Firenze'}
]

with open('/tmp/nuovi_studenti.csv', 'w', newline='') as f:
    fieldnames = ['nome', 'età', 'città']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(studenti)

print("CSV scritto con successo")

# ============================================
# 7. FILE JSON
# ============================================

print("\n=== FILE JSON ===\n")

import json

# Creare dati
dati = {
    'studente': 'Mario Rossi',
    'matricola': '12345',
    'esami': [
        {'corso': 'Matematica', 'voto': 28},
        {'corso': 'Fisica', 'voto': 30},
        {'corso': 'Informatica', 'voto': 27}
    ]
}

# Scrivere JSON
with open('/tmp/studente.json', 'w') as f:
    json.dump(dati, f, indent=4)
print("JSON scritto")

# Leggere JSON
with open('/tmp/studente.json', 'r') as f:
    dati_letti = json.load(f)

print(f"\nStudente: {dati_letti['studente']}")
print("Esami:")
for esame in dati_letti['esami']:
    print(f"  {esame['corso']}: {esame['voto']}")

# ============================================
# 8. CONTEXT MANAGER E WITH
# ============================================

print("\n=== CONTEXT MANAGER ===\n")

# Senza context manager (sconsigliato)
print("Senza with (sconsigliato):")
f = open('/tmp/test.txt', 'w')
try:
    f.write("Test\n")
finally:
    f.close()
print("File chiuso manualmente")

# Con context manager (raccomandato)
print("\nCon with (raccomandato):")
with open('/tmp/test.txt', 'w') as f:
    f.write("Test con context manager\n")
print("File chiuso automaticamente")

# Context manager multipli
print("\nContext manager multipli:")
with open('/tmp/input.txt', 'w') as f_in, \
     open('/tmp/output_copy.txt', 'w') as f_out:
    f_in.write("Dati di input\n")
    f_out.write("Dati di output\n")

# ============================================
# 9. FILE BINARI
# ============================================

print("\n=== FILE BINARI ===\n")

# Scrivere dati binari
dati_binari = bytes([65, 66, 67, 68, 69])  # ASCII per ABCDE
with open('/tmp/binario.bin', 'wb') as f:
    f.write(dati_binari)
print("File binario scritto")

# Leggere dati binari
with open('/tmp/binario.bin', 'rb') as f:
    contenuto = f.read()
    print(f"Contenuto binario: {contenuto}")
    print(f"Come testo: {contenuto.decode('ascii')}")

# ============================================
# 10. ESERCIZI PRATICI
# ============================================

print("\n=== ESERCIZI PRATICI ===\n")

# Esercizio 1: Contare parole in un file
print("Esercizio 1: Contare parole")
testo = """Python è un linguaggio di programmazione.
Python è facile da imparare.
Python è potente e versatile."""

with open('/tmp/testo.txt', 'w') as f:
    f.write(testo)

with open('/tmp/testo.txt', 'r') as f:
    contenuto = f.read()
    parole = contenuto.split()
    print(f"Numero di parole: {len(parole)}")
    print(f"Numero di righe: {contenuto.count(chr(10)) + 1}")

print()

# Esercizio 2: Filtrare righe
print("Esercizio 2: Filtrare righe che contengono 'Python'")
with open('/tmp/testo.txt', 'r') as f_in, \
     open('/tmp/filtrato.txt', 'w') as f_out:
    for riga in f_in:
        if 'Python' in riga:
            f_out.write(riga)

with open('/tmp/filtrato.txt', 'r') as f:
    print(f.read())

# Esercizio 3: Invertire l'ordine delle righe
print("Esercizio 3: Invertire righe")
with open('/tmp/esempio.txt', 'r') as f:
    righe = f.readlines()

righe_invertite = righe[::-1]

with open('/tmp/invertito.txt', 'w') as f:
    f.writelines(righe_invertite)

with open('/tmp/invertito.txt', 'r') as f:
    print(f.read())

# Esercizio 4: Analizzare log
print("Esercizio 4: Analizzare file log")
log_content = """2024-01-15 10:23:45 INFO Application started
2024-01-15 10:24:12 WARNING Low memory
2024-01-15 10:25:33 ERROR Connection failed
2024-01-15 10:26:01 INFO User logged in
2024-01-15 10:27:15 ERROR Database error"""

with open('/tmp/app.log', 'w') as f:
    f.write(log_content)

# Conta errori
conteggio = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
with open('/tmp/app.log', 'r') as f:
    for riga in f:
        for livello in conteggio:
            if livello in riga:
                conteggio[livello] += 1

print("Statistiche log:")
for livello, count in conteggio.items():
    print(f"  {livello}: {count}")

# Esercizio 5: Unire file
print("\nEsercizio 5: Unire più file")
file1_content = "Contenuto del primo file\n"
file2_content = "Contenuto del secondo file\n"
file3_content = "Contenuto del terzo file\n"

with open('/tmp/file1.txt', 'w') as f:
    f.write(file1_content)
with open('/tmp/file2.txt', 'w') as f:
    f.write(file2_content)
with open('/tmp/file3.txt', 'w') as f:
    f.write(file3_content)

# Unire i file
with open('/tmp/unito.txt', 'w') as f_out:
    for i in range(1, 4):
        with open(f'/tmp/file{i}.txt', 'r') as f_in:
            f_out.write(f_in.read())

with open('/tmp/unito.txt', 'r') as f:
    print(f.read())

print("\n=== Fine esempi file ===")
