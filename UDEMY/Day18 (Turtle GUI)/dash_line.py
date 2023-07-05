from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.shapesize(10)
tim.color("Green")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.screensize(200)
screen.exitonclick()
