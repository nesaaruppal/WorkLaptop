import random
import turtle

# A function to draw the canvas


def draw_square(x, y, width):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color("#333333")
    for side in range(0, 4):
        turtle.forward(width)
        turtle.right(90)
    turtle.pensize(1)

# A function to draw the circle


def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("#333333")
    turtle.circle(radius)
    turtle.pensize(1)

# A function to draw a dot


def draw_dot(x, y, color):
    turtle.penup()
    turtle.goto(x, y - 1)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(1)
    turtle.end_fill()


# Main program starts here
radius = 180
total = 2500
total_in = 0
turtle.setup(width=600, height=600)
turtle.hideturtle()
turtle.tracer(0)
turtle.speed(0)
draw_square(-radius, radius, 2 * radius)
draw_circle(0, 0, radius)
for dots in range(0, total):
    x = random.randint(-radius, radius)
    y = random.randint(-radius, radius)
    # Apply Pythagoras formula to find out the distance to the center of the screen
    distance = (x**2 + y**2)**0.5
    # Check if dot is in the circle
    if distance < radius:
        color = "#FF0000"
        total_in += 1
    else:
        color = "#0000FF"
    # Draw dot
    draw_dot(x, y, color)
turtle.done()
# Applying Monte Carlo's method to estimate Pi
pi = 4 * (total_in / total)
print("Pi Estimation:", pi)
