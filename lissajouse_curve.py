import turtle, math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("lime")

A, B = 200, 200
a, b = 3, 2    # frequencies
delta = math.pi / 2

for i in range(2000):
    t_x = A * math.sin(a * i * 0.01 + delta)
    t_y = B * math.sin(b * i * 0.01)
    t.goto(t_x, t_y)

turtle.done()
