from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_right():
    new_heading = tim.heading() + 45
    tim.setheading(new_heading)
    
def turn_left():
    new_heading = tim.heading() - 45
    tim.setheading(new_heading)


screen = Screen()
screen.setup(width=450, height=450)
screen.title("Etch A Sketch!")
screen.bgcolor("black")

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)


tim = Turtle()
tim.color("blue")




screen.exitonclick()