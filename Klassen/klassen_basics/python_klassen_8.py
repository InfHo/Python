
#jetzt auch mit 'spezialfunktion'
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

print("multidose name:", multidose.name)


#dasselbe kann man je´tzt auch mit der Campingdose machen
campingdose = Brotbox("Die Megadose für Camping",
                      "Nicht essbar",
                      "passt soviel rein wie ein Haus",
                      "80x10x25",
                      "Batterie",
                      "Nur automatische Kühlung")



#hier noch eine testdose, die aber zur oben erstelleten
#Multidose führt
testdose = multidose

#der beweis: Selbe adresse im System, es ist dasselbe Objekt
print("testdose name:", testdose.name)
print(multidose)
print(testdose)
