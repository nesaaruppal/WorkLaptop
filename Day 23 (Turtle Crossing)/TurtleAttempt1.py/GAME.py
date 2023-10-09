from turtle import Turtle, Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=500, height=500)
screen.title("Turtle Crossing!")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")


game_is_on = True 
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
     
# Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

#Detect when at finish line 
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()



screen.exitonclick()