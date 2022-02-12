class Brotbox:
    """ hier kommen dann brotbox details rein ,
        faecher, volumen, material, ladetechnik"""
    def __init__(self,
                 name,
                 material,
                 faecher,
                 volumen,
                 ladetechnik,
                 spezialfunktion):
        self.name = name
        self.material = material
        self.faecher = faecher
        self.volumen = volumen
        self.ladetechnik = ladetechnik
        self.spezialfunktion = spezialfunktion

        # hier passiert folgendes: wir sagen jetzt wir wollen nicht nur den Namen anzeigen, sondern 
        # zum Beispiel auch das Volumen.
        #
        # wenn wir jetzt mehrere Sachen anzeigen lassen wollen, kommen diese in die Klammer rein, durch ein
        # Komma getrennt. Dann gibt es noch den vorderen Teil und das '%' in der Mitte.
        #
        # Im Vorderen Teil muss fuer jede Sache im hinteren Teil ein Zeichen rein. 
        #
        # Das Zeichen haengt noch von der Art der Sache ab, also wenn self.name = "abc" ist, 
        # also string, dann muss vorne ein %s rein. 
    def __str__(self):
        return '%s, %s' % (self.name, self.volumen)

multidose = Brotbox("Multivitaminfunktionsdose",
                    "Essbar und gesund",
                    "Extrafächer für Vitamine",
                    "10x40x20",
                    "Solarzellen",
                    "Kühlbar wenn Batterien dabei")

campingdose = Brotbox("Die Megadose für Camping",
                      "Nicht essbar",
                      "passt soviel rein wie ein Haus",
                      "80x10x25",
                      "Batterie",
                      "Nur automatische Kühlung")

brotbox_3001 = Brotbox("Die praktische und äußerst handlich Box für Brot jeder Art",
                       "nicht essbar",
                       "riesig",
                       "20x50x10",
                       "Brennstoffzelle",
                       "Integrierte Aufstrichgläser+GPS")

print(brotbox_3001)
