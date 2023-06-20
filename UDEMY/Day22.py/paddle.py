from turtle import *

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


#paddle2 = Turtle ()
#paddle2.shape("square")
#paddle2.color("White")
#paddle2.shapesize(stretch_wid=5, stretch_len=1)
#paddle2.penup()
#paddle2.speed("fastest")
#paddle2.goto(y=0, x=-280)