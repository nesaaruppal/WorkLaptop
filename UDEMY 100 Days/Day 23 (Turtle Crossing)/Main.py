# Create screen
from turtle import * 
from Player import User
from Cars import Blocks
import time


screen = Screen()
screen.title("Turtle Crossing!")
screen.setup(width=500, height=500)

player = User()
block = Blocks()


screen.listen()
screen.onkey(player.move_forward, "Up")




screen.exitonclick()

game_on = True
while game_on:
    time.sleep(0.00001)
    screen.update()
    
    block.create_cars()



# Create a cars class and get them to move 



# Detect collision with car



# Detect collision when turtle reaches the end 



# Increase speed of cars and level each time



#Create Scoreboard