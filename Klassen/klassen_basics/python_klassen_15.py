class Brotbox:
    """ hier kommen dann brotbox details rein ,
        faecher, volumen, material, ladetechnik"""
    def __init__(self,
                 name,
                 material,
                 faecher,
                 volumen,
                 ladetechnik,
                 spezialfunktion,
                 anzahlfaecher):                        # anzahlfaecher hinzugefuegt
        self.name = name
        self.material = material
        self.faecher = faecher
        self.volumen = volumen
        self.ladetechnik = ladetechnik
        self.spezialfunktion = spezialfunktion
        self.anzahlfaecher = anzahlfaecher                 # anzahlfaecher hinzugefuegt

        # hier jetzt mit allen Details eingefuegt und anzahl faecher dazugemacht mit einer richtigen Zahl
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%d' % (self.name,
                                 self.material,
                                 self.faecher,
                                 self.volumen,
                                 self.ladetechnik,
                                 self.spezialfunktion,
                                 self.anzahlfaecher)

multidose = Brotbox("Multivitaminfunktionsdose",
                    "Essbar und gesund",
                    "Extrafächer für Vitamine",
                    "10x40x20",
                    "Solarzellen",
                    "Kühlbar wenn Batterien dabei",
                    5)                                                # anzahlfaecher hinzugefuegt

campingdose = Brotbox("Die Megadose für Camping",
                      "Nicht essbar",
                      "passt soviel rein wie ein Haus",
                      "80x10x25",
                      "Batterie",
                      "Nur automatische Kühlung",
                      32)                                              # anzahlfaecher hinzugefuegt

brotbox_3001 = Brotbox("Die praktische und äußerst handlich Box für Brot jeder Art",
                       "nicht essbar",
                       "riesig",
                       "20x50x10",
                       "Brennstoffzelle",
                       "Integrierte Aufstrichgläser+GPS",
                       1)                                               # anzahlfaecher hinzugefuegt

print(brotbox_3001)
print(campingdose)
