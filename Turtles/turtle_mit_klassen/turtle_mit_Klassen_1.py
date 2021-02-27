
# wir erstellen uns einen Plan fuer einen Punkt im Raum
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

# und hier sagen wir ein Viereck hat 2 Seiten und einen Anfagspunkt (ecke)
class Viereck:
    """hoehe, weite, punkt"""
    def __init__(self, laenge, hoehe, ecke):
        self.laenge = laenge
        self.hoehe = hoehe
        self.ecke = ecke

# hier erstellen wir einen Punkt und nennen ihn ecke_1
ecke_1 = Punkt(0,0)
# und printen ihn zum test
print(ecke_1.x, ecke_1.y)

# und hier erstellen wir ein Objekt nach dem Viereckplan und nennen es 'kasten'
kasten = Viereck(7,3,ecke_1)
print(kasten.hoehe)
