

class Brotbox:
    """ hier kommen dann brotbox details rein """


multidose = Brotbox()

multidose.name = "Multivitaminfunktionsdose"
multidose.faecher = "Extrafächer für Vitamine"
multidose.material = "Essbar und gesund"

#print(multidose)
print(multidose.name)
print(multidose.faecher)
print(multidose.material)


#jetzt kann  man sich auch noch ein weiteres Produkt mit dem Bauplan basteln,
#aber mit anderen Eigenschaften
campingdose = Brotbox()
campingdose.name = "Die Megadose für Camping"
campingdose.material = "Nicht essbar"
campingdose.faecher = "passt soviel rein wie ein Haus"
campingdose.spezialfunktion = "Kühlbar wenn Batterien dabei"

print(campingdose.name )
print(campingdose.material )
print(campingdose.faecher )
print(campingdose.spezialfunktion )
