import turtle
import math

turtle.bgcolor("#000000")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

def draw_tunnel():
    colors = ["#ff0080", "#00ffff", "#ffff00", "#00ff80", "#ff00ff", "#80ff00"]
    
    for i in range(360):
        t.pencolor(colors[i % len(colors)])
        t.width(2)
        
        # Create square tunnel effect
        for side in range(4):
            t.forward(300 - i * 0.8)
            t.right(90)
        
        t.right(10)
        
        # Add connecting rays every 10 degrees
        if i % 10 == 0:
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.forward(300 - i * 0.8)
            t.penup()
            t.goto(0, 0)
            t.pendown()

draw_tunnel()
turtle.update()
turtle.done()