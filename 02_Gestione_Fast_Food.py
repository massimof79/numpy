#!/usr/bin/env python3
"""
BurgerPython - versione semplice
Analisi vendite settimanali con NumPy: registrazione ordini (funzione),
prodotto più/meno venduto, ricavo giornaliero, ricavo medio, fatturato per zona.
Solo calcoli e stampe su console.
"""

import numpy as np

# --------------------------
# Dati: menu e filiali
# --------------------------
MENU = {
    1: ["Hamburger Classic", 5.50, 550, 5],
    2: ["Cheeseburger", 6.00, 650, 5],
    3: ["Double Burger", 8.50, 900, 7],
    4: ["Chicken Burger", 6.50, 500, 6],
    5: ["Veggie Burger", 7.00, 450, 6],
    6: ["Patatine Piccole", 2.50, 300, 3],
    7: ["Patatine Grandi", 4.00, 500, 3],
    8: ["Coca Cola", 2.00, 150, 1],
    9: ["Acqua", 1.50, 0, 1],
    10:["Milkshake", 4.50, 400, 4]
}

FILIALI = ["Centro", "Nord", "Sud", "Est"]
GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

# prezzi come vettore (index 0 -> prodotto 1)
prices = np.array([MENU[i+1][1] for i in range(len(MENU))])

# --------------------------
# Dati vendite forniti
# Shape: (7 giorni, 4 filiali, 10 prodotti)
# --------------------------
vendite_settimana = np.array([
    [[45, 38, 22, 30, 15, 55, 40, 60, 25, 20],
     [35, 30, 18, 25, 12, 45, 35, 50, 20, 15],
     [40, 35, 20, 28, 14, 50, 38, 55, 22, 18],
     [38, 32, 19, 26, 13, 48, 36, 52, 21, 16]],

    [[48, 40, 24, 32, 16, 58, 42, 63, 26, 22],
     [38, 32, 20, 27, 14, 48, 37, 53, 22, 17],
     [43, 37, 22, 30, 15, 53, 40, 58, 24, 19],
     [40, 34, 21, 28, 14, 50, 38, 55, 23, 18]],

    [[50, 42, 25, 34, 17, 60, 44, 65, 28, 23],
     [40, 34, 22, 29, 15, 50, 39, 55, 23, 18],
     [45, 38, 23, 31, 16, 55, 42, 60, 25, 20],
     [42, 36, 22, 29, 15, 52, 40, 57, 24, 19]],

    [[52, 44, 26, 35, 18, 62, 46, 67, 29, 24],
     [42, 36, 23, 30, 16, 52, 41, 57, 24, 19],
     [47, 40, 24, 33, 17, 57, 44, 62, 26, 21],
     [44, 38, 23, 31, 16, 54, 42, 59, 25, 20]],

    [[65, 55, 35, 45, 22, 75, 58, 80, 35, 30],
     [55, 48, 30, 38, 20, 68, 52, 72, 32, 26],
     [60, 52, 33, 42, 21, 72, 56, 77, 34, 28],
     [58, 50, 32, 40, 21, 70, 54, 75, 33, 27]],

    [[70, 60, 38, 48, 25, 80, 62, 85, 38, 32],
     [60, 52, 33, 42, 22, 73, 56, 78, 35, 28],
     [65, 56, 36, 46, 24, 77, 60, 82, 37, 30],
     [62, 54, 34, 44, 23, 75, 58, 80, 36, 29]],

    [[68, 58, 36, 47, 24, 78, 60, 83, 37, 31],
     [58, 50, 32, 41, 21, 71, 54, 76, 34, 27],
     [63, 54, 35, 45, 23, 75, 58, 80, 36, 29],
     [60, 52, 33, 43, 22, 73, 56, 78, 35, 28]]
], dtype=int)

# --------------------------
# Funzione per registrare un ordine
# --------------------------
def add_order(vendite, giorno, filiale, product_id, quantita=1):
    """
    Aggiunge `quantita` al prodotto `product_id` per il giorno `giorno` e la filiale `filiale`.
    Gli indici: giorno 0..6, filiale 0..3, product_id 1..10.
    Restituisce una nuova matrice vendite (non modifica l'array originale).
    """
    if not (0 <= giorno < vendite.shape[0]):
        raise IndexError("Indice giorno fuori range (0..6).")
    if not (0 <= filiale < vendite.shape[1]):
        raise IndexError("Indice filiale fuori range (0..3).")
    if not (1 <= product_id <= vendite.shape[2]):
        raise IndexError("product_id fuori range (1..10).")
    new = vendite.copy()
    new[giorno, filiale, product_id - 1] += quantita
    return new

# --------------------------
# Analisi principali
# --------------------------
def analisi_e_stampe(vendite):
    # totale venduto per prodotto (somma su giorni e filiali)
    totale_per_prodotto = vendite.sum(axis=(0,1))  # shape (10,)

    # prodotto più e meno venduto
    idx_max = int(np.argmax(totale_per_prodotto))  # 0-based
    idx_min = int(np.argmin(totale_per_prodotto))
    prodotto_piu = MENU[idx_max + 1][0]
    prodotto_meno = MENU[idx_min + 1][0]
    qty_piu = int(totale_per_prodotto[idx_max])
    qty_meno = int(totale_per_prodotto[idx_min])

    # ricavo giornaliero (somma su filiali e prodotti di qty * prezzo)
    ricavo_giornaliero = np.array([
        (vendite[g] * prices).sum() for g in range(vendite.shape[0])
    ])
    ricavo_medio = float(ricavo_giornaliero.mean())

    # fatturato giornaliero per zona (giorni x filiali)
    fatturato_per_zona = np.zeros((vendite.shape[0], vendite.shape[1]))
    for g in range(vendite.shape[0]):
        # per filiale somma prodotti: (10,) -> sum axis 1 produce 4 valori
        fatturato_per_zona[g] = (vendite[g] * prices).sum(axis=1)

    # Stampe
    print("Analisi vendite - BurgerPython (versione semplice)\n")
    print(f"Prodotto più venduto: {prodotto_piu} (quantità totale: {qty_piu})")
    print(f"Prodotto meno venduto: {prodotto_meno} (quantità totale: {qty_meno})\n")

    print("Ricavo giornaliero totale:")
    for i, giorno in enumerate(GIORNI):
        print(f"  {giorno}: €{ricavo_giornaliero[i]:.2f}")
    print(f"\nRicavo medio giornaliero: €{ricavo_medio:.2f}\n")

    print("Fatturato giornaliero per zona (Centro, Nord, Sud, Est):")
    for i, giorno in enumerate(GIORNI):
        row = fatturato_per_zona[i]
        print(f"  {giorno}: Centro: €{row[0]:.2f}, Nord: €{row[1]:.2f}, Sud: €{row[2]:.2f}, Est: €{row[3]:.2f}")

# --------------------------
# Esecuzione principale
# --------------------------
def main():
    # Analisi sui dati originali
    analisi_e_stampe(vendite_settimana)

    # Esempio (facoltativo): come registrare un ordine
    # Qui un esempio non interattivo: aggiungo 3 Double Burger il Martedì nella filiale Sud
    vendite_modificate = add_order(vendite_settimana, giorno=1, filiale=2, product_id=3, quantita=3)

    print("\n[Esempio] Dopo aver registrato 3 Double Burger (Martedì, filiale Sud):\n")
    analisi_e_stampe(vendite_modificate)

if __name__ == "__main__":
    main()
