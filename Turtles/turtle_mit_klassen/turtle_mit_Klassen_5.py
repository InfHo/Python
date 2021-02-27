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

# und noch in eine Funktion gepackt. mehr dazu auch auf 
# https://github.com/InfHo/Ferienkurse/tree/master/Winterferien2021/Python_Kurs_1/turtle_tim
def zeichne_viereck():
    for i in range(2):
        popcorn.forward(kasten.hoehe)
        popcorn.right(90)
        popcorn.forward(kasten.laenge)
        popcorn.right(90)


zeichne_viereck()

