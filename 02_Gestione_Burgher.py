"""
═══════════════════════════════════════════════════════════════════════
ESERCIZIO: Sistema di Gestione FastFood "BurgerPython"
Compito di Realtà con Input Utente e Analisi Statistiche

Studente: ___________________
Data: ___________________
═══════════════════════════════════════════════════════════════════════

CONTESTO:
Sei il responsabile di "BurgerPython", una catena di fast food con 4 punti vendita.
Devi creare un sistema per:
- Registrare ordini dei clienti
- Analizzare vendite e preferenze
- Generare statistiche e report
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════════
# SETUP INIZIALE - NON MODIFICARE
# ═══════════════════════════════════════════════════════════════════════

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

# Dati simulati settimana scorsa: 
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

giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

print("╔" + "═"*68 + "╗")
print("║" + " "*68 + "║")
print("║" + "         🍔 SISTEMA GESTIONE FASTFOOD - BURGERPYTHON 🍔".center(68) + "║")
print("║" + " "*68 + "║")
print("╚" + "═"*68 + "╝")

# ═══════════════════════════════════════════════════════════════════════
# PARTE 1: VISUALIZZAZIONE MENU
# ═══════════════════════════════════════════════════════════════════════

def mostra_menu():
    """Mostra il menu completo del ristorante"""
    print("\n" + "─"*70)
    print("📋 MENU BURGERPYTHON")
    print("─"*70)
    print(f"{'ID':<4} {'PRODOTTO':<25} {'PREZZO':<10} {'CALORIE':<10} {'TEMPO':<8}")
    print("─"*70)
    
    # TODO 1.1: Completa il ciclo per mostrare tutti i prodotti del menu
    # Hint: itera sul dizionario MENU e stampa ogni prodotto formattato
    for id_prodotto, dati in MENU.items():
        nome, prezzo, calorie, tempo = dati
        print(f"{id_prodotto:<4} {nome:<25} €{prezzo:<9.2f} {calorie:<10} {tempo} min")
    
    print("─"*70)

# ═══════════════════════════════════════════════════════════════════════
# PARTE 2: SISTEMA ORDINI CON INPUT UTENTE
# ═══════════════════════════════════════════════════════════════════════

def registra_ordine():
    """Registra un nuovo ordine da un cliente"""
    print("\n🛒 NUOVO ORDINE")
    print("─"*70)
    
    ordine = []
    totale = 0
    calorie_totali = 0
    
    # TODO 2.1: Implementa il ciclo per prendere ordini
    # Il cliente può ordinare più prodotti fino a quando digita 0
    while True:
        try:
            scelta = int(input("\nInserisci ID prodotto (0 per terminare): "))
            
            if scelta == 0:
                break
            
            # TODO 2.2: Verifica che l'ID sia valido
            if scelta not in MENU:
                print("❌ Prodotto non valido!")
                continue
            
            # TODO 2.3: Chiedi la quantità
            quantita = int(input(f"Quantità di {MENU[scelta][0]}: "))
            
            if quantita <= 0:
                print("❌ Quantità non valida!")
                continue
            
            # TODO 2.4: Aggiungi all'ordine e calcola totali
            nome, prezzo, calorie, tempo = MENU[scelta]
            ordine.append([scelta, nome, quantita, prezzo * quantita])
            totale += prezzo * quantita
            calorie_totali += calorie * quantita
            
            print(f"✓ Aggiunto: {quantita}x {nome} = €{prezzo * quantita:.2f}")
            
        except ValueError:
            print("❌ Input non valido! Inserisci un numero.")
    
    # TODO 2.5: Mostra lo scontrino finale
    if ordine:
        print("\n" + "="*70)
        print("🧾 SCONTRINO")
        print("="*70)
        for item in ordine:
            id_prod, nome, qta, subtot = item
            print(f"{qta}x {nome:<30} €{subtot:>8.2f}")
        print("─"*70)
        print(f"{'TOTALE':<35} €{totale:>8.2f}")
        print(f"{'CALORIE TOTALI':<35} {calorie_totali:>8} kcal")
        print("="*70)
        
        return ordine, totale, calorie_totali
    else:
        print("\n⚠️  Ordine vuoto!")
        return None, 0, 0

# ═══════════════════════════════════════════════════════════════════════
# PARTE 3: ANALISI STATISTICHE SETTIMANA PRECEDENTE
# ═══════════════════════════════════════════════════════════════════════

def analisi_vendite_base():
    """Statistiche base sulle vendite della settimana"""
    print("\n" + "="*70)
    print("📊 ANALISI VENDITE SETTIMANA PRECEDENTE")
    print("="*70)
    
    # TODO 3.1: Calcola il totale prodotti venduti nella settimana
    totale_prodotti = np.sum(vendite_settimana)
    print(f"\n📦 Totale prodotti venduti: {totale_prodotti}")
    
    # TODO 3.2: Calcola le vendite per ogni prodotto (somma su giorni e filiali)
    print("\n🏆 CLASSIFICA PRODOTTI PIÙ VENDUTI:")
    vendite_per_prodotto = np.sum(vendite_settimana, axis=(0, 1))
    
    # Crea lista con ID e vendite, poi ordina
    classifica = []
    for i in range(len(vendite_per_prodotto)):
        id_prod = i + 1
        nome = MENU[id_prod][0]
        vendite = vendite_per_prodotto[i]
        classifica.append([nome, vendite])
    
    # Ordina per vendite decrescenti
    classifica.sort(key=lambda x: x[1], reverse=True)
    
    for pos, (nome, vendite) in enumerate(classifica, 1):
        print(f"{pos}. {nome:<25} {vendite:>5} unità")
    
    # TODO 3.3: Calcola gli incassi totali
    print("\n💰 ANALISI INCASSI:")
    incasso_totale = 0
    for i in range(10):
        id_prod = i + 1
        prezzo = MENU[id_prod][1]
        quantita = vendite_per_prodotto[i]
        incasso = prezzo * quantita
        incasso_totale += incasso
    
    print(f"Incasso totale settimana: €{incasso_totale:,.2f}")
    
    # TODO 3.4: Trova il giorno con più vendite
    vendite_per_giorno = np.sum(vendite_settimana, axis=(1, 2))
    giorno_migliore_idx = np.argmax(vendite_per_giorno)
    print(f"\n📅 Giorno con più vendite: {giorni[giorno_migliore_idx]}")
    print(f"   Prodotti venduti: {vendite_per_giorno[giorno_migliore_idx]}")
    
    # TODO 3.5: Trova la filiale con più vendite
    vendite_per_filiale = np.sum(vendite_settimana, axis=(0, 2))
    filiale_migliore_idx = np.argmax(vendite_per_filiale)
    print(f"\n🏪 Filiale con più vendite: {FILIALI[filiale_migliore_idx]}")
    print(f"   Prodotti venduti: {vendite_per_filiale[filiale_migliore_idx]}")

def analisi_avanzata():
    """Analisi statistiche avanzate"""
    print("\n" + "="*70)
    print("🔬 ANALISI AVANZATE")
    print("="*70)
    
    # TODO 3.6: Confronta weekend vs giorni feriali
    print("\n📊 Confronto Feriali vs Weekend:")
    feriali = vendite_settimana[0:5]  # Lun-Ven
    weekend = vendite_settimana[5:7]  # Sab-Dom
    
    media_feriali = np.mean(feriali)
    media_weekend = np.mean(weekend)
    
    print(f"Media vendite giorno feriale: {media_feriali:.1f} prodotti")
    print(f"Media vendite giorno weekend: {media_weekend:.1f} prodotti")
    print(f"Incremento weekend: {((media_weekend/media_feriali - 1) * 100):.1f}%")
    
    # TODO 3.7: Trova le combinazioni prodotto-filiale più vendute
    print("\n🎯 TOP 5 COMBINAZIONI PRODOTTO-FILIALE:")
    # Somma su tutti i giorni per ottenere (filiali, prodotti)
    vendite_filiale_prodotto = np.sum(vendite_settimana, axis=0)
    
    # Trova i 5 valori massimi
    top5_indices = np.argsort(vendite_filiale_prodotto.flatten())[-5:][::-1]
    
    for idx in top5_indices:
        filiale_idx, prodotto_idx = np.unravel_index(idx, vendite_filiale_prodotto.shape)
        vendite = vendite_filiale_prodotto[filiale_idx, prodotto_idx]
        prodotto_nome = MENU[prodotto_idx + 1][0]
        print(f"• {FILIALI[filiale_idx]} - {prodotto_nome}: {vendite} unità")
    
    # TODO 3.8: Analisi trend settimanale hamburger
    print("\n📈 TREND VENDITE HAMBURGER CLASSIC:")
    vendite_hamburger = vendite_settimana[:, :, 0]  # Prodotto ID 1
    trend_giornaliero = np.sum(vendite_hamburger, axis=1)
    
    for i, giorno in enumerate(giorni):
        barra = "█" * int(trend_giornaliero[i] / 10)
        print(f"{giorno:10} {trend_giornaliero[i]:>3} {barra}")

def calcola_performance_filiali():
    """Calcola KPI per ogni filiale"""
    print("\n" + "="*70)
    print("📍 PERFORMANCE PER FILIALE")
    print("="*70)
    
    for i, filiale in enumerate(FILIALI):
        print(f"\n🏪 {filiale}:")
        print("─"*50)
        
        # TODO 3.9: Calcola statistiche per filiale
        vendite_filiale = vendite_settimana[:, i, :]
        
        totale = np.sum(vendite_filiale)
        media_giornaliera = np.mean(vendite_filiale)
        std = np.std(vendite_filiale)
        
        # Calcola incasso
        incasso = 0
        for prod_idx in range(10):
            quantita = np.sum(vendite_filiale[:, prod_idx])
            prezzo = MENU[prod_idx + 1][1]
            incasso += quantita * prezzo
        
        print(f"Totale vendite: {totale} prodotti")
        print(f"Media giornaliera: {media_giornaliera:.1f} prodotti")
        print(f"Deviazione standard: {std:.1f}")
        print(f"Incasso totale: €{incasso:,.2f}")
        
        # Prodotto più venduto in questa filiale
        vendite_per_prod = np.sum(vendite_filiale, axis=0)
        prod_top_idx = np.argmax(vendite_per_prod)
        prod_top_nome = MENU[prod_top_idx + 1][0]
        print(f"Prodotto più venduto: {prod_top_nome} ({vendite_per_prod[prod_top_idx]} unità)")

# ═══════════════════════════════════════════════════════════════════════
# PARTE 4: MENU INTERATTIVO PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════

def menu_principale():
    """Menu principale del sistema"""
    while True:
        print("\n" + "╔" + "═"*68 + "╗")
        print("║" + "  MENU PRINCIPALE".center(68) + "║")
        print("╠" + "═"*68 + "╣")
        print("║  1. 📋 Mostra Menu Prodotti".ljust(69) + "║")
        print("║  2. 🛒 Registra Nuovo Ordine".ljust(69) + "║")
        print("║  3. 📊 Analisi Vendite Base".ljust(69) + "║")
        print("║  4. 🔬 Analisi Avanzate".ljust(69) + "║")
        print("║  5. 📍 Performance Filiali".ljust(69) + "║")
        print("║  6. 🚪 Esci".ljust(69) + "║")
        print("╚" + "═"*68 + "╝")
        
        # TODO 4.1: Implementa la gestione delle scelte del menu
        try:
            scelta = input("\n👉 Seleziona un'opzione: ")
            
            if scelta == "1":
                mostra_menu()
            elif scelta == "2":
                registra_ordine()
            elif scelta == "3":
                analisi_vendite_base()
            elif scelta == "4":
                analisi_avanzata()
            elif scelta == "5":
                calcola_performance_filiali()
            elif scelta == "6":
                print("\n👋 Grazie per aver usato BurgerPython!")
                print("═"*70)
                break
            else:
                print("❌ Opzione non valida!")
        
        except KeyboardInterrupt:
            print("\n\n👋 Arrivederci!")
            break
        except Exception as e:
            print(f"❌ Errore: {e}")

# ═══════════════════════════════════════════════════════════════════════
# ESECUZIONE PROGRAMMA
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    menu_principale()

# ═══════════════════════════════════════════════════════════════════════
# ESERCIZI AGGIUNTIVI (OPZIONALI)
# ═══════════════════════════════════════════════════════════════════════
"""
TODO BONUS 1: Crea una funzione che trova i prodotti "complementari"
              (prodotti spesso ordinati insieme) usando la correlazione

TODO BONUS 2: Implementa un sistema di previsione: quanti hamburger 
              saranno venduti domani? (usa la media mobile)

TODO BONUS 3: Aggiungi un sistema di sconti:
              - 10% su ordini > €20
              - Menu del giorno (hamburger + patatine + bibita) a €10

TODO BONUS 4: Crea un report PDF o CSV esportabile con tutte le statistiche

TODO BONUS 5: Implementa un sistema di "alert": avvisa se un prodotto
              ha vendite molto inferiori alla media (potrebbe esserci un problema)
"""

# ═══════════════════════════════════════════════════════════════════════
# DOMANDE DI RIFLESSIONE
# ═══════════════════════════════════════════════════════════════════════
"""
1. Perché è utile usare un array 3D (giorni, filiali, prodotti) invece 
   di strutture dati separate?

2. Come cambieresti la struttura per tracciare anche l'orario degli ordini?
   (es: mattina, pranzo, sera)

3. Quali altri KPI (Key Performance Indicators) potrebbero essere utili 
   per un manager di fast food?

4. Come implementeresti un sistema di inventario che decrementa automaticamente
   quando vengono registrati gli ordini?

5. Proponi un'estensione: come gestiresti più settimane di dati per 
   analizzare trend mensili o stagionali?
"""