from turtle import Screen, Turtle


def tim_square():
    tim.forward(200)
    tim.right(90)
    tim.forward(200)
    tim.right(90)
    tim.forward(200)
    tim.right(90)
    tim.forward(200)


tim = Turtle()
tim.shape("turtle")
tim.shapesize(10)
tim.color("Blue")

tim_square()


screen = Screen()
screen.screensize(100)
screen.exitonclick()
