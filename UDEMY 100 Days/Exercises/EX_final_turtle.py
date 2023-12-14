from turtle import Turtle
import random

tim = Turtle()


colours = ["Red", "Blue", "Green", "Orange",
           "Yellow", "Black", "Brown", "Pink"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
