import turtle

#wechsle zu RGB Farben (0-255)
turtle.colormode(255)

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(10)

schildi.width(2)

#setze 3 Werte für r,g,b ein 
for zahl in range(1,50):
    r = 120
    g = 50
    b = 80
    #drucke Zahl, r, g, b für jede Zahl aus
    print("zahl=",zahl,"r=",r,"g=",g,"b=",b)
    schildi.color(r,g,b)
    schildi.forward(15+zahl*3)
    schildi.right(140)


