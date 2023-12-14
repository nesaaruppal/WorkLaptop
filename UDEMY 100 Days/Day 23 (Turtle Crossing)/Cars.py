from turtle import *
import random

COLOURS = ["red", "blue", "green", "pink", "purple", "yellow"]

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        all_cars = []
        
    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.shape("square")
            self.shapesize(stretch_len=1, stretch_wid=2)
            self.color(random.choice(COLOURS))
            self.penup()
            new_y = random.randint(-200, 200)
            self.goto(x=250, y=new_y)
            self.backward(100)
        
        