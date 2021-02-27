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

# und hier kann man jetzt die Ecke einsetzen, also einen Startpunkt
popcorn.pu()
popcorn.goto(kasten.ecke.x,kasten.ecke.y)
popcorn.pd()

def zeichne_viereck():
    for i in range(2):
        popcorn.forward(kasten.hoehe)
        popcorn.right(90)
        popcorn.forward(kasten.laenge)
        popcorn.right(90)


zeichne_viereck()

