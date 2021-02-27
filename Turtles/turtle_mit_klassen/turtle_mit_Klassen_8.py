import turtle

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Viereck:
    """hoehe, weite, punkt"""
    def __init__(self, laenge, hoehe, ecke):
        self.laenge = laenge
        self.hoehe = hoehe
        self.ecke = ecke

ecke_1 = Punkt(55,-100)
print(ecke_1.x, ecke_1.y)

kasten = Viereck(70,30,ecke_1)
print(kasten.hoehe)

popcorn = turtle.Turtle()

# und den Startpunkt noch in die Funktion eingesetzt
def zeichne_viereck():
    popcorn.pu()
    popcorn.goto(kasten.ecke.x,kasten.ecke.y)
    popcorn.pd()
    for i in range(2):
        popcorn.forward(kasten.hoehe)
        popcorn.right(90)
        popcorn.forward(kasten.laenge)
        popcorn.right(90)


zeichne_viereck()

# wir koennen jetzt eine Objekt das wir mit einer Klasse erstellt haben
# in die turtle-Zeichnung einsetzen. Mehr dazu im naechsten Kurs. 