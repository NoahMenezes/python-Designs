import turtle
import random

turtle.bgcolor("#05050f")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

colors = ["#ff006e", "#fb5607", "#ffbe0b", "#06ffa5", "#3a86ff", "#8338ec"]

def draw_galaxy():
    for i in range(500):
        t.pencolor(random.choice(colors))
        t.width(random.randint(1, 3))
        
        # Random starting position near center
        angle = random.randint(0, 360)
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(random.randint(0, 50))
        t.pendown()
        
        # Draw spiraling arm
        size = random.randint(100, 300)
        spiral_tight = random.uniform(0.5, 2)
        
        for j in range(50):
            t.forward(size / 50)
            t.right(90 / spiral_tight)
            size *= 0.95

draw_galaxy()
turtle.update()
turtle.done()