from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=1000, height=800)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]


tim = Turtle(shape="turtle")
tim.shapesize(5)
tim.penup()
tim.color("red")
tim.goto(x=-450, y=100)

tom = Turtle(shape="turtle")
tom.shapesize(5)
tom.penup()
tom.color("orange")
tom.goto(x=-450, y=200)

dan = Turtle(shape="turtle")
dan.shapesize(5)
dan.penup()
dan.color("yellow")
dan.goto(x=-450, y=300)

jack = Turtle(shape="turtle")
jack.shapesize(5)
jack.penup()
jack.color("green")
jack.goto(x=-450, y=0)

ben = Turtle(shape="turtle")
ben.shapesize(5)
ben.penup()
ben.color("blue")
ben.goto(x=-450, y=-100)

john = Turtle(shape="turtle")
john.shapesize(5)
john.penup()
john.color("purple")
john.goto(x=-450, y=-200)


screen.exitonclick()
