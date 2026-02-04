"""
Esempi di Classi e Programmazione Orientata agli Oggetti in Python
"""

# ============================================
# 1. CLASSE BASE
# ============================================

print("=== CLASSE BASE ===\n")

class Persona:
    """Classe che rappresenta una persona"""
    
    def __init__(self, nome, età):
        """Costruttore della classe"""
        self.nome = nome
        self.età = età
    
    def saluta(self):
        """Metodo per salutare"""
        return f"Ciao, sono {self.nome} e ho {self.età} anni"
    
    def compleanno(self):
        """Incrementa l'età di 1"""
        self.età += 1
        return f"{self.nome} ora ha {self.età} anni!"

# Creare istanze (oggetti)
persona1 = Persona("Mario", 25)
persona2 = Persona("Anna", 22)

print(persona1.saluta())
print(persona2.saluta())
print(persona1.compleanno())

# ============================================
# 2. ATTRIBUTI DI CLASSE VS ISTANZA
# ============================================

print("\n=== ATTRIBUTI DI CLASSE VS ISTANZA ===\n")

class Studente:
    # Attributo di classe (condiviso da tutte le istanze)
    università = "Università di Roma"
    numero_studenti = 0
    
    def __init__(self, nome, matricola):
        # Attributi di istanza (specifici per ogni oggetto)
        self.nome = nome
        self.matricola = matricola
        Studente.numero_studenti += 1
    
    def info(self):
        return f"{self.nome} ({self.matricola}) - {Studente.università}"

studente1 = Studente("Mario", "12345")
studente2 = Studente("Luigi", "12346")

print(studente1.info())
print(studente2.info())
print(f"Numero totale studenti: {Studente.numero_studenti}")

# ============================================
# 3. METODI SPECIALI (MAGIC METHODS)
# ============================================

print("\n=== METODI SPECIALI ===\n")

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def __str__(self):
        """Rappresentazione stringa leggibile"""
        return f"'{self.titolo}' di {self.autore}"
    
    def __repr__(self):
        """Rappresentazione stringa per debug"""
        return f"Libro('{self.titolo}', '{self.autore}', {self.pagine})"
    
    def __len__(self):
        """Lunghezza = numero di pagine"""
        return self.pagine
    
    def __eq__(self, other):
        """Uguaglianza basata su titolo e autore"""
        if isinstance(other, Libro):
            return self.titolo == other.titolo and self.autore == other.autore
        return False

libro1 = Libro("1984", "George Orwell", 328)
libro2 = Libro("1984", "George Orwell", 328)

print(f"str: {libro1}")
print(f"repr: {repr(libro1)}")
print(f"len: {len(libro1)} pagine")
print(f"libro1 == libro2: {libro1 == libro2}")

# ============================================
# 4. EREDITARIETÀ
# ============================================

print("\n=== EREDITARIETÀ ===\n")

class Animale:
    """Classe base"""
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def descrizione(self):
        return f"{self.nome} ha {self.età} anni"
    
    def suono(self):
        return "L'animale fa un suono"

class Cane(Animale):
    """Classe derivata da Animale"""
    def __init__(self, nome, età, razza):
        super().__init__(nome, età)  # Chiama il costruttore della classe base
        self.razza = razza
    
    def suono(self):
        """Override del metodo della classe base"""
        return "Bau bau!"
    
    def descrizione(self):
        """Estende il metodo della classe base"""
        base_desc = super().descrizione()
        return f"{base_desc}, è un {self.razza}"

class Gatto(Animale):
    def suono(self):
        return "Miao!"

# Utilizzare le classi
cane = Cane("Fido", 3, "Labrador")
gatto = Gatto("Felix", 2)

print(cane.descrizione())
print(f"{cane.nome} dice: {cane.suono()}")
print()
print(gatto.descrizione())
print(f"{gatto.nome} dice: {gatto.suono()}")

# ============================================
# 5. INCAPSULAMENTO (PRIVATE/PROTECTED)
# ============================================

print("\n=== INCAPSULAMENTO ===\n")

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        self._saldo = saldo_iniziale  # Protected (convenzione)
        self.__pin = "1234"  # Private (name mangling)
    
    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            return f"Depositati €{importo}. Saldo: €{self._saldo}"
        return "Importo non valido"
    
    def preleva(self, importo, pin):
        if pin != self.__pin:
            return "PIN errato"
        if importo > self._saldo:
            return "Saldo insufficiente"
        self._saldo -= importo
        return f"Prelevati €{importo}. Saldo: €{self._saldo}"
    
    def get_saldo(self):
        """Getter per il saldo"""
        return self._saldo
    
    def cambia_pin(self, vecchio_pin, nuovo_pin):
        if vecchio_pin == self.__pin:
            self.__pin = nuovo_pin
            return "PIN cambiato con successo"
        return "PIN vecchio errato"

conto = ContoBancario("Mario Rossi", 1000)
print(f"Saldo iniziale: €{conto.get_saldo()}")
print(conto.deposita(500))
print(conto.preleva(200, "1234"))
print(conto.preleva(200, "0000"))  # PIN errato

# ============================================
# 6. PROPERTY E DECORATORI
# ============================================

print("\n=== PROPERTY ===\n")

class Rettangolo:
    def __init__(self, base, altezza):
        self._base = base
        self._altezza = altezza
    
    @property
    def base(self):
        """Getter per base"""
        return self._base
    
    @base.setter
    def base(self, valore):
        """Setter per base con validazione"""
        if valore > 0:
            self._base = valore
        else:
            raise ValueError("La base deve essere positiva")
    
    @property
    def altezza(self):
        return self._altezza
    
    @altezza.setter
    def altezza(self, valore):
        if valore > 0:
            self._altezza = valore
        else:
            raise ValueError("L'altezza deve essere positiva")
    
    @property
    def area(self):
        """Property calcolata"""
        return self._base * self._altezza
    
    @property
    def perimetro(self):
        """Property calcolata"""
        return 2 * (self._base + self._altezza)

rett = Rettangolo(5, 3)
print(f"Base: {rett.base}, Altezza: {rett.altezza}")
print(f"Area: {rett.area}")
print(f"Perimetro: {rett.perimetro}")

# Modificare con setter
rett.base = 10
print(f"\nNuova base: {rett.base}")
print(f"Nuova area: {rett.area}")

# ============================================
# 7. METODI STATICI E DI CLASSE
# ============================================

print("\n=== METODI STATICI E DI CLASSE ===\n")

class Matematica:
    pi = 3.14159
    
    @staticmethod
    def somma(a, b):
        """Metodo statico - non accede a self o cls"""
        return a + b
    
    @staticmethod
    def è_pari(numero):
        return numero % 2 == 0
    
    @classmethod
    def area_cerchio(cls, raggio):
        """Metodo di classe - accede agli attributi di classe"""
        return cls.pi * raggio ** 2

# Chiamare metodi senza istanziare
print(f"5 + 3 = {Matematica.somma(5, 3)}")
print(f"4 è pari? {Matematica.è_pari(4)}")
print(f"Area cerchio (r=5): {Matematica.area_cerchio(5):.2f}")

# ============================================
# 8. EREDITARIETÀ MULTIPLA
# ============================================

print("\n=== EREDITARIETÀ MULTIPLA ===\n")

class Veicolo:
    def __init__(self, marca):
        self.marca = marca
    
    def info_veicolo(self):
        return f"Veicolo marca {self.marca}"

class Elettrico:
    def __init__(self, capacità_batteria):
        self.capacità_batteria = capacità_batteria
    
    def info_elettrico(self):
        return f"Batteria: {self.capacità_batteria} kWh"

class AutoElettrica(Veicolo, Elettrico):
    def __init__(self, marca, capacità_batteria, modello):
        Veicolo.__init__(self, marca)
        Elettrico.__init__(self, capacità_batteria)
        self.modello = modello
    
    def info_completa(self):
        return f"{self.marca} {self.modello} - {self.info_elettrico()}"

tesla = AutoElettrica("Tesla", 75, "Model 3")
print(tesla.info_completa())

# ============================================
# 9. COMPOSIZIONE
# ============================================

print("\n=== COMPOSIZIONE ===\n")

class Motore:
    def __init__(self, cilindrata, cavalli):
        self.cilindrata = cilindrata
        self.cavalli = cavalli
    
    def info(self):
        return f"{self.cilindrata}cc, {self.cavalli}CV"

class Automobile:
    def __init__(self, marca, modello, motore):
        self.marca = marca
        self.modello = modello
        self.motore = motore  # Composizione
    
    def descrizione(self):
        return f"{self.marca} {self.modello} con motore {self.motore.info()}"

motore_auto = Motore(2000, 150)
auto = Automobile("Fiat", "Tipo", motore_auto)
print(auto.descrizione())

# ============================================
# 10. ESERCIZIO PRATICO COMPLETO
# ============================================

print("\n=== ESERCIZIO PRATICO: GESTIONE BIBLIOTECA ===\n")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        return f"Libro '{libro.titolo}' aggiunto"
    
    def cerca_per_autore(self, autore):
        return [libro for libro in self.libri if libro.autore == autore]
    
    def lista_libri(self):
        if not self.libri:
            return "Nessun libro nella biblioteca"
        return "\n".join([f"- {libro}" for libro in self.libri])

class LibroEsteso:
    def __init__(self, titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere
        self.disponibile = True
    
    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Prestato"
        return f"{self.titolo} di {self.autore} ({self.anno}) - {stato}"
    
    def presta(self):
        if self.disponibile:
            self.disponibile = False
            return f"'{self.titolo}' prestato"
        return f"'{self.titolo}' non disponibile"
    
    def restituisci(self):
        self.disponibile = True
        return f"'{self.titolo}' restituito"

# Utilizzo
biblioteca = Biblioteca("Biblioteca Comunale")

libro1 = LibroEsteso("1984", "George Orwell", 1949, "Distopia")
libro2 = LibroEsteso("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, "Fantasy")
libro3 = LibroEsteso("La Fattoria degli Animali", "George Orwell", 1945, "Satira")

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

print(f"Biblioteca: {biblioteca.nome}\n")
print("Catalogo:")
print(biblioteca.lista_libri())

print(f"\n{libro1.presta()}")
print(f"\nLibri di George Orwell:")
for libro in biblioteca.cerca_per_autore("George Orwell"):
    print(f"  - {libro}")
