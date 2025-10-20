"""
ESERCIZIO: Sistema di Monitoraggio Qualità dell'Aria
Studente: SOLUZIONE COMPLETA
Data: 20/10/2025
"""

import numpy as np

# SETUP: Creazione dati simulati (NON MODIFICARE)
np.random.seed(42)

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

# Numero di elementi di ogni dimensione
# TODO 1.1: Stampa la forma (shape) dell'array
print("1.1) Dimensioni dell'array:")
print(f"Shape: {dati_aria.shape}")
print(f"(7 giorni, 5 zone, 4 inquinanti)")


# TODO 1.2: Stampa il numero totale di elementi
print("\n1.2) Numero totale di misurazioni:")
print(f"Elementi totali: {dati_aria.size}")

# TODO 1.3: Stampa il tipo di dato contenuto
print("\n1.3) Tipo di dato:")
print(f"Dtype: {dati_aria.dtype}")

# TODO 1.4: Estrai e stampa i dati del Mercoledì (giorno 3, indice 2)
print("\n1.4) Dati di Mercoledì:")
mercoledi = dati_aria[2]
print(mercoledi)
print(f"\nInterpretazione: 5 zone x 4 inquinanti")

# ============================================================================
# PARTE 2: ANALISI STATISTICHE BASE
# ============================================================================
print("\n\n--- PARTE 2: Statistiche Base ---\n")

# TODO 2.1: Calcola la concentrazione media di PM10 per tutta la settimana
print("2.1) Concentrazione media di PM10 nella settimana:")
#Tutti i giorni, tutte le zone poi prendo il primo elemento della terza dimensione
pm10_data = dati_aria[:, :, 0]  # Tutti i giorni, tutte le zone, solo PM10
media_pm10 = np.mean(pm10_data)
print(f"Media PM10: {media_pm10:.2f} μg/m³")

# TODO 2.2: Trova il valore massimo di PM2.5 registrato e in quale giorno/zona
print("\n2.2) Valore massimo di PM2.5:")
#Tutti i giorni, tutte le zone poi prendo il secondo elemento della terza dimensione
pm25_data = dati_aria[:, :, 1]
print("pm25_data: ", pm25_data)
max_pm25 = np.max(pm25_data)
print("Il massimo è: ", max_pm25)
#argmax trova la posizione dell'elemento come se si trovasse in un array ad una dimensione
print("Posizione del massimo in due dimensioni: ", np.argmax(pm25_data))
pos = np.unravel_index(np.argmax(pm25_data), pm25_data.shape)
print("Stampa la coordinata:", pos)
print(f"Valore massimo: {max_pm25} μg/m³")
print(f"Giorno: {giorni[pos[0]]}, Zona: {zone[pos[1]]}")

# TODO 2.3: Calcola la media di ogni inquinante per tutta la settimana
print("\n2.3) Media settimanale per inquinante:")
medie_inquinanti = np.mean(dati_aria, axis=(0, 1))
for i, inq in enumerate(inquinanti):
    print(f"{inq}: {medie_inquinanti[i]:.2f} μg/m³")

# ============================================================================
# PARTE 3: ANALISI PER ZONE
# ============================================================================
print("\n\n--- PARTE 3: Analisi per Zone ---\n")

# TODO 3.1: Calcola la media di inquinanti per ogni zona (media su giorni)
print("3.1) Media di inquinanti per zona (tutta la settimana):")
medie_zone = np.mean(dati_aria, axis=0)
for i, zona in enumerate(zone):
    print(f"\n{zona}:")
    for j, inq in enumerate(inquinanti):
        print(f"  {inq}: {medie_zone[i, j]:.2f} μg/m³")

# TODO 3.2: Identifica la zona più inquinata (quella con PM10 medio più alto)
print("\n3.2) Zona con PM10 medio più alto:")
pm10_per_zona = np.mean(dati_aria[:, :, 0], axis=0)
zona_peggiore = np.argmax(pm10_per_zona)
print(f"Zona: {zone[zona_peggiore]}")
print(f"PM10 medio: {pm10_per_zona[zona_peggiore]:.2f} μg/m³")

# TODO 3.3: Confronta la zona Centro con la zona Ovest
print("\n3.3) Confronto Centro vs Ovest:")
pm10_centro = np.mean(dati_aria[:, 0, 0])  # Centro = indice 0
pm10_ovest = np.mean(dati_aria[:, 4, 0])   # Ovest = indice 4
differenza = pm10_centro - pm10_ovest
print(f"PM10 medio Centro: {pm10_centro:.2f} μg/m³")
print(f"PM10 medio Ovest: {pm10_ovest:.2f} μg/m³")
print(f"Differenza: {differenza:.2f} μg/m³")
print(f"Centro è più inquinato di {differenza:.2f} μg/m³")

# ============================================================================
# PARTE 4: ANALISI TEMPORALE
# ============================================================================
print("\n\n--- PARTE 4: Analisi Temporale ---\n")

# TODO 4.1: Calcola la media giornaliera di tutti gli inquinanti
print("4.1) Media giornaliera complessiva:")
medie_giornaliere = np.mean(dati_aria, axis=(1, 2))
for i, giorno in enumerate(giorni):
    print(f"{giorno}: {medie_giornaliere[i]:.2f} μg/m³")

# TODO 4.2: Confronta weekend (Sabato-Domenica) con giorni feriali
print("\n4.2) Confronto Feriali vs Weekend:")
feriali = dati_aria[0:5]  # Lunedì-Venerdì
weekend = dati_aria[5:7]  # Sabato-Domenica
media_feriali = np.mean(feriali)
media_weekend = np.mean(weekend)
print(f"Media giorni feriali: {media_feriali:.2f} μg/m³")
print(f"Media weekend: {media_weekend:.2f} μg/m³")
print(f"Differenza: {media_feriali - media_weekend:.2f} μg/m³")
if media_feriali > media_weekend:
    print("→ L'aria è più pulita nel weekend")
else:
    print("→ L'aria è più inquinata nel weekend")

# TODO 4.3: Identifica il giorno più pulito (con valori medi più bassi)
print("\n4.3) Giorno con aria più pulita:")
giorno_migliore = np.argmin(medie_giornaliere)
print(f"Giorno: {giorni[giorno_migliore]}")
print(f"Media inquinanti: {medie_giornaliere[giorno_migliore]:.2f} μg/m³")

# ============================================================================
# PARTE 5: SUPERAMENTI DEI LIMITI
# ============================================================================
print("\n\n--- PARTE 5: Analisi Superamenti Limiti ---\n")

# TODO 5.1: Conta quante volte PM10 ha superato il limite (50 μg/m³)
print("5.1) Superamenti limite PM10 (50 μg/m³):")
superamenti_pm10 = np.sum(dati_aria[:, :, 0] > 50)
totale_misurazioni_pm10 = dati_aria[:, :, 0].size
print(f"Numero superamenti: {superamenti_pm10}")
print(f"Totale misurazioni: {totale_misurazioni_pm10}")
print(f"Percentuale: {(superamenti_pm10/totale_misurazioni_pm10)*100:.1f}%")

# TODO 5.2: Crea un array booleano che indica dove PM2.5 supera 25
print("\n5.2) Mappa superamenti PM2.5:")
superamenti_pm25 = dati_aria[:, :, 1] > 25
print("Array booleano (True = superamento):")
print(superamenti_pm25)
print(f"\nNumero totale superamenti: {np.sum(superamenti_pm25)}")

# TODO 5.3: Calcola la percentuale di misurazioni fuori norma per NO2 (>40)
print("\n5.3) Percentuale superamenti NO2:")
superamenti_no2 = np.sum(dati_aria[:, :, 2] > 40)
totale_no2 = dati_aria[:, :, 2].size
percentuale_no2 = (superamenti_no2 / totale_no2) * 100
print(f"Superamenti NO2: {superamenti_no2}/{totale_no2}")
print(f"Percentuale: {percentuale_no2:.1f}%")

# ============================================================================
# PARTE 6: OPERAZIONI AVANZATE
# ============================================================================
print("\n\n--- PARTE 6: Analisi Avanzate ---\n")

# TODO 6.1: Calcola l'indice di qualità dell'aria (AQI) semplificato
print("6.1) Indice di Qualità dell'Aria per zona:")
# Normalizzazione rispetto ai limiti (escluso O3 per semplicità)
pm10_norm = dati_aria[:, :, 0] / 50
pm25_norm = dati_aria[:, :, 1] / 25
no2_norm = dati_aria[:, :, 2] / 40

aqi_per_zona = np.mean((pm10_norm + pm25_norm + no2_norm) / 3, axis=0)
for i, zona in enumerate(zone):
    qualita = "BUONA" if aqi_per_zona[i] < 0.5 else "MODERATA" if aqi_per_zona[i] < 0.8 else "SCARSA"
    print(f"{zona}: {aqi_per_zona[i]:.3f} - {qualita}")

# TODO 6.2: Trova i 3 momenti (giorno, zona) peggiori per PM10
print("\n6.2) Top 3 peggiori misurazioni PM10:")
#Restituisce una copia dell'array collassato in una dimensione
pm10_flat = dati_aria[:, :, 0].flatten()
#Stampa array collassato
indices_peggiori = np.argsort(pm10_flat)[-3:][::-1]  # 3 peggiori, in ordine decrescente

print("Indice peggiori: ", indices_peggiori)


for idx in indices_peggiori:
    giorno_idx, zona_idx = np.unravel_index(idx, (7, 5))
    valore = dati_aria[giorno_idx, zona_idx, 0]
    print(f"{giorni[giorno_idx]}, {zone[zona_idx]}: {valore} μg/m³")

# TODO 6.3: Calcola la variabilità (deviazione standard) di PM10 per zona
print("\n6.3) Variabilità PM10 per zona:")
std_pm10_zone = np.std(dati_aria[:, :, 0], axis=0)
for i, zona in enumerate(zone):
    print(f"{zona}: {std_pm10_zone[i]:.2f} μg/m³ (dev. std.)")

# ============================================================================
# PARTE 7: VISUALIZZAZIONE DATI (BONUS)
# ============================================================================
print("\n\n--- PARTE 7: BONUS - Report Finale ---\n")

# TODO 7.1: Crea una matrice di correlazione tra i 4 inquinanti
print("7.1) Analisi correlazioni inquinanti:")
# Riorganizza i dati: (7*5) righe x 4 colonne
dati_reshapati = dati_aria.reshape(-1, 4)
matrice_corr = np.corrcoef(dati_reshapati.T)
print("\nMatrice di correlazione:")
print("          ", end="")
for inq in inquinanti:
    print(f"{inq:>8}", end="")
print()
for i, inq in enumerate(inquinanti):
    print(f"{inq:>8}: ", end="")
    for j in range(4):
        print(f"{matrice_corr[i,j]:>8.2f}", end="")
    print()

# TODO 7.2: Genera un report testuale automatico
print("\n7.2) REPORT AUTOMATICO PER IL SINDACO:")
print("-" * 60)

# Calcoli per il report
zona_critica_idx = np.argmax(aqi_per_zona)
giorno_peggiore_idx = np.argmax(medie_giornaliere)
totale_superamenti = (
    np.sum(dati_aria[:, :, 0] > 50) +  # PM10
    np.sum(dati_aria[:, :, 1] > 25) +  # PM2.5
    np.sum(dati_aria[:, :, 2] > 40)    # NO2
)

print(f"""
SINTESI SETTIMANALE QUALITÀ DELL'ARIA
Periodo: Settimana del {giorni[0]} - {giorni[-1]}

SITUAZIONE GENERALE:
• Zona più critica: {zone[zona_critica_idx]} (AQI: {aqi_per_zona[zona_critica_idx]:.3f})
• Giorno peggiore: {giorni[giorno_peggiore_idx]} ({medie_giornaliere[giorno_peggiore_idx]:.1f} μg/m³)
• Totale superamenti limiti: {totale_superamenti}

ANALISI PER INQUINANTE:
• PM10: media {medie_inquinanti[0]:.1f} μg/m³ (limite: 50) - {superamenti_pm10} superamenti
• PM2.5: media {medie_inquinanti[1]:.1f} μg/m³ (limite: 25) - {np.sum(superamenti_pm25)} superamenti
• NO2: media {medie_inquinanti[2]:.1f} μg/m³ (limite: 40) - {superamenti_no2} superamenti
• O3: media {medie_inquinanti[3]:.1f} μg/m³ (limite: 120) - nessun superamento

TREND:
• Feriali vs Weekend: {abs(media_feriali - media_weekend):.1f} μg/m³ di differenza
• L'aria è risultata {"più pulita nel weekend" if media_feriali > media_weekend else "più inquinata nel weekend"}

RACCOMANDAZIONI:
1. Implementare misure di contenimento traffico nella zona {zone[zona_critica_idx]}
2. Monitoraggio intensivo nei giorni di {giorni[giorno_peggiore_idx]}
3. Promuovere mobilità sostenibile per ridurre PM10 e NO2
4. Verificare fonti emissive nella zona Centro (PM10 medio: {pm10_centro:.1f} μg/m³)
""")

print("-" * 60)
print("\n" + "="*60)
print("FINE ESERCIZIO")
print("="*60)

# ============================================================================
# DOMANDE DI RIFLESSIONE (RISPOSTE)
# ============================================================================
print("\n\nRISPOSTE ALLE DOMANDE DI RIFLESSIONE:\n")
print("""
1. Vantaggi array 3D:
   - Struttura dati coerente e compatta
   - Operazioni vettorizzate su tutte le dimensioni
   - Facilita calcoli su assi specifici (giorni, zone, inquinanti)
   - Meno memoria rispetto a strutture separate

2. Utilità di .reshape():
   - Convertire da 3D a 2D per analisi di correlazione
   - Appiattire per ordinamenti o ricerche globali
   - Riorganizzare per diverse tipologie di analisi

3. Struttura per dati orari:
   - Array 4D: (giorni, ore, zone, inquinanti)
   - Shape: (7, 24, 5, 4) = 3360 misurazioni
   - Permette analisi su pattern orari

4. Efficienza di NumPy:
   - Operazioni implementate in C
   - Memoria contigua e ottimizzata
   - Broadcasting automatico
   - Nessun overhead di interpretazione Python

5. Estensione a 4D/5D:
   - 4D: aggiungere temperatura/umidità → (giorni, zone, inquinanti, meteo)
   - 5D: aggiungere mesi → (mesi, settimane, giorni, zone, parametri)
   - Permetterebbe analisi stagionali e trend annuali
""")