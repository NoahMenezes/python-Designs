import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#0d0d20")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["#ff006e", "#fb5607", "#ffbe0b", "#8338ec", "#3a86ff", "#06ffa5"]
breath = 0
rotation = 0

def draw_petal(size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    
    t.end_fill()

def draw_mandala():
    global breath, rotation
    
    screen.clear()
    screen.bgcolor("#0d0d20")
    
    # Breathing effect
    pulse = math.sin(breath * 0.05) * 30 + 100
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Draw layers
    for layer in range(3):
        layer_size = pulse + layer * 40
        
        for i in range(12):
            t.penup()
            t.goto(0, 0)
            t.setheading(rotation + i * 30 + layer * 10)
            t.forward(layer_size)
            
            angle = t.heading()
            t.pendown()
            
            # Draw petals
            color_idx = (i + layer) % len(colors)
            draw_petal(40 - layer * 5, colors[color_idx])
            
            # Add decorative circles
            t.penup()
            t.goto(0, 0)
            t.setheading(rotation + i * 30 + layer * 10)
            t.forward(layer_size + 30)
            t.pendown()
            t.dot(8, colors[(color_idx + 1) % len(colors)])
    
    # Central glowing core
    for i in range(5):
        t.penup()
        t.goto(0, -(20 - i * 4))
        t.pendown()
        t.pencolor(colors[i % len(colors)])
        t.circle(20 - i * 4)
    
    # Rotating particles around
    for i in range(36):
        angle_rad = math.radians(rotation * 2 + i * 10)
        x = math.cos(angle_rad) * (pulse + 80)
        y = math.sin(angle_rad) * (pulse + 80)
        
        t.penup()
        t.goto(x, y)
        size = abs(math.sin(breath * 0.05 + i * 0.2)) * 8 + 3
        t.dot(int(size), colors[i % len(colors)])
    
    breath += 1
    rotation += 1
    
    screen.update()
    screen.ontimer(draw_mandala, 40)

draw_mandala()
turtle.done()