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

# Lista per memorizzare gli ordini della giornata corrente
ordini_giornata = []

# Categorie prodotti per analisi
CATEGORIE = {
    "Hamburger": [1, 2, 3, 4, 5],
    "Contorni": [6, 7],
    "Bevande": [8, 9, 10]
}

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
    tempo_totale = 0
    
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
            ordine.append([scelta, nome, quantita, prezzo * quantita, calorie * quantita, tempo])
            totale += prezzo * quantita
            calorie_totali += calorie * quantita
            tempo_totale = max(tempo_totale, tempo)  # Tempo massimo (preparazione parallela)
            
            print(f"✓ Aggiunto: {quantita}x {nome} = €{prezzo * quantita:.2f}")
            
        except ValueError:
            print("❌ Input non valido! Inserisci un numero.")
    
    # TODO 2.5: Mostra lo scontrino finale
    if ordine:
        print("\n" + "="*70)
        print("🧾 SCONTRINO")
        print("="*70)
        for item in ordine:
            id_prod, nome, qta, subtot, cal, tmp = item
            print(f"{qta}x {nome:<30} €{subtot:>8.2f}")
        print("─"*70)
        print(f"{'TOTALE':<35} €{totale:>8.2f}")
        print(f"{'CALORIE TOTALI':<35} {calorie_totali:>8} kcal")
        print(f"{'TEMPO PREPARAZIONE STIMATO':<35} {tempo_totale:>8} min")
        print("="*70)
        
        # Salva l'ordine nella lista globale
        ordini_giornata.append({
            'ordine': ordine,
            'totale': totale,
            'calorie': calorie_totali,
            'tempo': tempo_totale
        })
        
        # Mostra il resoconto dettagliato
        resoconto_ordine(ordine, totale, calorie_totali)
        
        return ordine, totale, calorie_totali
    else:
        print("\n⚠️  Ordine vuoto!")
        return None, 0, 0

def resoconto_ordine(ordine, totale, calorie_totali):
    """Genera un resoconto dettagliato dell'ordine appena inserito"""
    print("\n" + "="*70)
    print("📊 RESOCONTO DETTAGLIATO ORDINE")
    print("="*70)
    
    # TODO 2.6: Analisi per categoria
    print("\n🏷️  ANALISI PER CATEGORIA:")
    print("─"*70)
    
    categoria_stats = {cat: {'quantita': 0, 'spesa': 0} for cat in CATEGORIE}
    
    for item in ordine:
        id_prod, nome, qta, subtot, cal, tmp = item
        # Trova la categoria del prodotto
        for categoria, prodotti_ids in CATEGORIE.items():
            if id_prod in prodotti_ids:
                categoria_stats[categoria]['quantita'] += qta
                categoria_stats[categoria]['spesa'] += subtot
                break
    
    for categoria, stats in categoria_stats.items():
        if stats['quantita'] > 0:
            print(f"{categoria:15} {stats['quantita']:3} prodotti  €{stats['spesa']:7.2f}")
    
    # TODO 2.7: Confronto con media storica
    print("\n📈 CONFRONTO CON SETTIMANA SCORSA:")
    print("─"*70)
    
    # Calcola la media di spesa per ordine dalla settimana scorsa
    vendite_per_prodotto = np.sum(vendite_settimana, axis=(0, 1))
    incasso_settimana = 0
    for i in range(10):
        prezzo = MENU[i + 1][1]
        quantita = vendite_per_prodotto[i]
        incasso_settimana += prezzo * quantita
    
    # Stima numero ordini (assumendo 3 prodotti per ordine in media)
    num_ordini_stimati = np.sum(vendite_settimana) / 3
    spesa_media_storica = incasso_settimana / num_ordini_stimati
    
    differenza_percentuale = ((totale - spesa_media_storica) / spesa_media_storica) * 100
    
    print(f"Spesa media storica per ordine: €{spesa_media_storica:.2f}")
    print(f"Questo ordine:                  €{totale:.2f}")
    
    if differenza_percentuale > 0:
        print(f"⬆️  Questo ordine è il {differenza_percentuale:.1f}% SUPERIORE alla media")
    else:
        print(f"⬇️  Questo ordine è il {abs(differenza_percentuale):.1f}% INFERIORE alla media")
    
    # TODO 2.8: Indicatori salute
    print("\n💚 INDICATORI SALUTE:")
    print("─"*70)
    
    if calorie_totali < 600:
        livello = "🟢 BASSO"
    elif calorie_totali < 1000:
        livello = "🟡 MEDIO"
    else:
        livello = "🔴 ALTO"
    
    print(f"Apporto calorico: {calorie_totali} kcal - Livello {livello}")
    
    # Calcola percentuale fabbisogno giornaliero (2000 kcal riferimento)
    percentuale_fabbisogno = (calorie_totali / 2000) * 100
    print(f"Percentuale fabbisogno giornaliero: {percentuale_fabbisogno:.1f}%")
    
    # TODO 2.9: Suggerimenti personalizzati
    print("\n💡 SUGGERIMENTI:")
    print("─"*70)
    
    ha_hamburger = any(item[0] in CATEGORIE["Hamburger"] for item in ordine)
    ha_bevanda = any(item[0] in CATEGORIE["Bevande"] for item in ordine)
    ha_contorno = any(item[0] in CATEGORIE["Contorni"] for item in ordine)
    
    if ha_hamburger and not ha_bevanda:
        print("• Che ne dici di una bevanda per completare il pasto?")
    if ha_hamburger and not ha_contorno:
        print("• Le nostre patatine accompagnano perfettamente gli hamburger!")
    if totale < 10:
        print("• Con soli €", f"{(10 - totale):.2f}", "in più potresti avere il Menu del Giorno!")
    if calorie_totali > 1200:
        print("• Ordine molto calorico! Considera le nostre opzioni più leggere.")
    
    print("="*70)

def analisi_ordini_giornata():
    """Analizza tutti gli ordini inseriti manualmente nella giornata corrente"""
    if not ordini_giornata:
        print("\n⚠️  Nessun ordine registrato oggi!")
        return
    
    print("\n" + "="*70)
    print("📋 RESOCONTO ORDINI GIORNATA CORRENTE")
    print("="*70)
    
    # TODO 2.10: Statistiche generali
    print(f"\n📊 STATISTICHE GENERALI:")
    print("─"*70)
    print(f"Numero ordini registrati: {len(ordini_giornata)}")
    
    totale_incassi = sum(ord['totale'] for ord in ordini_giornata)
    totale_calorie = sum(ord['calorie'] for ord in ordini_giornata)
    tempo_medio = np.mean([ord['tempo'] for ord in ordini_giornata])
    
    print(f"Incasso totale:           €{totale_incassi:.2f}")
    print(f"Incasso medio per ordine: €{totale_incassi/len(ordini_giornata):.2f}")
    print(f"Calorie totali servite:   {totale_calorie:,} kcal")
    print(f"Tempo medio preparazione: {tempo_medio:.1f} min")
    
    # TODO 2.11: Prodotti più ordinati oggi
    print(f"\n🏆 PRODOTTI PIÙ ORDINATI OGGI:")
    print("─"*70)
    
    # Conta i prodotti
    conteggio_prodotti = {}
    for ord_data in ordini_giornata:
        for item in ord_data['ordine']:
            id_prod = item[0]
            qta = item[2]
            if id_prod not in conteggio_prodotti:
                conteggio_prodotti[id_prod] = 0
            conteggio_prodotti[id_prod] += qta
    
    # Ordina per quantità
    prodotti_ordinati = sorted(conteggio_prodotti.items(), key=lambda x: x[1], reverse=True)
    
    for i, (id_prod, qta) in enumerate(prodotti_ordinati[:5], 1):
        nome = MENU[id_prod][0]
        print(f"{i}. {nome:<25} {qta} unità")
    
    # TODO 2.12: Distribuzione per fascia di prezzo
    print(f"\n💰 DISTRIBUZIONE ORDINI PER FASCIA DI PREZZO:")
    print("─"*70)
    
    fasce = {
        "Economico (< €10)": 0,
        "Medio (€10-€20)": 0,
        "Alto (> €20)": 0
    }
    
    for ord in ordini_giornata:
        if ord['totale'] < 10:
            fasce["Economico (< €10)"] += 1
        elif ord['totale'] <= 20:
            fasce["Medio (€10-€20)"] += 1
        else:
            fasce["Alto (> €20)"] += 1
    
    for fascia, count in fasce.items():
        percentuale = (count / len(ordini_giornata)) * 100
        barra = "█" * int(percentuale / 5)
        print(f"{fascia:25} {count:2} ordini ({percentuale:5.1f}%) {barra}")
    
    # TODO 2.13: Confronto con storico
    print(f"\n📈 CONFRONTO CON MEDIA SETTIMANALE:")
    print("─"*70)
    
    # Media giornaliera settimana scorsa
    vendite_giornaliere = np.sum(vendite_settimana, axis=(1, 2))
    media_storica = np.mean(vendite_giornaliere)
    prodotti_oggi = sum(sum(item[2] for item in ord['ordine']) for ord in ordini_giornata)
    
    print(f"Prodotti venduti oggi:        {prodotti_oggi}")
    print(f"Media giornaliera storica:    {media_storica:.0f}")
    
    if prodotti_oggi > media_storica:
        print(f"✅ Oggi siamo SOPRA la media di {prodotti_oggi - media_storica:.0f} prodotti!")
    else:
        print(f"⚠️  Oggi siamo SOTTO la media di {media_storica - prodotti_oggi:.0f} prodotti")
    
    # TODO 2.14: Grafico a barre ordini
    print(f"\n📊 TREND ORDINI GIORNATA:")
    print("─"*70)
    
    for i, ord in enumerate(ordini_giornata, 1):
        barra = "█" * int(ord['totale'])
        print(f"Ordine {i:2} €{ord['totale']:6.2f} {barra}")
    
    print("="*70)

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
        print("║  3. 📊 Resoconto Ordini di Oggi".ljust(69) + "║")
        print("║  4. 📈 Analisi Vendite Settimana Scorsa".ljust(69) + "║")
        print("║  5. 🔬 Analisi Avanzate Settimana Scorsa".ljust(69) + "║")
        print("║  6. 📍 Performance Filiali".ljust(69) + "║")
        print("║  7. 🚪 Esci".ljust(69) + "║")
        print("╚" + "═"*68 + "╝")
        
        # TODO 4.1: Implementa la gestione delle scelte del menu
        try:
            scelta = input("\n👉 Seleziona un'opzione: ")
            
            if scelta == "1":
                mostra_menu()
            elif scelta == "2":
                registra_ordine()
            elif scelta == "3":
                analisi_ordini_giornata()
            elif scelta == "4":
                analisi_vendite_base()
            elif scelta == "5":
                analisi_avanzata()
            elif scelta == "6":
                calcola_performance_filiali()
            elif scelta == "7":
                # Mostra riepilogo finale prima di uscire
                if ordini_giornata:
                    print("\n" + "="*70)
                    print("📊 RIEPILOGO FINALE GIORNATA")
                    print("="*70)
                    print(f"Ordini registrati oggi: {len(ordini_giornata)}")
                    totale_giorno = sum(ord['totale'] for ord in ordini_giornata)
                    print(f"Incasso totale: €{totale_giorno:.2f}")
                    print("="*70)
                
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
TODO BONUS 1: Implementa un sistema di sconti automatici:
              - 10% su ordini > €20
              - 15% su ordini > €30
              - Menu del giorno (hamburger + patatine + bibita) a €10

TODO BONUS 2: Crea una funzione che trova i prodotti "complementari"
              (prodotti spesso ordinati insieme) analizzando gli ordini della giornata

TODO BONUS 3: Implementa un sistema di "fidelity card":
              - Ogni €10 spesi = 1 punto
              - 10 punti = 1 hamburger gratis
              - Traccia i punti per ogni cliente (chiedi nome)

TODO BONUS 4: Aggiungi previsione vendite per domani:
              - Usa la media mobile degli ultimi 3 giorni
              - Considera il giorno della settimana (weekend vs feriali)

TODO BONUS 5: Crea un sistema di "alert" che avvisa se:
              - Un prodotto non viene ordinato per 3 giorni consecutivi
              - Le vendite di oggi sono < 50% della media storica
              - Un prodotto ha un picco insolito (> 200% della media)

TODO BONUS 6: Esporta il resoconto giornaliero in formato CSV con:
              - Timestamp ordine, prodotti, quantità, totale, calorie
              - Statistiche aggregate giornaliere

TODO BONUS 7: Implementa un sistema di "suggerimenti intelligenti":
              - Basato su orario (es: "È l'ora del caffè!")
              - Basato su meteo simulato (es: "Giornata calda, bevande fredde?")
              - Basato su vendite precedenti del cliente
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

6. Perché è importante confrontare gli ordini manuali con i dati storici?
   Quali decisioni aziendali potrebbero beneficiare di questa analisi?

7. Come potresti usare i dati degli ordini giornalieri per ottimizzare:
   - La gestione del personale (quanti dipendenti servono?)
   - L'inventario (quante materie prime ordinare?)
   - Il menu (quali prodotti promuovere o rimuovere?)

8. Cosa succederebbe se dovessi gestire migliaia di ordini al giorno?
   Quali problemi di performance potresti incontrare con l'approccio attuale?
"""