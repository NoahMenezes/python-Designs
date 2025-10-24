import turtle
import math

turtle.bgcolor("#1a1a2e")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

def draw_hypnotic():
    colors = ["#e94560", "#0f3460", "#16213e", "#00d9ff", "#ff6bcb"]
    
    for i in range(100):
        t.pencolor(colors[i % len(colors)])
        t.width(2)
        t.circle(200 - i * 2)
        t.right(360 / 100)
        t.forward(5)
        
        # Add inner detail
        if i % 5 == 0:
            pos = t.position()
            heading = t.heading()
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.circle(50 + i)
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

draw_hypnotic()
turtle.update()
turtle.done()