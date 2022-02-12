

#man kann es sich auch einfacher machen und spezielle Eigenarten die sowieso jede Brotbox
#hat, gleich in den Bauplan einfliessen lassen
class Brotbox:
    """ hier kommen dann brotbox details rein """
    def __init__(self, name, material): #hier werden Details festgelegt, mit der die Brotboxen geplant werden sollen
        self.name = name
        self.material = material
        

#jetzt kann man die Eigenschaften schon eingeben wenn man seine spezielle Box erstellt
multidose = Brotbox("Multivitaminfunktionsdose", "Essbar und gesund")

print(multidose.name)
print(multidose.material)


campingdose = Brotbox("Die Megadose für Camping", "Nicht essbar")
print(campingdose.name)
print(campingdose.material)
