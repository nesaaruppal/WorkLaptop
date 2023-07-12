from turtle import *
import time

def move_up():
    tim.forward(10)

game_is_on = True

while game_is_on:
    screen = Screen()
    screen.title("Turtle Crossing!")
    screen.setup(width=500, height=500)
    
    
    tim = Turtle()
    tim.penup()
    tim.goto(x=0, y=-200)
    tim.shape("turtle")
    tim.setheading(90)
    
    
    screen.listen()
    screen.onclick(move_up, "w")
    
    
    screen.exitonclick()