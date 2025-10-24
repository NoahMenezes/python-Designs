import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["#ff00ff", "#00ffff", "#ffff00", "#ff0066", "#00ff66", "#6600ff"]
rotation = 0
size_pulse = 0

def draw_vortex():
    global rotation, size_pulse
    
    screen.clear()
    screen.bgcolor("#000000")
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Create pulsing effect
    pulse = math.sin(size_pulse * 0.1) * 50 + 200
    
    for i in range(36):
        t.pencolor(colors[i % len(colors)])
        
        # Draw rotating arms
        t.setheading(rotation + i * 10)
        
        for j in range(30):
            t.forward(pulse / 30)
            t.right(3)
            
            # Add spiral dots
            if j % 5 == 0:
                pos = t.position()
                t.dot(8 - j // 5, colors[(i + j) % len(colors)])
                
        t.penup()
        t.goto(0, 0)
        t.pendown()
    
    # Draw center circle
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.pencolor("#ffffff")
    t.circle(30)
    
    rotation += 3
    size_pulse += 1
    
    screen.update()
    screen.ontimer(draw_vortex, 40)

draw_vortex()
turtle.done()