

class Karte:

    def __init__(self,farbe,nummer):
        self.farbe = farbe
        self.nummer = nummer

farben_namen = ["Pik", "Ass", "Herz", "Karo"]
nummern_namen = [None, 'Ass', '2','3','4','5','6','7','8',
                 '9','10','Bube', 'Dame', 'König']


neue_karte_1 = Karte(farben_namen[1], nummern_namen[4])

print(neue_karte_1.farbe)
print(neue_karte_1.nummer)

