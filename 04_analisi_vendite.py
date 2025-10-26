"""
================================================================================
COMPITO DI REALTÀ: Sistema di Analisi Vendite con NumPy
VERSIONE CON COMMENTI DIDATTICI DETTAGLIATI
================================================================================

Questo file contiene il codice completo con spiegazioni dettagliate di ogni
istruzione. È pensato per studenti che stanno imparando Python e NumPy.

ARGOMENTI TRATTATI:
- Array multidimensionali NumPy (ndarray)
- Operazioni di aggregazione (sum, mean, std, ecc.)
- Slicing e indexing avanzato
- Manipolazione di dati 3D
- Statistiche descrittive
- Analisi di tendenze
================================================================================
"""

# ==============================================================================
# IMPORTAZIONE LIBRERIE
# ==============================================================================

import numpy as np
# numpy (np): Libreria fondamentale per il calcolo scientifico in Python
# Fornisce supporto per array multidimensionali e funzioni matematiche
# La importiamo con l'alias "np" per abbreviare la scrittura

import sys
# sys: Libreria standard Python per interagire con il sistema
# La usiamo principalmente per sys.exit() che termina il programma


# ==============================================================================
# FUNZIONE: stampa_menu()
# ==============================================================================

def stampa_menu():
    """
    Visualizza il menù principale del programma
    
    SCOPO:
    Mostra all'utente tutte le opzioni disponibili in modo chiaro e organizzato.
    Questa funzione non restituisce nulla (None), serve solo per stampare.
    
    DIDATTICA:
    - Uso di print() per output su console
    - Stringhe multilinea con caratteri speciali e emoji
    - Formattazione output per migliorare la leggibilità
    """
    
    # print(): Funzione built-in Python per stampare testo su console
    # "\n" è il carattere di "a capo" (newline)
    # "="*60 crea una stringa di 60 caratteri "=" (moltiplicazione di stringhe)
    print("\n" + "="*60)
    
    # Le emoji (🏪, 📊, ecc.) sono caratteri Unicode che rendono l'interfaccia
    # più accattivante e moderna
    print("🏪 SISTEMA DI ANALISI VENDITE - ELETTRONICA TECH")
    print("="*60)
    
    # Ogni opzione del menù è numerata per facilitare la scelta dell'utente
    print("1. 📊 Visualizza dati vendite settimanali")
    print("2. 💰 Calcola ricavi totali per prodotto")
    print("3. 📈 Trova prodotto più/meno venduto")
    print("4. 📅 Analizza vendite per giorno della settimana")
    print("5. 🎯 Calcola statistiche avanzate")
    print("6. 🔄 Confronta performance tra settimane")
    print("7. 📉 Identifica tendenze (crescita/calo)")
    print("8. 🆕 Inserisci nuovi dati vendita")
    print("0. ❌ Esci")
    print("="*60)


# ==============================================================================
# FUNZIONE: inizializza_dati()
# ==============================================================================

def inizializza_dati():
    """
    Crea e inizializza tutti i dati necessari per il programma
    
    SCOPO:
    Genera un array 3D di vendite simulate e le strutture dati associate
    (prezzi, nomi prodotti, giorni della settimana).
    
    RETURN:
    - vendite: array NumPy 3D di shape (5, 7, 4)
    - prezzi: array NumPy 1D con 5 prezzi
    - prodotti: lista Python con 5 nomi
    - giorni: lista Python con 7 giorni abbreviati
    
    CONCETTI NUMPY:
    - np.random.seed(): Per risultati riproducibili
    - np.random.randint(): Generazione numeri casuali interi
    - np.array(): Creazione array NumPy da lista
    - shape 3D: (prodotti, giorni, settimane)
    """
    
    # -------------------------------------------------------------------------
    # IMPOSTAZIONE SEED PER RIPRODUCIBILITÀ
    # -------------------------------------------------------------------------
    
    np.random.seed(42)
    # seed(): Imposta il "seme" del generatore di numeri casuali
    # Con lo stesso seed, otterremo sempre gli stessi numeri "casuali"
    # Utile per testing e didattica (tutti avranno gli stessi dati)
    # Il numero 42 è arbitrario (riferimento a "Guida Galattica per Autostoppisti")
    
    # -------------------------------------------------------------------------
    # CREAZIONE ARRAY 3D DELLE VENDITE
    # -------------------------------------------------------------------------
    
    vendite = np.random.randint(5, 30, size=(5, 7, 4))
    # Analizziamo questa istruzione in dettaglio:
    
    # np.random.randint(low, high, size):
    #   - low=5: valore minimo (incluso)
    #   - high=30: valore massimo (escluso, quindi max è 29)
    #   - size=(5, 7, 4): dimensioni dell'array da creare
    
    # SHAPE (5, 7, 4):
    #   - Dimensione 0 (5): Rappresenta i 5 PRODOTTI
    #   - Dimensione 1 (7): Rappresenta i 7 GIORNI della settimana
    #   - Dimensione 2 (4): Rappresenta le 4 SETTIMANE
    
    # INTERPRETAZIONE:
    # vendite[i, j, k] = numero di unità vendute del prodotto i
    #                    nel giorno j della settimana k
    
    # ESEMPIO:
    # vendite[0, 0, 0] = vendite Smartphone il Lunedì della Settimana 1
    # vendite[1, 5, 2] = vendite Laptop il Sabato della Settimana 3
    
    # -------------------------------------------------------------------------
    # CREAZIONE ARRAY 1D DEI PREZZI
    # -------------------------------------------------------------------------
    
    prezzi = np.array([299.99, 599.99, 149.99, 899.99, 199.99])
    # np.array(): Crea un array NumPy da una lista Python
    # Questo è un array 1D (monodimensionale) con 5 elementi
    # Ogni elemento rappresenta il prezzo in euro di un prodotto
    
    # CORRISPONDENZA:
    # prezzi[0] = 299.99 € (Smartphone)
    # prezzi[1] = 599.99 € (Laptop)
    # prezzi[2] = 149.99 € (Cuffie Bluetooth)
    # prezzi[3] = 899.99 € (Tablet Pro)
    # prezzi[4] = 199.99 € (Smartwatch)
    
    # -------------------------------------------------------------------------
    # CREAZIONE LISTE PYTHON PER NOMI
    # -------------------------------------------------------------------------
    
    prodotti = [
        "Smartphone",
        "Laptop", 
        "Cuffie Bluetooth",
        "Tablet Pro",
        "Smartwatch"
    ]
    # Lista Python standard (NON array NumPy)
    # Contiene stringhe con i nomi dei prodotti
    # L'indice corrisponde alla prima dimensione dell'array vendite
    # prodotti[0] corrisponde a vendite[0, :, :]
    
    giorni = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]
    # Lista con abbreviazioni dei giorni della settimana
    # L'indice corrisponde alla seconda dimensione dell'array vendite
    # giorni[0]="Lun" corrisponde a vendite[:, 0, :]
    
    # -------------------------------------------------------------------------
    # RETURN: Restituzione di tutti i dati
    # -------------------------------------------------------------------------
    
    return vendite, prezzi, prodotti, giorni
    # Python permette di restituire più valori contemporaneamente
    # Sono impacchettati in una tupla e poi spacchettati dal chiamante


# ==============================================================================
# FUNZIONE: visualizza_dati()
# ==============================================================================

def visualizza_dati(vendite, prodotti, giorni, settimana=0):
    """
    Visualizza i dati di vendita in formato tabellare per una settimana
    
    PARAMETRI:
    - vendite: array NumPy 3D (5, 7, 4)
    - prodotti: lista con nomi prodotti
    - giorni: lista con nomi giorni
    - settimana: indice della settimana da visualizzare (default=0, cioè prima)
    
    SCOPO:
    Crea una tabella ben formattata che mostra:
    - Vendite per ogni prodotto, per ogni giorno
    - Totali di riga (per prodotto)
    - Totali di colonna (per giorno)
    - Totale generale
    
    CONCETTI NUMPY:
    - Slicing 3D: vendite[i, j, k]
    - sum() su un asse specifico
    - Iterazione su array
    
    CONCETTI PYTHON:
    - f-string per formattazione
    - Specificatori di formato (:>6, :<20)
    - end="" per print su stessa riga
    """
    
    # -------------------------------------------------------------------------
    # INTESTAZIONE TABELLA
    # -------------------------------------------------------------------------
    
    print(f"\n📊 VENDITE SETTIMANA {settimana + 1}")
    # f-string: Permette di inserire variabili direttamente nella stringa
    # {settimana + 1}: Gli array partono da 0, ma per l'utente partiamo da 1
    
    print("-" * 70)
    # Linea separatrice di 70 trattini
    
    # -------------------------------------------------------------------------
    # INTESTAZIONE COLONNE
    # -------------------------------------------------------------------------
    
    print(f"{'Prodotto':<20}", end="")
    # Formattazione stringa avanzata:
    # {'Prodotto':<20} significa:
    #   - 'Prodotto' è il testo da stampare
    #   - :<20 significa allineamento a sinistra (<) in uno spazio di 20 caratteri
    # end="" dice a print di NON andare a capo (default è end="\n")
    
    for giorno in giorni:
        # Itera su ogni giorno della settimana
        print(f"{giorno:>6}", end="")
        # :>6 = allineamento a destra (>) in 6 caratteri
        # Utile per numeri che vogliamo incolonnati
    
    print(f"{'TOTALE':>8}")
    # Ultima colonna (andrà a capo perché non c'è end="")
    
    print("-" * 70)
    
    # -------------------------------------------------------------------------
    # RIGHE CON DATI
    # -------------------------------------------------------------------------
    
    for i, prodotto in enumerate(prodotti):
        # enumerate(): Restituisce coppie (indice, valore)
        # i = 0, 1, 2, 3, 4 (indice)
        # prodotto = "Smartphone", "Laptop", ecc. (valore)
        
        print(f"{prodotto:<20}", end="")
        # Stampa nome prodotto allineato a sinistra
        
        # ---------------------------------------------------------------------
        # SLICING NUMPY: Accesso ai dati dell'array 3D
        # ---------------------------------------------------------------------
        
        for giorno in range(7):
            # range(7) genera: 0, 1, 2, 3, 4, 5, 6 (indici dei giorni)
            
            print(f"{vendite[i, giorno, settimana]:>6}", end="")
            # FONDAMENTALE: vendite[i, giorno, settimana]
            # Accediamo all'array 3D con tre indici:
            #   - i: indice prodotto (0-4)
            #   - giorno: indice giorno (0-6)
            #   - settimana: indice settimana (parametro della funzione)
            # Restituisce un SINGOLO VALORE (scalare)
        
        # ---------------------------------------------------------------------
        # NUMPY SLICING: Calcolo totale di riga
        # ---------------------------------------------------------------------
        
        totale = vendite[i, :, settimana].sum()
        # vendite[i, :, settimana]:
        #   - i: prodotto specifico
        #   - : (due punti) = "tutti i valori" = tutti i 7 giorni
        #   - settimana: settimana specifica
        # Risultato: array 1D con 7 valori (uno per giorno)
        # .sum(): Somma tutti gli elementi dell'array → totale vendite prodotto
        
        print(f"{totale:>8}")
        # Stampa totale allineato a destra in 8 caratteri
    
    # -------------------------------------------------------------------------
    # RIGA TOTALI PER GIORNO
    # -------------------------------------------------------------------------
    
    print("-" * 70)
    print(f"{'TOTALE GIORNALIERO':<20}", end="")
    
    for giorno in range(7):
        # Per ogni giorno, calcoliamo il totale di TUTTI i prodotti
        
        print(f"{vendite[:, giorno, settimana].sum():>6}", end="")
        # vendite[:, giorno, settimana]:
        #   - : = tutti i prodotti (0-4)
        #   - giorno: giorno specifico
        #   - settimana: settimana specifica
        # Risultato: array 1D con 5 valori (uno per prodotto)
        # .sum(): Somma tutti i prodotti per quel giorno
    
    # -------------------------------------------------------------------------
    # TOTALE GENERALE
    # -------------------------------------------------------------------------
    
    print(f"{vendite[:, :, settimana].sum():>8}")
    # vendite[:, :, settimana]:
    #   - : = tutti i prodotti
    #   - : = tutti i giorni
    #   - settimana: settimana specifica
    # Risultato: array 2D (5x7) con TUTTI i dati della settimana
    # .sum(): Somma TUTTO → totale generale della settimana


# ==============================================================================
# FUNZIONE: calcola_ricavi()
# ==============================================================================

def calcola_ricavi(vendite, prezzi, prodotti):
    """
    Calcola i ricavi totali moltiplicando quantità vendute per prezzi
    
    PARAMETRI:
    - vendite: array 3D (5, 7, 4)
    - prezzi: array 1D (5,)
    - prodotti: lista nomi prodotti
    
    RETURN:
    - ricavi: array 1D con ricavi per prodotto
    
    CONCETTI NUMPY CHIAVE:
    - Aggregazione multi-asse: sum(axis=(1, 2))
    - Broadcasting: moltiplicazione array di forme diverse
    - Operazioni vettorizzate: più efficienti dei loop
    """
    
    print("\n💰 RICAVI TOTALI PER PRODOTTO (tutte le settimane)")
    print("-" * 50)
    
    # -------------------------------------------------------------------------
    # AGGREGAZIONE MULTI-ASSE
    # -------------------------------------------------------------------------
    
    vendite_totali = vendite.sum(axis=(1, 2))
    # CRUCIALE: sum(axis=(1, 2))
    # Somma lungo gli assi 1 (giorni) e 2 (settimane) CONTEMPORANEAMENTE
    
    # PRIMA DELLA SOMMA:
    # vendite.shape = (5, 7, 4)
    #   - 5 prodotti
    #   - 7 giorni
    #   - 4 settimane
    
    # DOPO sum(axis=(1, 2)):
    # vendite_totali.shape = (5,)
    # Abbiamo "collassato" gli assi 1 e 2, mantenendo solo l'asse 0
    # Risultato: array 1D con 5 valori (totale vendite per prodotto)
    
    # COSA SIGNIFICA:
    # vendite_totali[0] = somma di vendite[0, :, :] 
    #                   = totale Smartphone in tutti i giorni e settimane
    
    # ALTERNATIVA EQUIVALENTE (meno efficiente):
    # vendite_totali = vendite.sum(axis=1).sum(axis=1)
    # Prima somma i giorni, poi le settimane
    
    # -------------------------------------------------------------------------
    # BROADCASTING: Moltiplicazione elemento per elemento
    # -------------------------------------------------------------------------
    
    ricavi = vendite_totali * prezzi
    # MAGIA DEL BROADCASTING!
    # vendite_totali: shape (5,) = [467, 443, 435, 442, 459]
    # prezzi:         shape (5,) = [299.99, 599.99, 149.99, 899.99, 199.99]
    
    # NumPy moltiplica elemento per elemento:
    # ricavi[0] = vendite_totali[0] * prezzi[0] = 467 * 299.99
    # ricavi[1] = vendite_totali[1] * prezzi[1] = 443 * 599.99
    # ... e così via
    
    # SENZA NumPy dovresti scrivere:
    # ricavi = []
    # for i in range(5):
    #     ricavi.append(vendite_totali[i] * prezzi[i])
    
    # Con NumPy è:
    # - Più conciso
    # - Più veloce (implementato in C)
    # - Più leggibile
    
    # -------------------------------------------------------------------------
    # VISUALIZZAZIONE RISULTATI
    # -------------------------------------------------------------------------
    
    for i, prodotto in enumerate(prodotti):
        print(f"{prodotto:<20} | Unità vendute: {vendite_totali[i]:>4} | "
              f"Ricavo: €{ricavi[i]:>10,.2f}")
        # Formattazione numeri:
        # :>4 = allinea destra, 4 caratteri
        # :>10,.2f = allinea destra, 10 caratteri, virgola migliaia, 2 decimali
        # La virgola (,) aggiunge separatore migliaia: 140095.33 → 140,095.33
        # .2f = fixed point, 2 cifre decimali
    
    print("-" * 50)
    
    # -------------------------------------------------------------------------
    # TOTALI COMPLESSIVI
    # -------------------------------------------------------------------------
    
    print(f"{'TOTALE':<20} | Unità vendute: {vendite_totali.sum():>4} | "
          f"Ricavo: €{ricavi.sum():>10,.2f}")
    # .sum() su array 1D somma tutti gli elementi
    # vendite_totali.sum() = totale unità vendute di TUTTI i prodotti
    # ricavi.sum() = ricavo totale dell'intero negozio
    
    return ricavi


# ==============================================================================
# FUNZIONE: trova_prodotto_top()
# ==============================================================================

def trova_prodotto_top(vendite, prodotti):
    """
    Identifica il prodotto più venduto e quello meno venduto
    
    CONCETTI NUMPY:
    - argmax(): Trova l'INDICE del valore massimo
    - argmin(): Trova l'INDICE del valore minimo
    - Differenza tra max()/min() e argmax()/argmin()
    """
    
    print("\n📈 ANALISI PERFORMANCE PRODOTTI")
    print("-" * 50)
    
    # -------------------------------------------------------------------------
    # AGGREGAZIONE TOTALE
    # -------------------------------------------------------------------------
    
    vendite_totali = vendite.sum(axis=(1, 2))
    # Come prima: somma su giorni e settimane
    # Risultato: array (5,) con vendite totali per prodotto
    
    # -------------------------------------------------------------------------
    # ARGMAX E ARGMIN: Trovare INDICI dei valori estremi
    # -------------------------------------------------------------------------
    
    idx_max = vendite_totali.argmax()
    # argmax(): Restituisce l'INDICE dell'elemento con valore MASSIMO
    # NON restituisce il valore, ma la sua POSIZIONE
    
    # ESEMPIO:
    # Se vendite_totali = [467, 443, 435, 442, 459]
    # Il massimo è 467 (indice 0)
    # idx_max = 0
    
    idx_min = vendite_totali.argmin()
    # argmin(): Restituisce l'INDICE dell'elemento con valore MINIMO
    
    # ESEMPIO:
    # Il minimo è 435 (indice 2)
    # idx_min = 2
    
    # CONFRONTO:
    # .max()     → restituisce il VALORE massimo (467)
    # .argmax()  → restituisce l'INDICE del massimo (0)
    
    # PERCHÉ ARGMAX È UTILE:
    # Conoscendo l'indice, possiamo accedere ad altre informazioni correlate:
    # - prodotti[idx_max] → nome del prodotto
    # - prezzi[idx_max] → prezzo del prodotto
    # - vendite[idx_max, :, :] → tutti i dati del prodotto
    
    # -------------------------------------------------------------------------
    # VISUALIZZAZIONE RISULTATI
    # -------------------------------------------------------------------------
    
    print(f"🏆 Prodotto PIÙ venduto: {prodotti[idx_max]}")
    # Usiamo l'indice per accedere al nome nella lista
    
    print(f"   Unità vendute: {vendite_totali[idx_max]}")
    # Usiamo l'indice per accedere al valore nell'array
    
    print(f"\n⚠️  Prodotto MENO venduto: {prodotti[idx_min]}")
    print(f"   Unità vendute: {vendite_totali[idx_min]}")
    
    # -------------------------------------------------------------------------
    # CALCOLO PERCENTUALE
    # -------------------------------------------------------------------------
    
    diff = ((vendite_totali[idx_max] - vendite_totali[idx_min]) / 
            vendite_totali[idx_min] * 100)
    # Formula variazione percentuale:
    # ((nuovo - vecchio) / vecchio) * 100
    
    # ESEMPIO:
    # Se max=467 e min=435:
    # diff = ((467 - 435) / 435) * 100 = (32 / 435) * 100 ≈ 7.4%
    
    print(f"\n📊 Il prodotto top vende il {diff:.1f}% in più del meno venduto")
    # :.1f = 1 cifra decimale


# ==============================================================================
# FUNZIONE: analizza_giorni()
# ==============================================================================

def analizza_giorni(vendite, giorni):
    """
    Analizza le vendite aggregate per giorno della settimana
    
    SCOPO:
    Risponde alla domanda: "Quale giorno della settimana vendiamo di più?"
    
    CONCETTI NUMPY:
    - Aggregazione su assi multipli con scelta degli assi
    - Confronto con media
    - Conditional logic con operatori
    """
    
    print("\n📅 ANALISI VENDITE PER GIORNO DELLA SETTIMANA")
    print("-" * 50)
    
    # -------------------------------------------------------------------------
    # AGGREGAZIONE SPECIFICA: Somma per giorno
    # -------------------------------------------------------------------------
    
    vendite_per_giorno = vendite.sum(axis=(0, 2))
    # sum(axis=(0, 2)): Somma lungo assi 0 (prodotti) e 2 (settimane)
    
    # PRIMA:
    # vendite.shape = (5, 7, 4)
    #   Asse 0: prodotti
    #   Asse 1: giorni
    #   Asse 2: settimane
    
    # DOPO sum(axis=(0, 2)):
    # vendite_per_giorno.shape = (7,)
    # Abbiamo mantenuto solo l'asse 1 (giorni)
    
    # SIGNIFICATO:
    # vendite_per_giorno[0] = vendite totali del Lunedì
    #   (sommando tutti i prodotti in tutte le settimane)
    # vendite_per_giorno[1] = vendite totali del Martedì
    # ... e così via
    
    # VISUALIZZAZIONE MENTALE:
    # Immagina di "schiacciare" l'array 3D eliminando prodotti e settimane,
    # lasciando solo i 7 giorni con i loro totali
    
    # -------------------------------------------------------------------------
    # CALCOLO MEDIA
    # -------------------------------------------------------------------------
    
    media = vendite_per_giorno.mean()
    # .mean(): Calcola la media aritmetica di tutti gli elementi
    # media = (Lun + Mar + Mer + Gio + Ven + Sab + Dom) / 7
    
    # -------------------------------------------------------------------------
    # ITERAZIONE E CONFRONTO
    # -------------------------------------------------------------------------
    
    for i, giorno in enumerate(giorni):
        pezzi = vendite_per_giorno[i]
        # Vendite totali di questo giorno
        
        diff = pezzi - media
        # Differenza rispetto alla media
        # Positivo = sopra media, Negativo = sotto media
        
        # LOGICA CONDIZIONALE
        indicatore = "📈" if diff > 0 else "📉"
        # Operatore ternario: condizione ? valore_se_vero : valore_se_falso
        # Se diff > 0: indicatore = "📈" (freccia su)
        # Altrimenti:  indicatore = "📉" (freccia giù)
        
        print(f"{giorno}: {pezzi:>4} unità {indicatore} "
              f"({diff:+.0f} rispetto alla media)")
        # :+.0f = mostra sempre il segno (+/-), 0 decimali
    
    print("-" * 50)
    print(f"Media giornaliera: {media:.1f} unità")
    
    # -------------------------------------------------------------------------
    # IDENTIFICAZIONE ESTREMI
    # -------------------------------------------------------------------------
    
    idx_best = vendite_per_giorno.argmax()
    idx_worst = vendite_per_giorno.argmin()
    # Come visto prima: troviamo gli indici dei valori min/max
    
    print(f"\n🌟 Giorno migliore: {giorni[idx_best]} "
          f"({vendite_per_giorno[idx_best]} unità)")
    print(f"⚡ Giorno peggiore: {giorni[idx_worst]} "
          f"({vendite_per_giorno[idx_worst]} unità)")


# ==============================================================================
# FUNZIONE: statistiche_avanzate()
# ==============================================================================

def statistiche_avanzate(vendite, prodotti):
    """
    Calcola statistiche descrittive per ogni prodotto
    
    STATISTICHE CALCOLATE:
    - Media: valore centrale (media aritmetica)
    - Mediana: valore che divide i dati a metà
    - Deviazione standard: misura della dispersione dei dati
    - Min/Max: valori estremi
    - Range: differenza tra max e min
    - Quartili: valori che dividono i dati in quarti
    
    CONCETTI NUMPY:
    - flatten(): Trasforma array multidimensionale in 1D
    - Funzioni statistiche: mean(), median(), std(), min(), max()
    - percentile(): Calcolo percentili
    """
    
    print("\n🎯 STATISTICHE AVANZATE")
    print("-" * 70)
    
    for i, prodotto in enumerate(prodotti):
        
        # ---------------------------------------------------------------------
        # FLATTEN: Appiattimento array
        # ---------------------------------------------------------------------
        
        dati_prodotto = vendite[i, :, :].flatten()
        # vendite[i, :, :]:
        #   - i: prodotto specifico
        #   - :, : = tutti i giorni, tutte le settimane
        # Risultato: array 2D di shape (7, 4) = 28 valori
        
        # .flatten(): Trasforma array di qualsiasi forma in 1D
        # (7, 4) → (28,)
        # Prende tutti i valori e li mette in fila
        
        # ESEMPIO:
        # [[11, 19, 14, 26],
        #  [23, 29,  6, 15],
        #  ...] 
        # Diventa:
        # [11, 19, 14, 26, 23, 29, 6, 15, ...]
        
        # PERCHÉ FLATTEN?
        # Le funzioni statistiche lavorano meglio su array 1D
        # Vogliamo considerare tutti i giorni/settimane come singole osservazioni
        
        print(f"\n{prodotto}:")
        
        # ---------------------------------------------------------------------
        # STATISTICHE DI TENDENZA CENTRALE
        # ---------------------------------------------------------------------
        
        print(f"  • Media vendite giornaliere: {dati_prodotto.mean():.2f}")
        # .mean(): Media aritmetica
        # Formula: (x₁ + x₂ + ... + xₙ) / n
        # Rappresenta il valore "tipico" o "centrale"
        
        print(f"  • Mediana: {np.median(dati_prodotto):.2f}")
        # np.median(): Valore centrale quando i dati sono ordinati
        # Se hai 28 valori ordinati, la mediana è tra il 14° e 15° valore
        # Meno sensibile agli outlier rispetto alla media
        
        # DIFFERENZA MEDIA vs MEDIANA:
        # Dati: [1, 2, 3, 4, 100]
        # Media = 22 (influenzata dal 100)
        # Mediana = 3 (valore centrale, non influenzata)
        
        # ---------------------------------------------------------------------
        # STATISTICHE DI DISPERSIONE
        # ---------------------------------------------------------------------
        
        print(f"  • Deviazione standard: {dati_prodotto.std():.2f}")
        # .std(): Standard Deviation (deviazione standard)
        # Misura quanto i dati sono "sparsi" rispetto alla media
        # Valore basso = dati concentrati vicino alla media
        # Valore alto = dati molto variabili
        
        # FORMULA (semplificata):
        # std = √(Σ(xᵢ - media)² / n)
        
        # ---------------------------------------------------------------------
        # VALORI ESTREMI
        # ---------------------------------------------------------------------
        
        print(f"  • Min: {dati_prodotto.min()} | Max: {dati_prodotto.max()}")
        # .min(): Valore minimo nell'array
        # .max(): Valore massimo nell'array
        
        print(f"  • Range: {dati_prodotto.max() - dati_prodotto.min()}")
        # Range = differenza tra max e min
        # Misura semplice della variabilità
        
        # ---------------------------------------------------------------------
        # QUARTILI
        # ---------------------------------------------------------------------
        
        q1, q3 = np.percentile(dati_prodotto, [25, 75])
        # np.percentile(data, [p1, p2, ...]):
        # Calcola i percentili specificati
        
        # QUARTILI:
        # Q1 (25° percentile): 25% dei dati è sotto questo valore
        # Q2 (50° percentile): = mediana
        # Q3 (75° percentile): 75% dei dati è sotto questo valore
        
        # INTERPRETAZIONE:
        # Se Q1=11 e Q3=23:
        # - Il 25% delle giornate vende ≤11 unità
        # - Il 50% delle giornate vende tra 11 e 23 unità
        # - Il 25% delle giornate vende ≥23 unità
        
        print(f"  • Q1 (25%): {q1:.1f} | Q3 (75%): {q3:.1f}")
        
        # IQR (Interquartile Range) = Q3 - Q1
        # Misura la dispersione del 50% centrale dei dati
        # Utile per identificare outlier


# ==============================================================================
# FUNZIONE: confronta_settimane()
# ==============================================================================

def confronta_settimane(vendite, prodotti):
    """
    Confronta le performance tra diverse settimane
    
    SCOPO:
    - Identificare quale settimana ha avuto le migliori vendite
    - Analizzare il trend per ogni prodotto
    
    CONCETTI NUMPY:
    - np.diff(): Calcola differenze consecutive
    - Aggregazioni su assi specifici
    - Analisi di serie temporali
    """
    
    print("\n🔄 CONFRONTO TRA SETTIMANE")
    print("-" * 70)
    
    n_settimane = vendite.shape[2]
    # .shape[2]: Accede alla dimensione dell'asse 2 (settimane)
    # vendite.shape = (5, 7, 4), quindi shape[2] = 4
    
    # -------------------------------------------------------------------------
    # AGGREGAZIONE PER SETTIMANA
    # -------------------------------------------------------------------------
    
    vendite_settimana = vendite.sum(axis=(0, 1))
    # sum(axis=(0, 1)): Somma prodotti (asse 0) e giorni (asse 1)
    # Risultato: array (4,) con totale vendite per ogni settimana
    
    # VISUALIZZAZIONE:
    # [593, 565, 544, 544] ← vendite totali delle 4 settimane
    
    print("Vendite totali per settimana:")
    for i in range(n_settimane):
        print(f"  Settimana {i+1}: {vendite_settimana[i]:>4} unità")
    
    # -------------------------------------------------------------------------
    # IDENTIFICAZIONE SETTIMANA MIGLIORE
    # -------------------------------------------------------------------------
    
    idx_best = vendite_settimana.argmax()
    print(f"\n🏆 Settimana migliore: Settimana {idx_best + 1} "
          f"({vendite_settimana[idx_best]} unità)")
    
    # -------------------------------------------------------------------------
    # ANALISI TREND PER PRODOTTO
    # -------------------------------------------------------------------------
    
    print("\n📈 TREND PER PRODOTTO:")
    
    for i, prodotto in enumerate(prodotti):
        
        vendite_prodotto = vendite[i, :, :].sum(axis=0)
        # vendite[i, :, :]: tutti i dati del prodotto i
        # sum(axis=0): somma i giorni (asse 0 dell'array 2D risultante)
        # Risultato: array (4,) con vendite per settimana del prodotto
        
        # ---------------------------------------------------------------------
        # NUMPY DIFF: Calcolo differenze consecutive
        # ---------------------------------------------------------------------
        
        trend = np.diff(vendite_prodotto)
        # np.diff(): Calcola differenze tra elementi consecutivi
        
        # ESEMPIO:
        # Se vendite_prodotto = [128, 122, 106, 111]
        # trend = [122-128, 106-122, 111-106]
        #       = [-6, -16, +5]
        
        # INTERPRETAZIONE:
        # trend[0] = -6: dalla sett. 1 alla 2, vendite calate di 6 unità
        # trend[1] = -16: dalla sett. 2 alla 3, vendite calate di 16 unità
        # trend[2] = +5: dalla sett. 3 alla 4, vendite aumentate di 5 unità
        
        # DIMENSIONI:
        # Se vendite_prodotto ha n elementi
        # trend avrà n-1 elementi (perché calcola differenze tra coppie)
        
        trend_medio = trend.mean()
        # Media delle variazioni settimanali
        # Positivo = crescita media
        # Negativo = calo medio
        
        # ---------------------------------------------------------------------
        # LOGICA CONDIZIONALE PER CLASSIFICAZIONE
        # ---------------------------------------------------------------------
        
        if trend_medio > 0:
            stato = "🔼 CRESCITA"
        elif trend_medio < 0:
            stato = "🔽 CALO"
        else:
            stato = "➡️  STABILE"
        # if-elif-else: struttura decisionale
        
        print(f"  {prodotto:<20} {stato} ({trend_medio:+.1f} unità/settimana)")
        # :+.1f mostra sempre il segno (+/-)


# ==============================================================================
# FUNZIONE: identifica_tendenze()
# ==============================================================================

def identifica_tendenze(vendite, prodotti):
    """
    Identifica tendenze di crescita o calo usando correlazione
    
    CONCETTI AVANZATI:
    - Correlazione lineare
    - np.corrcoef(): Coefficiente di correlazione di Pearson
    - Interpretazione statistica
    
    TEORIA:
    Correlazione misura la relazione lineare tra due variabili
    Valore tra -1 e +1:
    - +1: correlazione positiva perfetta (crescita lineare)
    - 0: nessuna correlazione
    - -1: correlazione negativa perfetta (decrescita lineare)
    """
    
    print("\n📉 ANALISI TENDENZE")
    print("-" * 70)
    
    for i, prodotto in enumerate(prodotti):
        
        # ---------------------------------------------------------------------
        # PREPARAZIONE DATI
        # ---------------------------------------------------------------------
        
        vendite_sett = vendite[i, :, :].sum(axis=0)
        # Vendite per settimana del prodotto (array con 4 valori)
        
        # ---------------------------------------------------------------------
        # NUMPY ARANGE: Creazione sequenza numerica
        # ---------------------------------------------------------------------
        
        x = np.arange(len(vendite_sett))
        # np.arange(n): Crea array [0, 1, 2, ..., n-1]
        # Equivalente a range() ma restituisce array NumPy
        
        # Se vendite_sett ha 4 elementi:
        # x = [0, 1, 2, 3]
        # Rappresenta il "tempo" (settimane in ordine)
        
        # ---------------------------------------------------------------------
        # CORRELAZIONE: Misura della relazione lineare
        # ---------------------------------------------------------------------
        
        correlazione = np.corrcoef(x, vendite_sett)[0, 1]
        # np.corrcoef(x, y): Calcola matrice di correlazione
        
        # MATRICE DI CORRELAZIONE:
        # [[corr(x,x), corr(x,y)],
        #  [corr(y,x), corr(y,y)]]
        
        # Diagonale = 1 (ogni variabile correlata perfettamente con se stessa)
        # [0, 1] = correlazione tra x e y (quello che vogliamo)
        
        # INTERPRETAZIONE COEFFICIENTE:
        # 0.7 < r ≤ 1.0: Forte correlazione positiva → Forte crescita
        # 0.3 < r ≤ 0.7: Debole correlazione positiva → Leggera crescita
        # -0.3 ≤ r ≤ 0.3: Nessuna correlazione → Stabile
        # -0.7 ≤ r < -0.3: Debole correlazione negativa → Leggero calo
        # -1.0 ≤ r < -0.7: Forte correlazione negativa → Forte calo
        
        # ESEMPIO VISIVO:
        # x = [0, 1, 2, 3]
        # y = [100, 110, 120, 130] → r ≈ +1 (crescita perfetta)
        # y = [130, 120, 110, 100] → r ≈ -1 (decrescita perfetta)
        # y = [100, 130, 105, 125] → r ≈ 0 (nessun pattern)
        
        print(f"\n{prodotto}:")
        print(f"  Vendite per settimana: {vendite_sett}")
        
        # ---------------------------------------------------------------------
        # CLASSIFICAZIONE BASATA SU SOGLIE
        # ---------------------------------------------------------------------
        
        if correlazione > 0.7:
            print(f"  ✅ Forte tendenza CRESCITA (corr: {correlazione:.2f})")
        elif correlazione > 0.3:
            print(f"  📈 Leggera tendenza CRESCITA (corr: {correlazione:.2f})")
        elif correlazione < -0.7:
            print(f"  ❌ Forte tendenza CALO (corr: {correlazione:.2f})")
        elif correlazione < -0.3:
            print(f"  📉 Leggera tendenza CALO (corr: {correlazione:.2f})")
        else:
            print(f"  ➡️  STABILE (corr: {correlazione:.2f})")


# ==============================================================================
# FUNZIONE: inserisci_dati()
# ==============================================================================

def inserisci_dati(vendite, prodotti, giorni):
    """
    Permette all'utente di inserire manualmente nuovi dati
    
    SCOPO:
    Interazione utente per modificare l'array esistente
    
    CONCETTI:
    - Input utente con validazione
    - Modifica di array NumPy esistenti
    - Gestione errori con try-except
    """
    
    print("\n🆕 INSERIMENTO NUOVI DATI")
    print("-" * 50)
    
    # -------------------------------------------------------------------------
    # VISUALIZZAZIONE OPZIONI
    # -------------------------------------------------------------------------
    
    print("Prodotti disponibili:")
    for i, prodotto in enumerate(prodotti):
        print(f"  {i+1}. {prodotto}")
    
    # -------------------------------------------------------------------------
    # GESTIONE ERRORI: Try-Except
    # -------------------------------------------------------------------------
    
    try:
        # try: Blocco di codice che potrebbe generare errori
        
        # ---------------------------------------------------------------------
        # INPUT UTENTE
        # ---------------------------------------------------------------------
        
        prod_idx = int(input("\nSeleziona prodotto (1-5): ")) - 1
        # input(): Legge stringa dall'utente
        # int(): Converte stringa in intero (può generare ValueError)
        # -1: Convertiamo da numerazione umana (1-5) a indici array (0-4)
        
        # VALIDAZIONE INPUT
        if prod_idx < 0 or prod_idx >= len(prodotti):
            print("❌ Prodotto non valido!")
            return vendite
        # Controlla che l'indice sia nel range valido [0, 4]
        
        sett = int(input("Seleziona settimana (1-4): ")) - 1
        if sett < 0 or sett >= 4:
            print("❌ Settimana non valida!")
            return vendite
        
        # ---------------------------------------------------------------------
        # RACCOLTA DATI E MODIFICA ARRAY
        # ---------------------------------------------------------------------
        
        print(f"\nInserisci vendite per {prodotti[prod_idx]} - Settimana {sett+1}:")
        
        for i, giorno in enumerate(giorni):
            valore = int(input(f"  {giorno}: "))
            
            # MODIFICA ARRAY IN-PLACE
            vendite[prod_idx, i, sett] = valore
            # Gli array NumPy sono MUTABILI
            # Questa assegnazione modifica l'array originale
            # vendite[i, j, k] = valore sostituisce il valore esistente
        
        print("\n✅ Dati aggiornati con successo!")
    
    # -------------------------------------------------------------------------
    # GESTIONE ECCEZIONI
    # -------------------------------------------------------------------------
    
    except ValueError:
        # ValueError: Sollevata quando int() riceve input non numerico
        # Es: input="abc" → int("abc") → ValueError
        print("❌ Errore: inserire solo numeri!")
    
    # -------------------------------------------------------------------------
    # RETURN
    # -------------------------------------------------------------------------
    
    return vendite
    # Restituiamo l'array modificato
    # NOTA: Poiché NumPy usa reference, l'array è già modificato
    # Il return è più per chiarezza che per necessità


# ==============================================================================
# FUNZIONE PRINCIPALE: main()
# ==============================================================================

def main():
    """
    Funzione principale che coordina l'intero programma
    
    STRUTTURA:
    1. Inizializzazione dati
    2. Loop infinito del menù
    3. Gestione scelte utente
    4. Chiamate alle funzioni appropriate
    
    CONCETTI:
    - Loop while infinito
    - Pattern menu-driven
    - Gestione input utente
    - Error handling
    """
    
    # -------------------------------------------------------------------------
    # INTESTAZIONE PROGRAMMA
    # -------------------------------------------------------------------------
    
    print("\n" + "="*60)
    print("🎓 COMPITO DI REALTÀ: Analisi Vendite con NumPy")
    print("="*60)
    print("Benvenuto nel sistema di analisi vendite!")
    print("Imparerai a usare array NumPy per analizzare dati reali.")
    
    # -------------------------------------------------------------------------
    # INIZIALIZZAZIONE DATI
    # -------------------------------------------------------------------------
    
    vendite, prezzi, prodotti, giorni = inizializza_dati()
    # Unpacking: La funzione restituisce 4 valori impacchettati in tupla
    # Li spacchetta e assegna a 4 variabili separate
    
    # -------------------------------------------------------------------------
    # LOOP PRINCIPALE DEL PROGRAMMA
    # -------------------------------------------------------------------------
    
    while True:
        # while True: Loop infinito
        # Si ripete finché non viene chiamato sys.exit() o break
        
        stampa_menu()
        
        # ---------------------------------------------------------------------
        # GESTIONE INPUT E ERRORI
        # ---------------------------------------------------------------------
        
        try:
            scelta = input("\n👉 Scegli un'opzione (0-8): ").strip()
            # input(): Legge stringa dall'utente
            # .strip(): Rimuove spazi bianchi all'inizio e fine
            #   "  3  ".strip() → "3"
            
            # -----------------------------------------------------------------
            # DISPATCH: Esecuzione basata su scelta
            # -----------------------------------------------------------------
            
            if scelta == "0":
                # USCITA DAL PROGRAMMA
                print("\n👋 Grazie per aver usato il sistema. Arrivederci!")
                sys.exit(0)
                # sys.exit(0): Termina il programma
                # 0 = codice di uscita (0 = successo)
            
            elif scelta == "1":
                # VISUALIZZA DATI SETTIMANA
                sett = int(input("Quale settimana vuoi visualizzare? (1-4): ")) - 1
                
                if 0 <= sett < 4:
                    # Verifica che settimana sia valida
                    visualizza_dati(vendite, prodotti, giorni, sett)
                else:
                    print("❌ Settimana non valida!")
            
            elif scelta == "2":
                # CALCOLA RICAVI
                calcola_ricavi(vendite, prezzi, prodotti)
            
            elif scelta == "3":
                # TROVA PRODOTTO TOP
                trova_prodotto_top(vendite, prodotti)
            
            elif scelta == "4":
                # ANALIZZA GIORNI
                analizza_giorni(vendite, giorni)
            
            elif scelta == "5":
                # STATISTICHE AVANZATE
                statistiche_avanzate(vendite, prodotti)
            
            elif scelta == "6":
                # CONFRONTA SETTIMANE
                confronta_settimane(vendite, prodotti)
            
            elif scelta == "7":
                # IDENTIFICA TENDENZE
                identifica_tendenze(vendite, prodotti)
            
            elif scelta == "8":
                # INSERISCI DATI
                vendite = inserisci_dati(vendite, prodotti, giorni)
                # Aggiorniamo la variabile vendite con l'array modificato
            
            else:
                # SCELTA NON VALIDA
                print("❌ Opzione non valida! Riprova.")
            
            # -----------------------------------------------------------------
            # PAUSA PER LETTURA
            # -----------------------------------------------------------------
            
            input("\n⏸️  Premi INVIO per continuare...")
            # Aspetta che l'utente prema Invio prima di continuare
            # Permette di leggere i risultati senza che il menù riappaia subito
        
        # ---------------------------------------------------------------------
        # GESTIONE ECCEZIONI
        # ---------------------------------------------------------------------
        
        except ValueError:
            # ValueError: Errore di conversione tipo (es: int("abc"))
            print("❌ Errore: inserire un numero valido!")
            input("\n⏸️  Premi INVIO per continuare...")
        
        except KeyboardInterrupt:
            # KeyboardInterrupt: Sollevata quando utente preme Ctrl+C
            print("\n\n👋 Uscita dal programma. Arrivederci!")
            sys.exit(0)


# ==============================================================================
# ENTRY POINT DEL PROGRAMMA
# ==============================================================================

if __name__ == "__main__":
    # __name__: Variabile speciale Python
    # Quando il file è eseguito direttamente: __name__ == "__main__"
    # Quando il file è importato: __name__ == nome del modulo
    
    # PATTERN STANDARD:
    # Permette di:
    # 1. Eseguire il programma: python script.py
    # 2. Importare funzioni: from script import calcola_ricavi
    
    main()
    # Chiamata alla funzione principale
    # Qui inizia l'esecuzione del programma


"""
================================================================================
RIEPILOGO CONCETTI NUMPY UTILIZZATI
================================================================================

1. CREAZIONE ARRAY
   - np.array(): Da lista Python
   - np.random.randint(): Numeri casuali interi
   - np.random.seed(): Riproducibilità
   - np.arange(): Sequenze numeriche

2. SHAPE E DIMENSIONI
   - .shape: Ottiene dimensioni array
   - .ndim: Numero di dimensioni
   - .size: Numero totale elementi

3. INDEXING E SLICING
   - arr[i, j, k]: Accesso singolo elemento
   - arr[i, :, k]: Slice con "tutti i valori"
   - arr[:, :, :]: Tutti gli elementi

4. AGGREGAZIONI
   - .sum(): Somma elementi
   - .sum(axis=n): Somma lungo asse specifico
   - .sum(axis=(n, m)): Somma lungo più assi
   - .mean(): Media
   - .min(), .max(): Minimo e massimo

5. FUNZIONI STATISTICHE
   - .std(): Deviazione standard
   - np.median(): Mediana
   - np.percentile(): Percentili
   - np.corrcoef(): Correlazione

6. RICERCA
   - .argmax(): Indice del massimo
   - .argmin(): Indice del minimo

7. MANIPOLAZIONE
   - .flatten(): Appiattimento array
   - np.diff(): Differenze consecutive

8. BROADCASTING
   - Operazioni elemento per elemento su array di forme compatibili
   - Esempio: array(5,) * array(5,) = array(5,)

================================================================================
BEST PRACTICES OSSERVATE
================================================================================

1. NAMING: Nomi variabili descrittivi (vendite_totali, idx_max)
2. COMMENTI: Spiegazioni chiare del codice
3. DOCSTRINGS: Documentazione funzioni
4. VALIDAZIONE: Controllo input utente
5. ERROR HANDLING: Try-except per gestire errori
6. MODULARITÀ: Funzioni separate per task specifici
7. FORMATTAZIONE: Output ben formattato e leggibile
8. UX: Messaggi chiari e interfaccia user-friendly

================================================================================
PATTERNS DI PROGRAMMAZIONE
================================================================================

1. MENU-DRIVEN: Loop principale con menù scelte
2. SEPARATION OF CONCERNS: Ogni funzione ha uno scopo specifico
3. DRY (Don't Repeat Yourself): Codice riutilizzabile
4. DEFENSIVE PROGRAMMING: Validazione input e gestione errori
5. SINGLE RESPONSIBILITY: Ogni funzione fa una cosa sola

================================================================================
"""