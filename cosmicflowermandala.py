import turtle
import math

turtle.bgcolor("#0a0a1a")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

colors = ["#ff006e", "#fb5607", "#ffbe0b", "#8338ec", "#3a86ff", "#06ffa5"]

def draw_petal(size, angle):
    t.circle(size, angle)
    t.left(180 - angle)
    t.circle(size, angle)
    t.left(180 - angle)

for i in range(180):
    t.pencolor(colors[i % len(colors)])
    t.width(2)
    
    # Create spiraling petals
    draw_petal(200 - i, 60)
    
    t.right(360/180 + 1)
    t.forward(i * 0.3)

turtle.update()
turtle.done()