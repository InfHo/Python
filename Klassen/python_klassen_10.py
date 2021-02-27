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

multidose = Brotbox("Multivitaminfunktionsdose",
                    "Essbar und gesund",
                    "Extrafächer für Vitamine",
                    "10x40x20",
                    "Solarzellen",
                    "Kühlbar wenn Batterien dabei")

#print("multidose name:", multidose.name)

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

# und zeigen jetzt wie die Boxen alle aussehen
print("-----")
print("Name:", brotbox_3001.name)
print("Material:",brotbox_3001.material)
print("Vol:",brotbox_3001.volumen)
print("Ladetechnik",brotbox_3001.ladetechnik)
print("Extras:",brotbox_3001.spezialfunktion)
print("-----")

print("Name:", campingdose.name)
print("Material:",campingdose.material)
print("Vol:",campingdose.volumen)
print("Ladetechnik",campingdose.ladetechnik)
print("Extras:",campingdose.spezialfunktion)
print("-----")

print("Name:", multidose.name)
print("Material:",multidose.material)
print("Vol:",multidose.volumen)
print("Ladetechnik",multidose.ladetechnik)
print("Extras:",multidose.spezialfunktion)
print("-----")











                       
                       
