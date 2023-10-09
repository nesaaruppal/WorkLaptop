import random 
from turtle import * 

def blue_circle(self):
    self.hideturtle()
    self.penup()
    self.goto(x=-150, y=0)
    self.speed("fastest")
    self.pendown()
    self.pensize(10)
    self.color("blue")
    self.circle(50)

def yellow_circle(self):
    self.hideturtle()
    self.penup()
    self.goto(x=-50, y=-100)
    self.speed("fastest")
    self.pendown()
    self.pensize(10)
    self.color("yellow")
    self.circle(50)
    
def black_circle(self):
    self.hideturtle()
    self.penup()
    self.goto(x=0, y=0)
    self.speed("fastest")
    self.pendown()
    self.pensize(10)
    self.color("black")
    self.circle(50)
    
def green_circle(self):
    self.hideturtle()
    self.penup()
    self.goto(x=50, y=-100)
    self.speed("fastest")
    self.pendown()
    self.pensize(10)
    self.color("green")
    self.circle(50)


screen = Screen()
screen.setup(width=500, height=400)
screen.title("OLYMPICS!")

t = Turtle()

blue_circle(t)
yellow_circle(t)
black_circle(t)
green_circle(t)



screen.mainloop()