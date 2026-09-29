from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-150,280)
        self.write(f' Level {self.level}',align='center',font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f' Level {self.level}',align='center',font=FONT)
    
