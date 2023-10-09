from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #Read the data file
        with open("UDEMY\Day24.py\SnakeGame2\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            #Write to the data file
            with open("UDEMY\Day24.py\SnakeGame2\data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
