import numpy as np

# Menu prodotti: [Nome, Prezzo€, Calorie, Tempo preparazione (min)]
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
    10: ["Milkshake", 4.50, 400, 4]
}

# Punti vendita
FILIALI = ["Centro", "Nord", "Sud", "Est"]

# Dati simulati settimana scorsa
# Shape: (7 giorni, 4 filiali, 10 prodotti) = quantità vendute
np.random.seed(123)
vendite_settimana = np.array([
    # Lunedì
    [[45, 38, 22, 30, 15, 55, 40, 60, 25, 20],  # Centro
     [35, 30, 18, 25, 12, 45, 35, 50, 20, 15],  # Nord
     [40, 35, 20, 28, 14, 50, 38, 55, 22, 18],  # Sud
     [38, 32, 19, 26, 13, 48, 36, 52, 21, 16]], # Est
    
    # Martedì
    [[48, 40, 24, 32, 16, 58, 42, 63, 26, 22],
     [38, 32, 20, 27, 14, 48, 37, 53, 22, 17],
     [43, 37, 22, 30, 15, 53, 40, 58, 24, 19],
     [40, 34, 21, 28, 14, 50, 38, 55, 23, 18]],
    
    # Mercoledì
    [[50, 42, 25, 34, 17, 60, 44, 65, 28, 23],
     [40, 34, 22, 29, 15, 50, 39, 55, 23, 18],
     [45, 38, 23, 31, 16, 55, 42, 60, 25, 20],
     [42, 36, 22, 29, 15, 52, 40, 57, 24, 19]],
    
    # Giovedì
    [[52, 44, 26, 35, 18, 62, 46, 67, 29, 24],
     [42, 36, 23, 30, 16, 52, 41, 57, 24, 19],
     [47, 40, 24, 33, 17, 57, 44, 62, 26, 21],
     [44, 38, 23, 31, 16, 54, 42, 59, 25, 20]],
    
    # Venerdì
    [[65, 55, 35, 45, 22, 75, 58, 80, 35, 30],
     [55, 48, 30, 38, 20, 68, 52, 72, 32, 26],
     [60, 52, 33, 42, 21, 72, 56, 77, 34, 28],
     [58, 50, 32, 40, 21, 70, 54, 75, 33, 27]],
    
    # Sabato
    [[70, 60, 38, 48, 25, 80, 62, 85, 38, 32],
     [60, 52, 33, 42, 22, 73, 56, 78, 35, 28],
     [65, 56, 36, 46, 24, 77, 60, 82, 37, 30],
     [62, 54, 34, 44, 23, 75, 58, 80, 36, 29]],
    
    # Domenica
    [[68, 58, 36, 47, 24, 78, 60, 83, 37, 31],
     [58, 50, 32, 41, 21, 71, 54, 76, 34, 27],
     [63, 54, 35, 45, 23, 75, 58, 80, 36, 29],
     [60, 52, 33, 43, 22, 73, 56, 78, 35, 28]]
])


def analizza_vendite():
    """
    Funzione principale per analizzare le vendite di BurgerPython
    """
    print("=" * 70)
    print("🍔 ANALISI VENDITE BURGERPYTHON - SETTIMANA SCORSA 🍔")
    print("=" * 70)
    
    # Estrazione array prezzi dal menu
    prezzi = np.array([MENU[i][1] for i in range(1, 11)])
    
    # ===== 1. PRODOTTO PIÙ VENDUTO =====
    # Somma tutte le vendite per prodotto (su tutti i giorni e filiali)
    vendite_per_prodotto = vendite_settimana.sum(axis=(0, 1))
    
    prodotto_piu_venduto_idx = vendite_per_prodotto.argmax()
    quantita_max = vendite_per_prodotto[prodotto_piu_venduto_idx]
    nome_piu_venduto = MENU[prodotto_piu_venduto_idx + 1][0]
    
    print(f"\n📊 1. PRODOTTO PIÙ VENDUTO")
    print(f"   → {nome_piu_venduto}")
    print(f"   → Quantità totale: {quantita_max} unità")
    
    # ===== 2. PRODOTTO MENO VENDUTO =====
    prodotto_meno_venduto_idx = vendite_per_prodotto.argmin()
    quantita_min = vendite_per_prodotto[prodotto_meno_venduto_idx]
    nome_meno_venduto = MENU[prodotto_meno_venduto_idx + 1][0]
    
    print(f"\n📊 2. PRODOTTO MENO VENDUTO")
    print(f"   → {nome_meno_venduto}")
    print(f"   → Quantità totale: {quantita_min} unità")
    
    # ===== 3. RICAVO MEDIO GIORNALIERO =====
    # Calcola il fatturato per ogni giorno
    # Moltiplica le vendite per i prezzi e somma su filiali e prodotti
    fatturato_giornaliero = np.sum(vendite_settimana * prezzi, axis=(1, 2))
    ricavo_medio = fatturato_giornaliero.mean()
    
    print(f"\n💰 3. RICAVO MEDIO GIORNALIERO")
    print(f"   → €{ricavo_medio:,.2f}")
    
    giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    print(f"\n   Dettaglio giornaliero:")
    for i, giorno in enumerate(giorni):
        print(f"   • {giorno:10s}: €{fatturato_giornaliero[i]:,.2f}")
    
    # ===== 4. FATTURATO GIORNALIERO PER ZONA =====
    print(f"\n🗺️  4. FATTURATO GIORNALIERO RAGGRUPPATO PER ZONA")
    print(f"   {'':12s} | {'Centro':>12s} | {'Nord':>12s} | {'Sud':>12s} | {'Est':>12s} | {'TOTALE':>12s}")
    print(f"   {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12}")
    
    # Calcola fatturato per zona per ogni giorno
    fatturato_per_zona_giorno = np.sum(vendite_settimana * prezzi, axis=2)
    
    for i, giorno in enumerate(giorni):
        riga = f"   {giorno:12s}"
        for j in range(4):
            riga += f" | €{fatturato_per_zona_giorno[i, j]:>11,.2f}"
        totale_giorno = fatturato_per_zona_giorno[i].sum()
        riga += f" | €{totale_giorno:>11,.2f}"
        print(riga)
    
    # Totali per zona
    print(f"   {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12}")
    riga = f"   {'TOTALE':12s}"
    totale_generale = 0
    for j in range(4):
        totale_zona = fatturato_per_zona_giorno[:, j].sum()
        riga += f" | €{totale_zona:>11,.2f}"
        totale_generale += totale_zona
    riga += f" | €{totale_generale:>11,.2f}"
    print(riga)
    
    # ===== STATISTICHE EXTRA =====
    print(f"\n📈 STATISTICHE AGGIUNTIVE")
    print(f"   • Fatturato totale settimanale: €{totale_generale:,.2f}")
    print(f"   • Prodotti totali venduti: {vendite_per_prodotto.sum():,} unità")
    print(f"   • Giorno con più incassi: {giorni[fatturato_giornaliero.argmax()]} (€{fatturato_giornaliero.max():,.2f})")
    print(f"   • Giorno con meno incassi: {giorni[fatturato_giornaliero.argmin()]} (€{fatturato_giornaliero.min():,.2f})")
    
    # Zona più redditizia
    fatturato_per_zona_totale = fatturato_per_zona_giorno.sum(axis=0)
    zona_migliore_idx = fatturato_per_zona_totale.argmax()
    print(f"   • Zona più redditizia: {FILIALI[zona_migliore_idx]} (€{fatturato_per_zona_totale[zona_migliore_idx]:,.2f})")
    
    print("\n" + "=" * 70)


def mostra_menu():
    """
    Visualizza il menu dei prodotti disponibili
    """
    print("\n" + "=" * 70)
    print("📋 MENU BURGERPYTHON")
    print("=" * 70)
    print(f"{'ID':<4} | {'Prodotto':<20} | {'Prezzo':>8} | {'Calorie':>8} | {'Tempo (min)':>12}")
    print("-" * 70)
    for id_prodotto, dati in MENU.items():
        nome, prezzo, calorie, tempo = dati
        print(f"{id_prodotto:<4} | {nome:<20} | €{prezzo:>7.2f} | {calorie:>8} | {tempo:>12}")
    print("=" * 70)


def registra_ordine():
    """
    Funzione interattiva per registrare un nuovo ordine
    """
    print("\n🛒 REGISTRAZIONE NUOVO ORDINE")
    print("-" * 40)
    
    ordine = []
    totale = 0
    
    while True:
        try:
            id_prodotto = int(input("\nInserisci ID prodotto (0 per terminare): "))
            
            if id_prodotto == 0:
                break
            
            if id_prodotto not in MENU:
                print("❌ ID prodotto non valido!")
                continue
            
            quantita = int(input("Quantità: "))
            if quantita <= 0:
                print("❌ Quantità non valida!")
                continue
            
            nome = MENU[id_prodotto][0]
            prezzo = MENU[id_prodotto][1]
            subtotale = prezzo * quantita
            
            ordine.append((nome, quantita, prezzo, subtotale))
            totale += subtotale
            
            print(f"✅ Aggiunto: {quantita}x {nome} = €{subtotale:.2f}")
            
        except ValueError:
            print("❌ Input non valido!")
    
    if ordine:
        print("\n" + "=" * 60)
        print("📝 RIEPILOGO ORDINE")
        print("=" * 60)
        for nome, quantita, prezzo, subtotale in ordine:
            print(f"{quantita}x {nome:<25} €{prezzo:>6.2f} = €{subtotale:>7.2f}")
        print("-" * 60)
        print(f"{'TOTALE':<32} = €{totale:>7.2f}")
        print("=" * 60)
    else:
        print("\n❌ Nessun ordine registrato.")


def menu_principale():
    """
    Menu principale dell'applicazione
    """
    while True:
        print("\n" + "=" * 70)
        print("🍔 BURGERPYTHON - SISTEMA GESTIONALE 🍔")
        print("=" * 70)
        print("1. Visualizza Menu")
        print("2. Registra Nuovo Ordine")
        print("3. Analizza Vendite Settimanali")
        print("0. Esci")
        print("=" * 70)
        
        try:
            scelta = input("\nSeleziona un'opzione: ")
            
            if scelta == "1":
                mostra_menu()
            elif scelta == "2":
                mostra_menu()
                registra_ordine()
            elif scelta == "3":
                analizza_vendite()
            elif scelta == "0":
                print("\n👋 Grazie per aver utilizzato BurgerPython!")
                break
            else:
                print("\n❌ Opzione non valida!")
        
        except KeyboardInterrupt:
            print("\n\n👋 Arrivederci!")
            break


# Esecuzione del programma
if __name__ == "__main__":
    # Esegui analisi automatica
    analizza_vendite()
    
    # Avvia menu interattivo
    input("\n\nPremi INVIO per accedere al menu interattivo...")
    menu_principale()