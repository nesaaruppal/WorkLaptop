from turtle import Turtle
import random

COLOURS = ["red", "orange", "pink", "blue", "purple", "yellow"]
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5
        

        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:  
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,   stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-225, 225)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT