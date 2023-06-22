from turtle import Screen, Turtle
from Objects import Cube
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.title("TETRIS")
screen.bgcolor("black")
screen.tracer(0)

cube = Cube()




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    cube.square()


screen.exitonclick()