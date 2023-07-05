from turtle import Turtle, Screen
import random
import turtle

colours = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim = Turtle()
tim.shape("turtle")
tim.shapesize(5)
tim.color("Blue")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 60):
    tim.color(random.choice(colours))
    tim.pensize(15)
    draw_shape(shape_side_n)


screen = Screen()
screen.screensize(250)
screen.canvheight(800)
screen.canvwidth(800)
screen.exitonclick()
