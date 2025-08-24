import turtle, math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("magenta")

a = 200
k = 5   # try changing 3, 4, 7...

for angle in range(0, 360 * 5):  # more turns for a full flower
    r = a * math.cos(math.radians(k * angle))
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    t.goto(x, y)

turtle.done()
