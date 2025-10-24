import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.tracer(0)

# Create multiple turtles for complex patterns
turtles = []
colors = ["#ff006e", "#fb5607", "#ffbe0b", "#8338ec", "#3a86ff", "#06ffa5"]

for i in range(6):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    t.pencolor(colors[i])
    t.penup()
    t.goto(0, 0)
    t.pendown()
    turtles.append(t)

angle = 0
radius = 0

def draw_frame():
    global angle, radius
    
    screen.clear()
    screen.bgcolor("#0a0a1a")
    
    for i, t in enumerate(turtles):
        t.clear()
        t.penup()
        t.goto(0, 0)
        t.setheading(angle + i * 60)
        t.pendown()
        
        # Draw beautiful spiraling patterns
        for j in range(100):
            t.forward(2)
            t.left(2)
            
            # Pulsing effect
            pulse = math.sin(angle * 0.05 + j * 0.1) * 30
            
            # Draw petals at intervals
            if j % 10 == 0:
                pos = t.position()
                heading = t.heading()
                
                # Draw a petal
                for _ in range(2):
                    t.circle(20 + pulse, 60)
                    t.left(120)
                
                t.penup()
                t.goto(pos)
                t.setheading(heading)
                t.pendown()
    
    angle += 2
    radius = (radius + 0.5) % 200
    
    screen.update()
    screen.ontimer(draw_frame, 30)

draw_frame()
turtle.done()