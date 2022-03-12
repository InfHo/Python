import rechenmodul
import random

def rechensimulator(z):
    zahl_1 = random.randint(1, z)
    zahl_2 = random.randint(1, z)

    ergebnis = rechenmodul.addition(zahl_1,zahl_2)

    print(zahl_1, "Spanne: 1-"+str(z))
    print(ergebnis)
    if int(input()) == zahl_2:
        print("Richtig!",
              "Correct!",
              "¡Correcto!")
    else: print("Falsch!",
                "Incorrect!",
                "¡Falso!")
    neustart = input("neustarten? (j/n)")
    if neustart == "j":
        z = int(input("neue zahl:"))
        rechensimulator(z)
    else:
        print("ciao!")


def dingsda():
    print("Dingsdafunktion!")

if __name__ == "__main__":
    rechensimulator(3)
