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
        # %d fuer Zahlen (int)
        # %f fuer Kommazahlen (float)
    def __str__(self):
        return '%s, %d %f' % (self.name, self.material, self.faecher)

testdose = Brotbox("Multivitaminfunktionsdose",
                   5,
                   4.2,
                    "10x40x20",
                    "Solarzellen",
                    "Kühlbar wenn Batterien dabei")


print(testdose)
