import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("#0a0a2e")
screen.tracer(0)

# Create multiple turtles for wave effect
waves = []
for i in range(8):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(3)
    waves.append(t)

colors = ["#00ff88", "#00ddff", "#8844ff", "#ff00aa", "#ffaa00", "#00ffff"]
offset = 0

def draw_aurora():
    global offset
    
    screen.clear()
    screen.bgcolor("#0a0a2e")
    
    for wave_idx, wave in enumerate(waves):
        wave.penup()
        wave.goto(-400, -100 + wave_idx * 30)
        wave.pendown()
        
        # Set color with gradient
        wave.pencolor(colors[wave_idx % len(colors)])
        
        # Draw flowing wave
        for x in range(0, 800, 5):
            # Multiple sine waves for complexity
            y1 = math.sin((x + offset + wave_idx * 50) * 0.01) * 40
            y2 = math.sin((x + offset + wave_idx * 50) * 0.02) * 20
            y3 = math.cos((x + offset) * 0.015) * 15
            
            y = y1 + y2 + y3 - 100 + wave_idx * 30
            
            wave.goto(-400 + x, y)
            
            # Add glowing dots randomly
            if random.random() > 0.97:
                wave.dot(random.randint(3, 8), colors[(wave_idx + 1) % len(colors)])
    
    # Add stars
    for _ in range(3):
        x = random.randint(-400, 400)
        y = random.randint(100, 300)
        star_turtle = turtle.Turtle()
        star_turtle.hideturtle()
        star_turtle.penup()
        star_turtle.goto(x, y)
        star_turtle.dot(3, "#ffffff")
    
    offset += 5
    
    screen.update()
    screen.ontimer(draw_aurora, 50)

draw_aurora()
turtle.done()