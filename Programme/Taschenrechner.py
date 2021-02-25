# Aus dem Python 3 Kurs der Initiative für Hochbegabung e.V. 
# infho.eu

# erstelle Funktion Taschenrechner mit Addition
def taschenrechner_plu():
    # antwort und antwort2 ist das was als input eingegeben wird
    antwort = input("Erste Zahl: ")
    antwort2 = input("Zweite Zahl: ")
    f = int(antwort)
    g = int(antwort2)
    print(f+g)

# erstelle Funktion Taschenrechner mit Subtraktion
def taschenrechner_min():
    antwort = input("Erste Zahl: ")
    antwort2 = input("Zweite Zahl: ")
    f = int(antwort)
    g = int(antwort2)
    print(f-g)

# erstelle Funktion Taschenrechner mit Multiplikation
def taschenrechner_mal():
    antwort = input("Erste Zahl: ")
    antwort2 = input("Zweite Zahl: ")
    f = int(antwort)
    g = int(antwort2)
    print(f*g)

# erstelle Funktion Taschenrechner mit Division
def taschenrechner_geteilt():
    antwort = input("Erste Zahl: ")
    antwort2 = input("Zweite Zahl: ")
    f = int(antwort)
    g = int(antwort2)
    print(f/g)

# Bringe alle Funktionen in eine Taschenrechnerfunktion
def taschenrechner_komplett():
    # antwort3 ist das was als input eingegeben wird
    # lower() setzt antwort3 auf Kleinbuchstaben
    antwort3 = input("Welchen Rechner ('plus', 'mal', 'minus', 'geteilt'): ").lower() 

    if antwort3 == "plus": # wenn man Plus eintippt soll er addieren
        taschenrechner_plu()

    elif antwort3 == "mal"  "multipliziere": # wenn man 'mal eingibt multpliziere..'
        taschenrechner_mal()   

    elif antwort3 == "minus": # ...subtrahiere
        taschenrechner_min()

    elif antwort3 == "geteilt": # ..dividiere
        taschenrechner_geteilt() 

    else: # else soll immer nur ganz ans Ende und heisst soviel wie 'Oder sonst' 
        print("diesen Rechner gibt es nicht. Versuche erneut.")
        taschenrechner_komplett() #starte die Taschenrechnerfunktion erneut
    
taschenrechner_komplett() #führe den Taschenrechner aus
