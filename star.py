import turtle
turtle.bgcolor("#0d0d2b")
noah = turtle.Turtle()
noah.speed(0)   # make drawing faster
noah.pencolor("cyan")
def star(noah, size):
    if size <= 20:   # base case
        return
    else:
        for i in range(5):
            noah.forward(size)
            star(noah, size/2.2)   # pass the same turtle object
            noah.left(216)

star(noah, 300)

turtle.done()
