import turtle
import math
noah=turtle.Turtle()
noah.speed(80)
for i in range(2000):
    noah.forward(10)
    noah.left(math.sin(i/10)*25)
    noah.left(20)

turtle.done()