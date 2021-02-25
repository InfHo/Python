import turtle

turtle.colormode(255)

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(0)

schildi.width(2)

# wenn eine Zahl für r,g,b kleiner als 0 oder grösser als 255 ist,
# gibt es einen Error und das Programm stoppt
for zahl in range(1,1000):
    
    # setzte r (mit dem '%'-Zeichen) als den Restwert von (100+zahl)/255
    # dh die Zahl kann nie groesser als 255 werden!
    r = (100 + zahl) % 255
    
    # setzte r (mit dem '%'-Zeichen) als den Restwert von (50 + 2*zahl)/255 
    g = (50 + 2*zahl)%255

    #das ganze geht auch umgekehrt und mit anderen Zahlen:
    b = (70 - zahl*5) % 255
    
    print("zahl=",zahl,"r=",r,"g=",g,"b=",b)
    schildi.color(r,g,b)
    schildi.forward(15+zahl*3)
    schildi.right(140)
