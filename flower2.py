import turtle

noah=turtle.Turtle()

turtle.bgcolor('#0d0d2b')
noah.speed(20)
noah.color('cyan', 'red')
noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
   
noah.end_fill() 
noah.penup()
noah.forward(230)
noah.pendown()

noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
noah.end_fill()
    
noah.right(90)
noah.penup()
noah.forward(230)
noah.pendown()

noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
noah.end_fill()

noah.right(90)
noah.penup()
noah.forward(230)
noah.pendown()

noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
noah.end_fill()

noah.penup()
noah.forward(400)
noah.right(90)
noah.forward(400)
noah.pendown()

noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
noah.end_fill()


noah.penup()
noah.right(90)
noah.forward(200)
noah.pendown()

noah.begin_fill()
for i in range(108):
    noah.forward(200)
    noah.left(170)
noah.end_fill()




turtle.done()