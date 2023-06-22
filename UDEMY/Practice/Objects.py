from turtle import Turtle
import random

STARTING_POINT = (0, 230)
X_STARTING_POINT = [(0)]
Y_STARTING_POINT = [(230)]
COLORS = ["red","green","purple","orange","yellow"]


class Cube(Turtle):
    def __init__(self):
        super().__init__()
        
        
    def starting_point(self):
        self.goto(STARTING_POINT)
        
    def square(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()

        
   # def top_right_square(self):
   #     self = Turtle()
   #     self.shape("square")
   #     self.shapesize()
   #     self.color(random.choice(COLORS))
   #     self.penup()
   # 
   # def top_left_square(self):
   #     self.shape("square")
   #     self.color(random.choice(COLORS))
   #     self.penup()
   # 
   # def bottom_right_square(self):
   #     self.shape("square")
   #     self.__sizeof__()
   #     self.color(random.choice(COLORS))
   #     self.penup()
   #     
   # def bottom_left_square(self):
   #     self.shape("square")
   #     self.__sizeof__()
   #     self.color(random.choice(COLORS))
   #     self.penup()
   #     
   #             
   # def move_down(self):
   #     new_y = self.ycor() - 40
   #     self.goto(x=0, y=new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x, new_y)
        