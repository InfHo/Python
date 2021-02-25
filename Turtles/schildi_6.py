import turtle

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(10)

schildi.width(2)

for zahl in range(50):
	#fuehre noch eine Schleife aus, mit Farben anstatt Zahlen
    for farbe in ("MediumSpringGreen",
                  "Gold",
                  "SteelBlue",
                  "DeepPink",
                  "Aqua"):
        schildi.color(farbe)
        schildi.forward(15+zahl*3)
        schildi.right(140)
        print("zahl:",zahl)
