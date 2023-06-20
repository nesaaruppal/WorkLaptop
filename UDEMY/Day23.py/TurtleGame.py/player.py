from turtle import Turtle

STARTING_POSITION = (0, -275)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        self.go_to(STARTING_POSITION)
        
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    
    