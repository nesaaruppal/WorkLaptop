from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_INCREMENT = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_INCREMENT
        
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-280, 280)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT