"""
ESERCIZIO: Sistema di Monitoraggio Qualità dell'Aria
Studente: ___________________
Data: ___________________
"""

import numpy as np

# SETUP: Creazione dati simulati (NON MODIFICARE)
np.random.seed(42)

# Dimensioni: (7 giorni, 5 zone, 4 inquinanti)
# Inquinanti: [PM10, PM2.5, NO2, O3]
# Zone: [Centro, Nord, Sud, Est, Ovest]

dati_aria = np.array([
    # Giorno 1
    [[45, 28, 52, 48], [38, 22, 45, 55], [42, 25, 48, 52], [40, 24, 50, 50], [35, 20, 42, 58]],
    # Giorno 2
    [[52, 32, 58, 45], [45, 28, 52, 48], [48, 30, 55, 46], [46, 29, 53, 47], [40, 25, 48, 52]],
    # Giorno 3
    [[65, 42, 68, 38], [58, 38, 62, 42], [62, 40, 65, 40], [60, 39, 64, 41], [52, 35, 58, 48]],
    # Giorno 4
    [[72, 48, 75, 35], [65, 42, 68, 40], [68, 45, 72, 38], [66, 44, 70, 39], [58, 38, 62, 45]],
    # Giorno 5
    [[55, 35, 60, 42], [48, 30, 55, 48], [52, 32, 58, 45], [50, 31, 57, 46], [42, 28, 50, 52]],
    # Giorno 6
    [[38, 22, 45, 55], [32, 18, 40, 62], [35, 20, 42, 58], [34, 19, 41, 60], [28, 16, 38, 65]],
    # Giorno 7
    [[42, 25, 48, 52], [36, 21, 44, 58], [40, 24, 46, 55], [38, 22, 45, 56], [32, 19, 42, 62]]
])

giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
zone = ['Centro', 'Nord', 'Sud', 'Est', 'Ovest']
inquinanti = ['PM10', 'PM2.5', 'NO2', 'O3']

# Valori limite secondo normative (μg/m³)
limiti = {'PM10': 50, 'PM2.5': 25, 'NO2': 40, 'O3': 120}

print("="*60)
print("SISTEMA DI MONITORAGGIO QUALITÀ DELL'ARIA")
print("="*60)

# ============================================================================
# PARTE 1: ESPLORAZIONE DELLA STRUTTURA DATI
# ============================================================================
print("\n--- PARTE 1: Analisi della Struttura ---\n")

# TODO 1.1: Stampa la forma (shape) dell'array
print("1.1) Dimensioni dell'array:")
# Scrivi qui il tuo codice


# TODO 1.2: Stampa il numero totale di elementi
print("\n1.2) Numero totale di misurazioni:")
# Scrivi qui il tuo codice


# TODO 1.3: Stampa il tipo di dato contenuto
print("\n1.3) Tipo di dato:")
# Scrivi qui il tuo codice


# TODO 1.4: Estrai e stampa i dati del Mercoledì (giorno 3, indice 2)
print("\n1.4) Dati di Mercoledì:")
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 2: ANALISI STATISTICHE BASE
# ============================================================================
print("\n\n--- PARTE 2: Statistiche Base ---\n")

# TODO 2.1: Calcola la concentrazione media di PM10 per tutta la settimana
print("2.1) Concentrazione media di PM10 nella settimana:")
# Hint: usa slicing per estrarre solo i dati PM10 (indice 0 degli inquinanti)
# Scrivi qui il tuo codice


# TODO 2.2: Trova il valore massimo di PM2.5 registrato e in quale giorno/zona
print("\n2.2) Valore massimo di PM2.5:")
# Scrivi qui il tuo codice
# Bonus: usa np.unravel_index per trovare la posizione


# TODO 2.3: Calcola la media di ogni inquinante per tutta la settimana
print("\n2.3) Media settimanale per inquinante:")
# Hint: calcola la media lungo gli assi giorni e zone
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 3: ANALISI PER ZONE
# ============================================================================
print("\n\n--- PARTE 3: Analisi per Zone ---\n")

# TODO 3.1: Calcola la media di inquinanti per ogni zona (media su giorni)
print("3.1) Media di inquinanti per zona (tutta la settimana):")
# Scrivi qui il tuo codice


# TODO 3.2: Identifica la zona più inquinata (quella con PM10 medio più alto)
print("\n3.2) Zona con PM10 medio più alto:")
# Scrivi qui il tuo codice


# TODO 3.3: Confronta la zona Centro con la zona Ovest
print("\n3.3) Confronto Centro vs Ovest:")
# Calcola la differenza media di PM10 tra le due zone
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 4: ANALISI TEMPORALE
# ============================================================================
print("\n\n--- PARTE 4: Analisi Temporale ---\n")

# TODO 4.1: Calcola la media giornaliera di tutti gli inquinanti
print("4.1) Media giornaliera complessiva:")
# Scrivi qui il tuo codice


# TODO 4.2: Confronta weekend (Sabato-Domenica) con giorni feriali
print("\n4.2) Confronto Feriali vs Weekend:")
# Hint: usa slicing per separare i giorni
# Scrivi qui il tuo codice


# TODO 4.3: Identifica il giorno più pulito (con valori medi più bassi)
print("\n4.3) Giorno con aria più pulita:")
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 5: SUPERAMENTI DEI LIMITI
# ============================================================================
print("\n\n--- PARTE 5: Analisi Superamenti Limiti ---\n")

# TODO 5.1: Conta quante volte PM10 ha superato il limite (50 μg/m³)
print("5.1) Superamenti limite PM10 (50 μg/m³):")
# Hint: usa operatori di confronto e np.sum
# Scrivi qui il tuo codice


# TODO 5.2: Crea un array booleano che indica dove PM2.5 supera 25
print("\n5.2) Mappa superamenti PM2.5:")
# Scrivi qui il tuo codice


# TODO 5.3: Calcola la percentuale di misurazioni fuori norma per NO2 (>40)
print("\n5.3) Percentuale superamenti NO2:")
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 6: OPERAZIONI AVANZATE
# ============================================================================
print("\n\n--- PARTE 6: Analisi Avanzate ---\n")

# TODO 6.1: Calcola l'indice di qualità dell'aria (AQI) semplificato
# AQI = media di tutti gli inquinanti normalizzati rispetto ai loro limiti
print("6.1) Indice di Qualità dell'Aria per zona:")
# Formula: AQI_zona = media((PM10/50 + PM2.5/25 + NO2/40) / 3)
# Scrivi qui il tuo codice


# TODO 6.2: Trova i 3 momenti (giorno, zona) peggiori per PM10
print("\n6.2) Top 3 peggiori misurazioni PM10:")
# Hint: usa np.argsort o np.argpartition
# Scrivi qui il tuo codice


# TODO 6.3: Calcola la variabilità (deviazione standard) di PM10 per zona
print("\n6.3) Variabilità PM10 per zona:")
# Questo indica quanto i valori oscillano durante la settimana
# Scrivi qui il tuo codice


# ============================================================================
# PARTE 7: VISUALIZZAZIONE DATI (BONUS)
# ============================================================================
print("\n\n--- PARTE 7: BONUS - Report Finale ---\n")

# TODO 7.1: Crea una matrice di correlazione tra i 4 inquinanti
print("7.1) Analisi correlazioni inquinanti:")
# Hint: usa np.corrcoef dopo aver appiattito opportunamente i dati
# Scrivi qui il tuo codice


# TODO 7.2: Genera un report testuale automatico
print("\n7.2) REPORT AUTOMATICO PER IL SINDACO:")
print("-" * 60)
# Usa i risultati calcolati per creare un breve report che includa:
# - Zona più critica
# - Giorno peggiore
# - Numero totale di superamenti
# - Raccomandazioni
# Scrivi qui il tuo codice


print("\n" + "="*60)
print("FINE ESERCIZIO")
print("="*60)

# ============================================================================
# DOMANDE DI RIFLESSIONE (da rispondere in forma scritta)
# ============================================================================
"""
1. Quali sono i vantaggi di usare un array 3D rispetto a tre array 2D separati?

2. In quali situazioni il metodo .reshape() potrebbe essere utile per questi dati?

3. Come cambieresti la struttura dati se dovessi aggiungere misurazioni orarie 
   invece che giornaliere?

4. Perché numpy è più efficiente delle liste Python per questo tipo di operazioni?

5. Proponi un'estensione del progetto: quali altri dati ambientali potrebbero 
   essere integrati e come organizzeresti un array 4D o 5D?
"""
