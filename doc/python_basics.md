# Python Basics - Documentazione

## Indice
1. [Variabili e Tipi di Dati](#variabili-e-tipi-di-dati)
2. [Cicli (Loops)](#cicli-loops)
3. [Funzioni Lambda](#funzioni-lambda)
4. [Classi e OOP](#classi-e-oop)
5. [Lettura File](#lettura-file)
6. [Pandas](#pandas)

---

## Variabili e Tipi di Dati

### Tipi di Dati Base
- **int**: numeri interi (es: 42, -10)
- **float**: numeri decimali (es: 3.14, -0.5)
- **str**: stringhe di testo (es: "Hello", 'World')
- **bool**: valori booleani (True, False)
- **list**: liste mutabili (es: [1, 2, 3])
- **tuple**: tuple immutabili (es: (1, 2, 3))
- **dict**: dizionari chiave-valore (es: {"nome": "Mario", "età": 25})
- **set**: insiemi non ordinati (es: {1, 2, 3})

### Dichiarazione Variabili
```python
# Assegnazione semplice
x = 10
nome = "Mario"
is_active = True

# Assegnazione multipla
a, b, c = 1, 2, 3

# Type casting
numero_str = "42"
numero_int = int(numero_str)
```

---

## Cicli (Loops)

### For Loop
```python
# Iterare su una lista
for i in [1, 2, 3, 4, 5]:
    print(i)

# Range
for i in range(10):  # da 0 a 9
    print(i)

# Enumerate
for index, valore in enumerate(['a', 'b', 'c']):
    print(f"Indice {index}: {valore}")
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Controllo del Flusso
- **break**: esce dal ciclo
- **continue**: salta all'iterazione successiva
- **else**: eseguito se il ciclo termina normalmente

---

## Funzioni Lambda

### Sintassi
```python
# Funzione lambda base
lambda argomenti: espressione

# Esempio
somma = lambda x, y: x + y
risultato = somma(5, 3)  # 8
```

### Utilizzo con Funzioni Built-in
```python
# map()
numeri = [1, 2, 3, 4]
quadrati = list(map(lambda x: x**2, numeri))

# filter()
pari = list(filter(lambda x: x % 2 == 0, numeri))

# sorted()
studenti = [("Mario", 25), ("Luigi", 22), ("Anna", 28)]
ordinati = sorted(studenti, key=lambda x: x[1])
```

---

## Classi e OOP

### Definizione Classe Base
```python
class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def saluta(self):
        return f"Ciao, sono {self.nome}"
```

### Ereditarietà
```python
class Studente(Persona):
    def __init__(self, nome, età, matricola):
        super().__init__(nome, età)
        self.matricola = matricola
```

### Concetti Chiave
- **__init__**: costruttore
- **self**: riferimento all'istanza corrente
- **Ereditarietà**: riuso del codice
- **Metodi**: funzioni all'interno della classe
- **Attributi**: variabili della classe

---

## Lettura File

### Lettura File di Testo
```python
# Metodo con context manager (raccomandato)
with open('file.txt', 'r') as f:
    contenuto = f.read()

# Lettura riga per riga
with open('file.txt', 'r') as f:
    for riga in f:
        print(riga.strip())
```

### Scrittura File
```python
with open('file.txt', 'w') as f:
    f.write("Testo da scrivere\n")
```

### Modalità di Apertura
- **'r'**: lettura (default)
- **'w'**: scrittura (sovrascrive)
- **'a'**: append (aggiunge in fondo)
- **'r+'**: lettura e scrittura

---

## Pandas

### Importazione
```python
import pandas as pd
```

### DataFrame
```python
# Creare un DataFrame
df = pd.DataFrame({
    'nome': ['Mario', 'Luigi', 'Anna'],
    'età': [25, 22, 28],
    'città': ['Roma', 'Milano', 'Napoli']
})

# Leggere da CSV
df = pd.read_csv('dati.csv')

# Scrivere su CSV
df.to_csv('output.csv', index=False)
```

### Operazioni Comuni
```python
# Visualizzare prime righe
df.head()

# Informazioni sul DataFrame
df.info()

# Statistiche descrittive
df.describe()

# Selezione colonne
df['nome']
df[['nome', 'età']]

# Filtraggio
df[df['età'] > 25]

# Ordinamento
df.sort_values('età')

# Groupby
df.groupby('città')['età'].mean()
```

---

## Risorse Aggiuntive

- [Python Official Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
