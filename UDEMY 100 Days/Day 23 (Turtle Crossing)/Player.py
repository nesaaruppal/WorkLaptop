from turtle import *



class User(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(x=0, y=-200)
        self.setheading(90)
        
    def move_forward(self):
        self.forward(10)
        