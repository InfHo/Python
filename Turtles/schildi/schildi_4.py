import turtle

schildi = turtle.Turtle()

schildi.shape("turtle")

schildi.speed(2)

schildi.width(2)

# fuehre eine Schleife aus
for zahl in range(5):
    schildi.color("MediumSpringGreen")
    schildi.forward(150)
    schildi.right(70)
