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

        # __str__ bedeutet, dass wenn wir ein Objekt mit dem Brotbox-Plan erstellen
        # ( also zB  multidose=Brotbox(...) ) und dieses Objekt 'multidose' dann in print() reinstecken,
        # wird das was hier nach return kommt angezeigt.  
        #
        # 'self' bedeutet dass wir alle objekte benutzen können,
        # also nicht nur multidose, sondern auch campingdose, brotbox_3001 oder was auch immer wir erstellt haben.
        #
        # Also bedeutet print(multidose) hier soviel
        # wie print(self.name) und da 'self' hier 'multidose' ist steht dort eigentlich
        # print(multidose.name)
    def __str__(self):
        return self.name

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

print(multidose)
print(multidose.name)