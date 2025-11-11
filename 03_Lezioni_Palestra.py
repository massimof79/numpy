#!/usr/bin/env python3
"""
GymAnalytics - versione semplificata (senza grafici)
Genera riepiloghi testuali:
  - lezione più / meno seguita
  - partecipanti totali per lezione (settimana)
  - accessi giornalieri e media
  - fatturato giornaliero per sede (tabellare)

Requisiti: numpy
Esecuzione: python3 gymanalytics_simplificato.py
"""

import numpy as np

# --------------------------
# Configurazione dati
# --------------------------
LEZIONI = {
    1: ["Yoga", 8.00, 50, 1],
    2: ["Pilates", 9.00, 60, 1],
    3: ["CrossFit", 12.00, 200, 1],
    4: ["HIIT", 11.00, 220, 1],
    5: ["Spinning", 10.00, 300, 1],
    6: ["Zumba", 8.50, 180, 1],
    7: ["Functional", 10.50, 190, 1],
    8: ["Boxe", 12.50, 250, 1],
    9: ["Calisthenics", 11.50, 170, 1],
    10:["Mobility", 7.50, 80, 1]
}

SEDI = ["Centro", "Nord", "Sud", "Est"]
GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

prices = np.array([LEZIONI[i+1][1] for i in range(len(LEZIONI))])

# --------------------------
# Dati partecipazioni (fittizi)
# Shape: (7 giorni, 4 sedi, 10 lezioni)
# --------------------------
partecipazioni_settimana = np.array([
    [[18, 16, 12, 14, 15, 20, 13, 10, 9, 12],
     [14, 13, 10, 11, 12, 16, 11, 9, 8, 10],
     [15, 14, 11, 12, 13, 18, 12, 9, 8, 11],
     [16, 14, 11, 12, 13, 17, 12, 9, 8, 10]],

    [[20, 18, 13, 15, 16, 22, 14, 11, 10, 13],
     [15, 14, 11, 12, 13, 18, 12, 10, 9, 11],
     [17, 15, 12, 13, 14, 19, 13, 10, 9, 12],
     [16, 15, 12, 13, 14, 18, 13, 10, 9, 11]],

    [[21, 19, 14, 16, 17, 23, 15, 12, 10, 13],
     [16, 15, 12, 13, 14, 19, 13, 10, 9, 12],
     [18, 16, 13, 14, 15, 20, 14, 11, 10, 12],
     [17, 16, 12, 13, 14, 19, 13, 10, 9, 12]],

    [[22, 20, 15, 17, 18, 24, 16, 12, 11, 14],
     [17, 16, 13, 14, 15, 20, 14, 11, 10, 12],
     [19, 17, 14, 15, 16, 21, 15, 12, 10, 13],
     [18, 17, 13, 14, 15, 20, 14, 11, 10, 12]],

    [[28, 25, 20, 22, 24, 30, 21, 18, 16, 20],
     [24, 22, 18, 20, 21, 27, 19, 16, 14, 18],
     [26, 23, 19, 21, 23, 29, 20, 17, 15, 19],
     [25, 23, 19, 20, 22, 28, 20, 17, 15, 19]],

    [[30, 27, 22, 24, 26, 32, 23, 20, 18, 22],
     [26, 24, 19, 21, 23, 29, 21, 18, 16, 20],
     [28, 25, 21, 23, 25, 31, 22, 19, 17, 21],
     [27, 25, 20, 22, 24, 30, 22, 18, 17, 20]],

    [[29, 26, 21, 23, 25, 31, 22, 19, 17, 21],
     [25, 23, 18, 20, 22, 28, 20, 17, 15, 19],
     [27, 24, 20, 22, 24, 30, 21, 18, 16, 20],
     [26, 24, 19, 21, 23, 29, 21, 18, 16, 19]]
], dtype=int)

# --------------------------
# Funzioni utili
# --------------------------
def add_booking(partecipazioni, giorno, sede, lesson_id, quantita=1):
    """
    Aggiunge `quantita` di prenotazioni alla lezione `lesson_id` per giorno e sede specificati.
    Indici: giorno 0..6, sede 0..3, lesson_id 1..10.
    Restituisce copia modificata delle partecipazioni.
    """
    if not (0 <= giorno < partecipazioni.shape[0]):
        raise IndexError("Indice giorno fuori range (0..6).")
    if not (0 <= sede < partecipazioni.shape[1]):
        raise IndexError("Indice sede fuori range (0..3).")
    if not (1 <= lesson_id <= partecipazioni.shape[2]):
        raise IndexError("lesson_id fuori range (1..10).")
    new = partecipazioni.copy()
    new[giorno, sede, lesson_id - 1] += quantita
    return new

def calcola_statistiche(partecipazioni):
    """
    Restituisce dizionario con:
      - totale_per_lezione (array)
      - accessi_giornalieri (array, 7)
      - fatturato_per_sede (array 7x4)
      - lezione_piu_seguita, lezione_meno_seguita, qty_piu, qty_meno
    """

    #collassa gli assi dei giorni e delle sedi, resta solo la dimensione delle lezioni
    totale_per_lezione = partecipazioni.sum(axis=(0,1))
    idx_max = int(np.argmax(totale_per_lezione))
    idx_min = int(np.argmin(totale_per_lezione))
    lezione_piu = LEZIONI[idx_max + 1][0]
    lezione_meno = LEZIONI[idx_min + 1][0]
    qty_piu = int(totale_per_lezione[idx_max])
    qty_meno = int(totale_per_lezione[idx_min])


    ##Cicla un numero di volte parli alla lunghezza della dimensione 0
    for g in range(partecipazioni.shape[0]):
        somma_giorno = partecipazioni[g].sum()   # somma dei valori del giorno g
        accessi_giornalieri.append(somma_giorno)

    #converto la lista in un array numpy
    accessi_giornalieri = np.array(accessi_giornalieri)
    
    fatturato_per_sede = np.zeros((partecipazioni.shape[0], partecipazioni.shape[1]))
    for g in range(partecipazioni.shape[0]):
        fatturato_per_sede[g] = (partecipazioni[g] * prices).sum(axis=1)

    return {
        "totale_per_lezione": totale_per_lezione,
        "accessi_giornalieri": accessi_giornalieri,
        "fatturato_per_sede": fatturato_per_sede,
        "lezione_piu": lezione_piu,
        "lezione_meno": lezione_meno,
        "qty_piu": qty_piu,
        "qty_meno": qty_meno
    }


""" 2. partecipazioni.shape[0]
shape restituisce una tupla con le dimensioni dell’array.
partecipazioni.shape[0] → numero di righe → numero di giorni.

3. for g in range(partecipazioni.shape[0])
Cicla su tutti gli indici di riga (cioè su ogni giorno).

4. partecipazioni[g].sum()
partecipazioni[g] estrae la riga g (un array 1D contenente i valori di quel giorno).
.sum() calcola la somma dei valori di quella riga (cioè il totale dei partecipanti in quel giorno).

5. [partecipazioni[g].sum() for g in range(...)]
Crea una lista che contiene la somma giornaliera per ogni riga.
 """




# --------------------------
# Output testuale
# --------------------------
def stampa_riassunto(stats):
    print("GymAnalytics - Riepilogo settimanale\n")
    print(f"Lezione più seguita: {stats['lezione_piu']} (partecipanti: {stats['qty_piu']})")
    print(f"Lezione meno seguita: {stats['lezione_meno']} (partecipanti: {stats['qty_meno']})\n")

    print("Partecipanti totali per lezione (settimana):")
    lezioni_nomi = [LEZIONI[i+1][0] for i in range(len(LEZIONI))]
    for nome, tot in zip(lezioni_nomi, stats['totale_per_lezione']):
        print(f"  {nome}: {int(tot)}")

    print("\nAccessi giornalieri:")
    for i, g in enumerate(GIORNI):
        print(f"  {g}: {int(stats['accessi_giornalieri'][i])} accessi")
    print(f"Accessi medi giornalieri: {stats['accessi_giornalieri'].mean():.2f}\n")

    print("Fatturato giornaliero per sede (tabella: righe=giorni, colonne=sedi):")
    header = "Giorno".ljust(12) + "".join(s.ljust(10) for s in SEDI)
    print(header)
    for i, g in enumerate(GIORNI):
        row = g.ljust(12) + "".join(f"{stats['fatturato_per_sede'][i, j]:<10.2f}" for j in range(len(SEDI)))
        print(row)

# --------------------------
# Main
# --------------------------
def main():
    stats = calcola_statistiche(partecipazioni_settimana)
    stampa_riassunto(stats)

    # Esempio d'uso della funzione add_booking (commentata)
    # partecipazioni_mod = add_booking(partecipazioni_settimana, giorno=2, sede=1, lesson_id=3, quantita=2)
    # stats2 = calcola_statistiche(partecipazioni_mod)
    # stampa_riassunto(stats2)

if __name__ == "__main__":
    main()
