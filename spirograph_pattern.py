import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.bgcolor("#0d001a") # A dark purple background

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# --- Define a list of colors ---
colors = ["#ff0055", "#ff4d88", "#f2acff", "#a33bff", "#5200cc"]

# --- The Drawing Loop ---
# Draw 60 circles to create the pattern
for i in range(60):
    # Set the color, cycling through the list
    t.pencolor(colors[i % 5])
    
    # Draw a circle
    t.circle(120)
    
    # Rotate the turtle's starting position for the next circle
    t.right(6)
    
screen.exitonclick()