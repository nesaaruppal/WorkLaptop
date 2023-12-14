from turtle import * 
from datetime import datetime as dt
import time


def draw_square(self):
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)

second = dt.now().second
minute = dt.now().minute
hour = dt.now().hour

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Digital Clock!")

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.speed("fastest")
turtle1.color("blue")
turtle1.penup()
turtle1.pensize(3)
turtle1.goto(x=-225, y=-225)
turtle1.pendown()

t = Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()
t.goto(x=-75, y=0)




draw_square(turtle1)


while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hour).zfill(2)
            + ":"+str(minute).zfill(2)+":"
            + str(second).zfill(2),
            font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    second += 1
 
    if second == 60:
        second = 0
        minute += 1
 
    if minute == 60:
        minute = 0
        hour += 1
 
    if hour == 13:
        hour = 1




    screen.mainloop()