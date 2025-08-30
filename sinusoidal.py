import turtle
import math

# Background color
turtle.bgcolor("#0d0d2b")  # deep navy-blue aesthetic

noah = turtle.Turtle()
noah.speed(80)
noah.pencolor("cyan")  # glowing color looks better on dark bg

for i in range(2000):
    noah.forward(10)
    noah.left(math.sin(i/10) * 25)
    noah.left(20)

turtle.done()
