from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-225)
        self.setheading(90)

    def create_turtle(self):
        super().__init__()
        self = Player()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-225)
        self.setheading(90)
        
    def move(self):
        self.forward(10)