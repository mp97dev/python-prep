"""
Esempi di Pandas per Analisi Dati
"""

import pandas as pd
import numpy as np

# ============================================
# 1. CREARE DATAFRAME
# ============================================

print("=== CREARE DATAFRAME ===\n")

# Da dizionario
dati = {
    'nome': ['Mario', 'Luigi', 'Anna', 'Carlo', 'Sara'],
    'età': [25, 30, 28, 22, 26],
    'città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna'],
    'voto': [28, 30, 27, 29, 26]
}

df = pd.DataFrame(dati)
print("DataFrame da dizionario:")
print(df)
print()

# Da lista di liste
dati_lista = [
    ['Mario', 25, 'Roma', 28],
    ['Luigi', 30, 'Milano', 30],
    ['Anna', 28, 'Napoli', 27]
]
df_lista = pd.DataFrame(dati_lista, columns=['nome', 'età', 'città', 'voto'])
print("DataFrame da lista:")
print(df_lista)
print()

# ============================================
# 2. INFORMAZIONI BASE
# ============================================

print("=== INFORMAZIONI BASE ===\n")

# Prime righe
print("Prime 3 righe (head):")
print(df.head(3))
print()

# Ultime righe
print("Ultime 2 righe (tail):")
print(df.tail(2))
print()

# Forma del DataFrame
print(f"Forma (righe, colonne): {df.shape}")
print()

# Info sul DataFrame
print("Info:")
df.info()
print()

# Statistiche descrittive
print("Statistiche descrittive:")
print(df.describe())
print()

# Colonne
print(f"Colonne: {df.columns.tolist()}")
print()

# Tipi di dati
print("Tipi di dati:")
print(df.dtypes)
print()

# ============================================
# 3. SELEZIONE DATI
# ============================================

print("=== SELEZIONE DATI ===\n")

# Selezionare una colonna
print("Colonna 'nome':")
print(df['nome'])
print()

# Selezionare più colonne
print("Colonne 'nome' e 'età':")
print(df[['nome', 'età']])
print()

# Selezionare righe per indice (iloc)
print("Prima riga:")
print(df.iloc[0])
print()

print("Prime due righe:")
print(df.iloc[0:2])
print()

# Selezionare per label (loc)
print("Righe 1-2, colonne 'nome' e 'voto':")
print(df.loc[1:2, ['nome', 'voto']])
print()

# ============================================
# 4. FILTRAGGIO
# ============================================

print("=== FILTRAGGIO ===\n")

# Filtro semplice
print("Studenti con età > 26:")
print(df[df['età'] > 26])
print()

# Filtro multiplo (AND)
print("Studenti con età > 25 e voto >= 28:")
print(df[(df['età'] > 25) & (df['voto'] >= 28)])
print()

# Filtro multiplo (OR)
print("Studenti con età < 25 o voto = 30:")
print(df[(df['età'] < 25) | (df['voto'] == 30)])
print()

# Filtro con isin
print("Studenti di Roma o Milano:")
print(df[df['città'].isin(['Roma', 'Milano'])])
print()

# ============================================
# 5. ORDINAMENTO
# ============================================

print("=== ORDINAMENTO ===\n")

# Ordinare per una colonna
print("Ordinati per età:")
print(df.sort_values('età'))
print()

# Ordinare decrescente
print("Ordinati per voto (decrescente):")
print(df.sort_values('voto', ascending=False))
print()

# Ordinare per più colonne
df_copia = df.copy()
df_copia.loc[len(df_copia)] = ['Paolo', 28, 'Roma', 27]
print("Ordinati per città e poi per età:")
print(df_copia.sort_values(['città', 'età']))
print()

# ============================================
# 6. OPERAZIONI SU COLONNE
# ============================================

print("=== OPERAZIONI SU COLONNE ===\n")

# Aggiungere nuova colonna
df['anno_nascita'] = 2024 - df['età']
print("Con anno di nascita:")
print(df)
print()

# Operazioni matematiche
df['voto_normalizzato'] = df['voto'] / 30
print("Con voto normalizzato:")
print(df[['nome', 'voto', 'voto_normalizzato']])
print()

# Apply - applicare funzione
df['nome_maiuscolo'] = df['nome'].apply(lambda x: x.upper())
print("Con nome maiuscolo:")
print(df[['nome', 'nome_maiuscolo']])
print()

# ============================================
# 7. AGGREGAZIONE E GROUPBY
# ============================================

print("=== AGGREGAZIONE ===\n")

# Creare dataset più grande
dati_esami = {
    'studente': ['Mario', 'Mario', 'Luigi', 'Luigi', 'Anna', 'Anna'],
    'corso': ['Matematica', 'Fisica', 'Matematica', 'Fisica', 'Matematica', 'Fisica'],
    'voto': [28, 30, 27, 29, 30, 28]
}
df_esami = pd.DataFrame(dati_esami)

print("Dataset esami:")
print(df_esami)
print()

# GroupBy e aggregazione
print("Media voti per studente:")
print(df_esami.groupby('studente')['voto'].mean())
print()

print("Statistiche per corso:")
print(df_esami.groupby('corso')['voto'].describe())
print()

# Aggregazioni multiple
print("Aggregazioni multiple per studente:")
print(df_esami.groupby('studente')['voto'].agg(['mean', 'min', 'max', 'count']))
print()

# ============================================
# 8. VALORI MANCANTI
# ============================================

print("=== VALORI MANCANTI ===\n")

# Creare DataFrame con NaN
dati_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df_nan = pd.DataFrame(dati_nan)

print("DataFrame con NaN:")
print(df_nan)
print()

# Controllare NaN
print("Ci sono NaN?")
print(df_nan.isnull())
print()

print("Conteggio NaN per colonna:")
print(df_nan.isnull().sum())
print()

# Rimuovere righe con NaN
print("Rimuovere righe con NaN:")
print(df_nan.dropna())
print()

# Riempire NaN
print("Riempire NaN con 0:")
print(df_nan.fillna(0))
print()

print("Riempire NaN con media:")
print(df_nan.fillna(df_nan.mean()))
print()

# ============================================
# 9. UNIRE DATAFRAME
# ============================================

print("=== UNIRE DATAFRAME ===\n")

# Concatenazione
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print()

print("Concatenazione verticale:")
print(pd.concat([df1, df2], ignore_index=True))
print()

# Merge (join)
studenti = pd.DataFrame({
    'id': [1, 2, 3],
    'nome': ['Mario', 'Luigi', 'Anna']
})

voti = pd.DataFrame({
    'id': [1, 2, 3],
    'voto': [28, 30, 27]
})

print("Studenti:")
print(studenti)
print("\nVoti:")
print(voti)
print()

print("Merge su 'id':")
risultato = pd.merge(studenti, voti, on='id')
print(risultato)
print()

# ============================================
# 10. LETTURA/SCRITTURA CSV
# ============================================

print("=== LETTURA/SCRITTURA CSV ===\n")

# Scrivere CSV
df.to_csv('/tmp/studenti.csv', index=False)
print("CSV scritto in /tmp/studenti.csv")

# Leggere CSV
df_letto = pd.read_csv('/tmp/studenti.csv')
print("\nCSV letto:")
print(df_letto.head())
print()

# ============================================
# 11. PIVOT TABLE
# ============================================

print("=== PIVOT TABLE ===\n")

# Dati per pivot
dati_vendite = {
    'data': ['2024-01', '2024-01', '2024-02', '2024-02', '2024-01', '2024-02'],
    'prodotto': ['A', 'B', 'A', 'B', 'A', 'B'],
    'vendite': [100, 150, 120, 180, 110, 160]
}
df_vendite = pd.DataFrame(dati_vendite)

print("Dati vendite:")
print(df_vendite)
print()

# Creare pivot table
pivot = df_vendite.pivot_table(
    values='vendite',
    index='data',
    columns='prodotto',
    aggfunc='sum'
)
print("Pivot table:")
print(pivot)
print()

# ============================================
# 12. ESERCIZI PRATICI
# ============================================

print("=== ESERCIZI PRATICI ===\n")

# Esercizio 1: Analisi voti
print("Esercizio 1: Analisi voti studenti")
dati = {
    'nome': ['Mario', 'Luigi', 'Anna', 'Carlo', 'Sara', 'Paolo'],
    'voto_matematica': [28, 30, 27, 29, 26, 30],
    'voto_fisica': [30, 28, 29, 27, 28, 29],
    'voto_informatica': [27, 29, 30, 28, 27, 30]
}
df_studenti = pd.DataFrame(dati)

# Media voti per studente
df_studenti['media'] = df_studenti[['voto_matematica', 'voto_fisica', 'voto_informatica']].mean(axis=1)
print(df_studenti)
print()

print(f"Media più alta: {df_studenti['media'].max():.2f}")
print(f"Studente migliore: {df_studenti.loc[df_studenti['media'].idxmax(), 'nome']}")
print()

# Esercizio 2: Filtrare e ordinare
print("Esercizio 2: Studenti con media >= 28")
studenti_top = df_studenti[df_studenti['media'] >= 28].sort_values('media', ascending=False)
print(studenti_top[['nome', 'media']])
print()

# Esercizio 3: Conteggi e percentuali
print("Esercizio 3: Distribuzione per città")
dati_città = {
    'nome': ['Mario', 'Luigi', 'Anna', 'Carlo', 'Sara', 'Paolo', 'Laura', 'Marco'],
    'città': ['Roma', 'Milano', 'Roma', 'Milano', 'Roma', 'Napoli', 'Milano', 'Roma']
}
df_città = pd.DataFrame(dati_città)

conteggio = df_città['città'].value_counts()
percentuale = df_città['città'].value_counts(normalize=True) * 100

print("Conteggio per città:")
print(conteggio)
print("\nPercentuale:")
print(percentuale.round(2))
print()

# Esercizio 4: Time series
print("Esercizio 4: Analisi temporale")
dati_temp = {
    'data': pd.date_range('2024-01-01', periods=7),
    'temperatura': [15, 16, 14, 18, 17, 19, 20]
}
df_temp = pd.DataFrame(dati_temp)
df_temp['giorno_settimana'] = df_temp['data'].dt.day_name()

print(df_temp)
print(f"\nTemperatura media: {df_temp['temperatura'].mean():.1f}°C")
print(f"Temperatura massima: {df_temp['temperatura'].max()}°C")
print(f"Temperatura minima: {df_temp['temperatura'].min()}°C")

print("\n=== Fine esempi Pandas ===")
