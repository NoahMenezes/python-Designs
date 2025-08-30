import turtle
import math
noah=turtle.Turtle()
turtle.bgcolor('#0d0d2b')
noah.pencolor('cyan')
noah.speed(60)
for i in range(2200):
    noah.forward(math.sqrt(i))
    noah.left(i%180)
    
turtle.done()