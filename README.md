# Python Exam Preparation 🐍

Template per preparare l'esame di python / Template to prepare for Python exam

## 📚 Struttura del Repository

Questo repository contiene materiale didattico completo per la preparazione agli esami di Python, organizzato in:

### 📖 Documentazione (`doc/`)
- **`python_basics.md`**: Guida completa ai concetti fondamentali di Python con spiegazioni ed esempi

### 💻 Esempi Pratici (`examples/`)

1. **`01_variables.py`** - Variabili e Tipi di Dati
   - Tipi primitivi (int, float, str, bool)
   - Strutture dati (list, tuple, dict, set)
   - Operazioni e conversioni
   - Scope delle variabili

2. **`02_loops.py`** - Cicli
   - For loop e range
   - While loop
   - Enumerate e zip
   - Break, continue, else
   - List comprehension
   - Cicli annidati

3. **`03_lambda.py`** - Funzioni Lambda
   - Sintassi lambda
   - Map, filter, reduce
   - Sorted con lambda
   - Lambda con condizioni
   - Applicazioni pratiche

4. **`04_classes.py`** - Classi e OOP
   - Classi base e costruttori
   - Ereditarietà
   - Incapsulamento
   - Metodi speciali (magic methods)
   - Property e decoratori
   - Metodi statici e di classe

5. **`05_file_reading.py`** - Lettura e Scrittura File
   - Lettura file di testo
   - Scrittura e append
   - Modalità di apertura
   - Gestione errori
   - CSV e JSON
   - Context manager

6. **`06_pandas.py`** - Pandas per Analisi Dati
   - Creare DataFrame
   - Selezione e filtraggio
   - Ordinamento
   - Operazioni su colonne
   - GroupBy e aggregazioni
   - Valori mancanti
   - Merge e join
   - Lettura/scrittura CSV

## 🚀 Come Usare

### Setup Iniziale (Consigliato per Ubuntu)

Per configurare un ambiente virtuale Python e installare tutte le dipendenze:

```bash
# Eseguire lo script di setup (su Ubuntu)
./setup_venv.sh
```

Lo script:
- Verifica che Python 3 sia installato
- Crea un ambiente virtuale nella cartella `venv/`
- Installa automaticamente le dipendenze da `requirements.txt`
- Attiva l'ambiente virtuale

Dopo l'esecuzione, l'ambiente virtuale sarà attivo e potrai eseguire gli esempi.

**Per attivare manualmente l'ambiente virtuale in futuro:**
```bash
source venv/bin/activate
```

**Per disattivare l'ambiente virtuale:**
```bash
deactivate
```

### Setup Manuale

Se preferisci non usare lo script automatico:

```bash
# Creare ambiente virtuale
python3 -m venv venv

# Attivare ambiente virtuale
source venv/bin/activate

# Installare dipendenze
pip install -r requirements.txt
```

### Eseguire gli Esempi

Ogni file di esempio può essere eseguito direttamente:

```bash
# Esempio: eseguire il file sulle variabili
python examples/01_variables.py

# Esempio: eseguire il file sui cicli
python examples/02_loops.py

# Esempio: eseguire il file su pandas
python examples/06_pandas.py
```

### Studiare la Documentazione

Leggi la documentazione completa per avere una visione d'insieme:

```bash
# Aprire la documentazione
cat doc/python_basics.md
```

O visualizzarla su GitHub navigando nella cartella `doc/`.

## 📋 Prerequisiti

- Python 3.x installato
- `python3-venv` per creare ambienti virtuali (Ubuntu: `sudo apt install python3-venv`)
- Per gli esempi Pandas (installate automaticamente con `setup_venv.sh`):
  ```bash
  pip install -r requirements.txt
  ```

## 💡 Suggerimenti per lo Studio

1. **Inizia dalla documentazione**: Leggi `doc/python_basics.md` per avere una panoramica completa
2. **Esegui gli esempi**: Prova ogni file nella cartella `examples/` e osserva l'output
3. **Modifica il codice**: Sperimenta modificando gli esempi per consolidare la comprensione
4. **Fai esercizi**: Ogni file contiene esercizi pratici alla fine
5. **Pratica regolarmente**: La programmazione si impara praticando!

## 📚 Argomenti Coperti

- ✅ Variabili e tipi di dati
- ✅ Cicli (for, while, comprehension)
- ✅ Funzioni lambda e programmazione funzionale
- ✅ Classi e programmazione orientata agli oggetti
- ✅ Lettura e scrittura file
- ✅ Pandas per analisi dati

## 🤝 Contribuire

Sentiti libero di contribuire migliorando gli esempi o aggiungendo nuovi argomenti!

## 📄 Licenza

Materiale didattico open source per la preparazione agli esami di Python.

---

**Buono studio! 📚✨**
