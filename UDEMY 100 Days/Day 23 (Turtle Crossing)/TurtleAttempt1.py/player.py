from turtle import Turtle

#MOVE_DISTANCE = 10
STARTING_POINT = (0, -225)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POINT)
        
    def move_forward(self):
        self.forward(10)
        
    def is_at_finish_line(self):
        if self.ycor() > 225:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(STARTING_POINT)
        
    
    