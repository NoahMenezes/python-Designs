import turtle

noah = turtle.Turtle()
noah.getscreen().bgcolor("#994444")
noah.speed(0)   # make drawing faster

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
