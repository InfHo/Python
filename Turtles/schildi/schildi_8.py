import turtle

turtle.colormode(255)

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(10)

schildi.width(2)

for zahl in range(1,100):
    #addiere die zahl aus der Schleife zum Farbwert r
    r = 100 + zahl
    g = 50 
    b = 0
    print("zahl=",zahl,"r=",r,"g=",g,"b=",b)
    schildi.color(r,g,b)
    schildi.forward(15+zahl*3)
    schildi.right(140)
