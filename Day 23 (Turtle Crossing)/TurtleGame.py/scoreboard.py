from turtle import Turtle

FONT = ("Cascadia Code", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.update_scoreboard()
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)
