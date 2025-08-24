import turtle

def draw_tree(branch_length, t):
    """
    Recursive function to draw a branch of the tree.
    """
    if branch_length > 5:  # Base case: stop when branches are too short
        # Draw the main branch
        t.forward(branch_length)
        
        # Turn right for the first sub-branch
        t.right(20)
        draw_tree(branch_length - 15, t) # Recursive call for a smaller branch
        
        # Turn left for the second sub-branch
        t.left(40)
        draw_tree(branch_length - 15, t) # Recursive call for a smaller branch
        
        # Go back to the starting point of this branch
        t.right(20)
        t.backward(branch_length)

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.color("green")
t.hideturtle()

# --- Position the turtle to start drawing ---
t.left(90) # Point the turtle upwards
t.penup()
t.backward(150) # Move to the bottom of the screen
t.pendown()

# --- Start drawing the tree ---
draw_tree(100, t)

screen.exitonclick()