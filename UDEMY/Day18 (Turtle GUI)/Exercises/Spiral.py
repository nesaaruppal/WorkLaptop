import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.pensize(20)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
t.bgpic("image.jpg")

t.bgpic()
