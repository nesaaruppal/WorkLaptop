from turtle import *
from Player_Manager import Player
from CarManager import CarCreator
import time

screen = Screen()
screen.screensize(500, 500)
screen.title("Turtle Crossing")
screen.tracer(0)

tim = Player()
car = CarCreator()

screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    
           
screen.exitonclick()