import turtle

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(9)

schildi.width(2)

for zahl in range(50):
    #zeige die Zahl aus der Schleife an
    print("zahl:",zahl) 

    schildi.color("MediumSpringGreen")

    #erhoehe nach jeder Ausfuehrung die Vorwartszahl um die zahl in der Schleife
    schildi.forward(15+zahl) 


    schildi.right(140)


