import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["#ff0080", "#00ffff", "#ffff00", "#ff00ff", "#00ff80", "#8000ff"]
shape_rotation = 0
sides_float = 3.0

def draw_polygon(sides, size, color):
    t.pencolor(color)
    angle = 360 / sides
    
    for _ in range(int(sides)):
        t.forward(size)
        t.right(angle)

def draw_morphing_tunnel():
    global shape_rotation, sides_float
    
    screen.clear()
    screen.bgcolor("#000000")
    
    # Morph between triangle, square, pentagon, hexagon
    sides_float += 0.02
    if sides_float > 8:
        sides_float = 3.0
    
    sides = int(sides_float)
    
    # Draw tunnel layers
    for i in range(30):
        size = 300 - i * 10
        
        if size <= 0:
            break
        
        t.penup()
        t.goto(0, 0)
        t.setheading(shape_rotation + i * 3)
        
        # Position for polygon
        t.forward(size / (2 * math.tan(math.pi / sides)))
        t.right(90 + 180/sides)
        
        t.pendown()
        
        color_idx = i % len(colors)
        draw_polygon(sides, size / sides, colors[color_idx])
        
        # Add connecting lines to center
        if i % 5 == 0:
            pos = t.position()
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.goto(pos)
    
    # Draw orbiting particles
    for i in range(12):
        angle = shape_rotation * 3 + i * 30
        radius = 150 + math.sin(shape_rotation * 0.1 + i) * 50
        
        x = math.cos(math.radians(angle)) * radius
        y = math.sin(math.radians(angle)) * radius
        
        t.penup()
        t.goto(x, y)
        t.dot(10, colors[i % len(colors)])
    
    # Central bright core
    t.penup()
    t.goto(0, 0)
    t.dot(30, "#ffffff")
    t.dot(20, colors[int(shape_rotation / 10) % len(colors)])
    
    shape_rotation += 2
    
    screen.update()
    screen.ontimer(draw_morphing_tunnel, 40)

draw_morphing_tunnel()
turtle.done()