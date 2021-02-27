import turtle

turtle.colormode(255)

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(0)

schildi.width(2)

# wenn eine Zahl für r,g,b kleiner als 0 oder grösser als 255 ist,
# gibt es einen Error und das Programm stoppt
for zahl in range(1,1000):
    
    #addiere die zahl aus der Schleife zum Farbwert r
    r = 100 + zahl
    
    #addiere 2*zahl zu g
    g = 50 + 2*zahl

    b = 0
    print("zahl=",zahl,"r=",r,"g=",g,"b=",b)
    schildi.color(r,g,b)
    schildi.forward(15+zahl*3)
    schildi.right(140)
