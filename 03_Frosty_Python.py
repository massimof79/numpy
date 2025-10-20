"""
═══════════════════════════════════════════════════════════════════════
ESERCIZIO: Sistema di Gestione Gelateria "FrostyPython"
Compito di Realtà - Livello Base/Intermedio

Studente: ___________________
Data: ___________________
═══════════════════════════════════════════════════════════════════════

CONTESTO:
Sei il proprietario di "FrostyPython", una gelateria artigianale.
Devi creare un sistema per:
- Registrare vendite di gelati
- Analizzare i gusti più venduti
- Calcolare incassi e statistiche
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════════
# SETUP INIZIALE - NON MODIFICARE
# ═══════════════════════════════════════════════════════════════════════

# Menu gelati: [Nome, Prezzo€ al gusto, Calorie per gusto]
GUSTI = {
    1: ["Cioccolato", 2.00, 180],
    2: ["Vaniglia", 2.00, 150],
    3: ["Fragola", 2.00, 140],
    4: ["Pistacchio", 2.50, 200],
    5: ["Stracciatella", 2.00, 190],
    6: ["Limone", 1.80, 120],
    7: ["Nocciola", 2.50, 210],
    8: ["Menta", 1.80, 130]
}

# Dimensioni coppette/coni
DIMENSIONI = {
    "Piccolo": 1,    # 1 gusto
    "Medio": 2,      # 2 gusti
    "Grande": 3      # 3 gusti
}

# Dati settimana scorsa (5 giorni lavorativi)
# Shape: (5 giorni, 8 gusti) = numero di gusti venduti
np.random.seed(100)
vendite_settimana = np.array([
    # Lun  Mar  Mer  Gio  Ven
    [45, 38, 32, 28, 55, 25, 42, 20],  # Lunedì
    [48, 40, 35, 30, 58, 27, 45, 22],  # Martedì
    [52, 43, 38, 33, 62, 30, 48, 25],  # Mercoledì
    [55, 46, 40, 35, 65, 32, 50, 27],  # Giovedì
    [70, 60, 52, 48, 85, 42, 65, 35]   # Venerdì
])

giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì']

# Lista per memorizzare le vendite di oggi
vendite_oggi = []

print("╔" + "═"*68 + "╗")
print("║" + "🍦 SISTEMA GESTIONE GELATERIA - FROSTYPYTHON 🍦".center(68) + "║")
print("╚" + "═"*68 + "╝")

# ═══════════════════════════════════════════════════════════════════════
# PARTE 1: VISUALIZZAZIONE MENU
# ═══════════════════════════════════════════════════════════════════════

def mostra_menu():
    """Mostra il menu dei gusti disponibili"""
    print("\n" + "─"*60)
    print("🍨 MENU GUSTI DISPONIBILI")
    print("─"*60)
    print(f"{'ID':<4} {'GUSTO':<20} {'PREZZO':<10} {'CALORIE':<10}")
    print("─"*60)
    
    # TODO 1.1: Completa il ciclo per mostrare tutti i gusti
    for id_gusto, dati in GUSTI.items():
        nome, prezzo, calorie = dati
        print(f"{id_gusto:<4} {nome:<20} €{prezzo:<9.2f} {calorie} kcal")
    
    print("─"*60)
    print("\n📏 DIMENSIONI:")
    print("   • Piccolo (1 gusto)  = prezzo base")
    print("   • Medio   (2 gusti)  = prezzo base x 2")
    print("   • Grande  (3 gusti)  = prezzo base x 3")

# ═══════════════════════════════════════════════════════════════════════
# PARTE 2: REGISTRAZIONE VENDITE
# ═══════════════════════════════════════════════════════════════════════

def registra_vendita():
    """Registra una nuova vendita di gelato"""
    print("\n" + "═"*60)
    print("🛒 NUOVA VENDITA")
    print("═"*60)
    
    # TODO 2.1: Chiedi la dimensione
    print("\nScegli la dimensione:")
    print("1. Piccolo (1 gusto)")
    print("2. Medio (2 gusti)")
    print("3. Grande (3 gusti)")
    
    try:
        dim_scelta = int(input("\nDimensione (1-3): "))
        
        if dim_scelta == 1:
            dimensione = "Piccolo"
            num_gusti = 1
        elif dim_scelta == 2:
            dimensione = "Medio"
            num_gusti = 2
        elif dim_scelta == 3:
            dimensione = "Grande"
            num_gusti = 3
        else:
            print("❌ Dimensione non valida!")
            return
        
        print(f"\n✓ Dimensione: {dimensione} ({num_gusti} gusti)")
        
        # TODO 2.2: Scegli i gusti
        gusti_scelti = []
        totale = 0
        calorie_totali = 0
        
        for i in range(num_gusti):
            print(f"\n--- Gusto {i+1}/{num_gusti} ---")
            id_gusto = int(input("ID gusto: "))
            
            # TODO 2.3: Verifica che il gusto sia valido
            if id_gusto not in GUSTI:
                print("❌ Gusto non valido!")
                return
            
            nome, prezzo, calorie = GUSTI[id_gusto]
            gusti_scelti.append([id_gusto, nome, prezzo])
            totale += prezzo
            calorie_totali += calorie
            
            print(f"✓ Aggiunto: {nome} (€{prezzo:.2f})")
        
        # TODO 2.4: Mostra il riepilogo
        print("\n" + "═"*60)
        print("🧾 RIEPILOGO VENDITA")
        print("═"*60)
        print(f"Dimensione: {dimensione}")
        print(f"\nGusti selezionati:")
        for gusto in gusti_scelti:
            print(f"  • {gusto[1]:<20} €{gusto[2]:.2f}")
        print("─"*60)
        print(f"{'TOTALE':<25} €{totale:.2f}")
        print(f"{'CALORIE TOTALI':<25} {calorie_totali} kcal")
        print("═"*60)
        
        # TODO 2.5: Salva la vendita
        vendite_oggi.append({
            'dimensione': dimensione,
            'num_gusti': num_gusti,
            'gusti': gusti_scelti,
            'totale': totale,
            'calorie': calorie_totali
        })
        
        print("\n✅ Vendita registrata con successo!")
        
        # Mostra suggerimento
        if calorie_totali > 500:
            print("💡 Suggerimento: Proponi una passeggiata al cliente! 🚶")
        
    except ValueError:
        print("❌ Input non valido!")

# ═══════════════════════════════════════════════════════════════════════
# PARTE 3: RESOCONTO VENDITE ODIERNE
# ═══════════════════════════════════════════════════════════════════════

def resoconto_oggi():
    """Mostra il resoconto delle vendite di oggi"""
    
    if not vendite_oggi:
        print("\n⚠️  Nessuna vendita registrata oggi!")
        return
    
    print("\n" + "═"*60)
    print("📊 RESOCONTO VENDITE DI OGGI")
    print("═"*60)
    
    # TODO 3.1: Calcola statistiche base
    num_vendite = len(vendite_oggi)
    incasso_totale = sum(v['totale'] for v in vendite_oggi)
    incasso_medio = incasso_totale / num_vendite
    
    print(f"\n📦 Vendite totali: {num_vendite}")
    print(f"💰 Incasso totale: €{incasso_totale:.2f}")
    print(f"📊 Incasso medio per vendita: €{incasso_medio:.2f}")
    
    # TODO 3.2: Conta i gusti venduti
    print("\n🏆 GUSTI PIÙ VENDUTI OGGI:")
    print("─"*60)
    
    conteggio_gusti = {}
    for vendita in vendite_oggi:
        for gusto_info in vendita['gusti']:
            id_gusto = gusto_info[0]
            if id_gusto not in conteggio_gusti:
                conteggio_gusti[id_gusto] = 0
            conteggio_gusti[id_gusto] += 1
    
    # Ordina per quantità
    gusti_ordinati = sorted(conteggio_gusti.items(), key=lambda x: x[1], reverse=True)
    
    for i, (id_gusto, quantita) in enumerate(gusti_ordinati, 1):
        nome = GUSTI[id_gusto][0]
        barra = "█" * quantita
        print(f"{i}. {nome:<20} {quantita:3} {barra}")
    
    # TODO 3.3: Distribuzione dimensioni
    print("\n📏 DISTRIBUZIONE PER DIMENSIONE:")
    print("─"*60)
    
    dim_count = {"Piccolo": 0, "Medio": 0, "Grande": 0}
    for vendita in vendite_oggi:
        dim_count[vendita['dimensione']] += 1
    
    for dim, count in dim_count.items():
        if num_vendite > 0:
            percentuale = (count / num_vendite) * 100
            barra = "█" * int(percentuale / 5)
            print(f"{dim:<10} {count:2} vendite ({percentuale:5.1f}%) {barra}")
    
    # TODO 3.4: Confronto con la settimana scorsa
    print("\n📈 CONFRONTO CON MEDIA SETTIMANALE:")
    print("─"*60)
    
    # Calcola numero medio di gusti venduti al giorno la settimana scorsa
    gusti_per_giorno = np.sum(vendite_settimana, axis=1)
    media_storica = np.mean(gusti_per_giorno)
    
    # Conta gusti venduti oggi
    gusti_oggi = sum(v['num_gusti'] for v in vendite_oggi)
    
    print(f"Gusti venduti oggi:        {gusti_oggi}")
    print(f"Media giornaliera storica: {media_storica:.0f}")
    
    if gusti_oggi > media_storica:
        print(f"✅ Oggi siamo SOPRA la media! (+{gusti_oggi - media_storica:.0f})")
    else:
        print(f"⚠️  Oggi siamo sotto la media (-{media_storica - gusti_oggi:.0f})")
    
    print("═"*60)

# ═══════════════════════════════════════════════════════════════════════
# PARTE 4: ANALISI SETTIMANA SCORSA
# ═══════════════════════════════════════════════════════════════════════

def analisi_settimana():
    """Analizza i dati della settimana scorsa"""
    print("\n" + "═"*60)
    print("📊 ANALISI SETTIMANA SCORSA")
    print("═"*60)
    
    # TODO 4.1: Totale gusti venduti
    totale_gusti = np.sum(vendite_settimana)
    print(f"\n🍨 Totale gusti venduti: {totale_gusti}")
    
    # TODO 4.2: Classifica gusti più venduti
    print("\n🏆 CLASSIFICA GUSTI SETTIMANA:")
    print("─"*60)
    
    vendite_per_gusto = np.sum(vendite_settimana, axis=0)
    
    # Crea lista con nome e vendite, poi ordina
    classifica = []
    for i in range(len(vendite_per_gusto)):
        id_gusto = i + 1
        nome = GUSTI[id_gusto][0]
        vendite = vendite_per_gusto[i]
        classifica.append([nome, vendite])
    
    classifica.sort(key=lambda x: x[1], reverse=True)
    
    for pos, (nome, vendite) in enumerate(classifica, 1):
        medaglia = "🥇" if pos == 1 else "🥈" if pos == 2 else "🥉" if pos == 3 else "  "
        print(f"{medaglia} {pos}. {nome:<20} {vendite:>4} gusti")
    
    # TODO 4.3: Incasso totale stimato
    print("\n💰 INCASSO SETTIMANALE STIMATO:")
    print("─"*60)
    
    incasso_totale = 0
    for i in range(8):
        id_gusto = i + 1
        prezzo = GUSTI[id_gusto][1]
        quantita = vendite_per_gusto[i]
        incasso = prezzo * quantita
        incasso_totale += incasso
    
    print(f"Incasso totale: €{incasso_totale:,.2f}")
    print(f"Incasso medio giornaliero: €{incasso_totale/5:,.2f}")
    
    # TODO 4.4: Giorno migliore
    print("\n📅 ANALISI PER GIORNO:")
    print("─"*60)
    
    vendite_per_giorno = np.sum(vendite_settimana, axis=1)
    
    for i, giorno in enumerate(giorni):
        gusti = vendite_per_giorno[i]
        barra = "█" * int(gusti / 5)
        print(f"{giorno:10} {gusti:>3} gusti {barra}")
    
    giorno_top = np.argmax(vendite_per_giorno)
    print(f"\n🌟 Giorno migliore: {giorni[giorno_top]} ({vendite_per_giorno[giorno_top]} gusti)")
    
    # TODO 4.5: Trend crescita
    print("\n📈 TREND SETTIMANALE:")
    print("─"*60)
    
    crescita = vendite_per_giorno[-1] - vendite_per_giorno[0]
    percentuale = (crescita / vendite_per_giorno[0]) * 100
    
    print(f"Vendite Lunedì:  {vendite_per_giorno[0]} gusti")
    print(f"Vendite Venerdì: {vendite_per_giorno[-1]} gusti")
    print(f"Crescita: {crescita} gusti ({percentuale:+.1f}%)")
    
    if crescita > 0:
        print("✅ Trend POSITIVO! Le vendite sono aumentate durante la settimana")
    else:
        print("⚠️  Trend negativo, le vendite sono diminuite")
    
    print("═"*60)

# ═══════════════════════════════════════════════════════════════════════
# PARTE 5: MENU PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════

def menu_principale():
    """Menu principale del sistema"""
    while True:
        print("\n" + "╔" + "═"*58 + "╗")
        print("║" + "  MENU PRINCIPALE".center(58) + "║")
        print("╠" + "═"*58 + "╣")
        print("║  1. 🍨 Mostra Menu Gusti".ljust(59) + "║")
        print("║  2. 🛒 Registra Vendita".ljust(59) + "║")
        print("║  3. 📊 Resoconto Vendite di Oggi".ljust(59) + "║")
        print("║  4. 📈 Analisi Settimana Scorsa".ljust(59) + "║")
        print("║  5. 🚪 Esci".ljust(59) + "║")
        print("╚" + "═"*58 + "╝")
        
        try:
            scelta = input("\n👉 Seleziona un'opzione: ")
            
            if scelta == "1":
                mostra_menu()
            elif scelta == "2":
                registra_vendita()
            elif scelta == "3":
                resoconto_oggi()
            elif scelta == "4":
                analisi_settimana()
            elif scelta == "5":
                # Riepilogo finale
                if vendite_oggi:
                    print("\n" + "═"*60)
                    print("📊 RIEPILOGO FINALE GIORNATA")
                    print("═"*60)
                    print(f"🍦 Vendite registrate: {len(vendite_oggi)}")
                    totale = sum(v['totale'] for v in vendite_oggi)
                    print(f"💰 Incasso totale: €{totale:.2f}")
                    print("═"*60)
                
                print("\n🍨 Grazie per aver usato FrostyPython!")
                print("   A presto! 👋")
                print("═"*60)
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
# ESERCIZI BONUS (OPZIONALI)
# ═══════════════════════════════════════════════════════════════════════
"""
TODO BONUS 1: Aggiungi i "topping" extra (panna, cioccolato, noccioline)
              con costo aggiuntivo di €0.50 cadauno

TODO BONUS 2: Implementa un sistema di sconti:
              - 10% per clienti con più di 5 gelati acquistati
              - "Happy Hour" dalle 15:00 alle 17:00 con sconto 20%

TODO BONUS 3: Crea una funzione che suggerisce abbinamenti di gusti
              basandosi su quali gusti vengono spesso scelti insieme

TODO BONUS 4: Aggiungi la gestione della temperatura:
              - Se fa molto caldo (>30°C), mostra un alert: "Giornata calda!"
              - Prevedi più vendite nei giorni caldi

TODO BONUS 5: Implementa un sistema di "fidelity card":
              - Ogni 10 gusti = 1 gelato gratis
              - Traccia i punti per cliente (chiedi nome)
"""

# ═══════════════════════════════════════════════════════════════════════
# DOMANDE DI RIFLESSIONE
# ═══════════════════════════════════════════════════════════════════════
"""
1. Perché è utile usare un array 2D (giorni x gusti) per memorizzare
   le vendite della settimana?

2. Come cambieresti la struttura dati se dovessi gestire anche
   vendite di pomeriggio e sera separatamente?

3. Quali altre statistiche potrebbero essere utili per il proprietario
   della gelateria?

4. Come potresti usare questi dati per decidere quali gusti preparare
   ogni giorno? (per evitare sprechi)

5. Se dovessi aggiungere altre gelaterie in città, come organizzeresti
   i dati per confrontare le performance?

6. Perché è importante confrontare le vendite di oggi con la media
   della settimana scorsa?
"""