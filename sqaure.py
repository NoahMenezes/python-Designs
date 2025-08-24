import turtle

noah=turtle.Turtle()

noah.color('#cf1342', '#13b2cf')


    
noah.begin_fill()
for i in range(3):
    noah.forward(100)
    noah.left(90)
noah.forward(100)

noah.penup()
noah.forward(150)
noah.pendown()

for i in range(3):
    noah.forward(100)
    noah.left(90)
noah.forward(100)

noah.penup()
noah.forward(150)
noah.pendown()

for i in range(3):
    noah.forward(100)
    noah.left(90)
noah.forward(100)

noah.penup()
noah.forward(150)
noah.pendown()

for i in range(3):
    noah.forward(100)
    noah.left(90)
noah.forward(100)

noah.forward(150)
noah.right(90)
noah.forward(150)
noah.right(90)
noah.forward(150)
noah.right(90)
noah.forward(150)


noah.end_fill()
turtle.done()
