
#jetzt sind alle wichtigen Details im Plan
class Brotbox:
    """ hier kommen dann brotbox details rein """
    def __init__(self, name, material,faecher,volumen,ladetechnik):
        self.name = name
        self.material = material
        self.faecher = faecher
        self.volumen = volumen
        self.ladetechnik = ladetechnik


#und hier können Sie dann eingesetzt werden
multidose = Brotbox("Multivitaminfunktionsdose",
                    "Essbar und gesund",
                    "Extrafächer für Vitamine",
                    "10x40x20",
                    "Solarzellen")

#oder ausgedruckt werden
print(multidose.name)
print(multidose.faecher)
print(multidose.material)
print(multidose.ladetechnik)
print(multidose.volumen)

