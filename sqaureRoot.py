import turtle
import math
noah=turtle.Turtle()
turtle.bgcolor('#0d0d2b')
noah.color('red','yellow')
noah.speed(40)

noah.begin_fill()
for i in range(100):
    noah.forward(math.sqrt(i)*10)
    noah.left(170)
noah.end_fill()





turtle.done()
