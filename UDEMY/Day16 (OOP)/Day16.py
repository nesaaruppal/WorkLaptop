from prettytable import PrettyTable
from turtle import Turtle
from turtle import Screen
import turtle

# FIRST OBJECT
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("Red")
timmy.shapesize(5)
timmy.forward(250)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()


# TABLE DATA
table = PrettyTable()

table.add_column("Lower Ground", ["Yes", "No", "Report"])
table.add_column("7th Floor", ["Yes", "No", "Report"])
table.add_column("Other Rooms", ["Yes", "No", "Report"])
table.align = "l"

print(table)
