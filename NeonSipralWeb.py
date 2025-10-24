import turtle
import math

turtle.bgcolor("#000000")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

def draw_spiral_web():
    colors = ["#ff00ff", "#00ffff", "#ffff00", "#00ff00", "#ff0066", "#6600ff"]
    
    for j in range(6):
        t.pencolor(colors[j])
        t.width(2)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(60)
        
        for i in range(200):
            t.forward(i * 0.5)
            t.right(59)
            
            if i % 10 == 0:
                # Add connecting lines
                pos = t.position()
                heading = t.heading()
                t.penup()
                t.goto(0, 0)
                t.pendown()
                t.goto(pos)
                t.penup()
                t.goto(pos)
                t.setheading(heading)
                t.pendown()

draw_spiral_web()
turtle.update()
turtle.done()