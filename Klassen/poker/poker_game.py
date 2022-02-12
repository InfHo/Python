
# definiere Kartenklasse
class Karte:

    # erstelle Liste mit Farben und Nummern
    farben_namen = ["Pik", "Kreuz", "Herz", "Karo"]
    nummern_namen = [None, 'Ass', '2','3','4','5','6','7','8',
                     '9','10','Bube', 'Dame', 'König']

    # initialisiere karten
    def __init__(self,farbe,nummer):
        self.farbe = farbe
        self.nummer = nummer

    # printe die karten
    def __str__(self):
        return f'{Karte.farben_namen[self.farbe]}-{Karte.nummern_namen[self.nummer]}'


# erstelle zwei Karten
neue_karte_1 = Karte(1,3)
neue_karte_2 = Karte(3,13)


# printe die Karten
print(neue_karte_1)
print(neue_karte_2)


class Stapel:

    def __init__(self):
        self.karten = list()
        for farbe in range(4):
            for nummer in range(1,14):
                self.karten.append(Karte(farbe, nummer))

    def __str__(self):
        kv=str()
        for i in self.karten:
            kv+=str(i)
            kv+="\n"
        return kv

    
stapel = Stapel()

print(stapel)
        

















        
