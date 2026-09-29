from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.write(f'Score: {self.score}',align='center',font=('Arial',20,'normal'))
        self.highscore = 0

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over',align='center',font=('Arial',20,'normal'))

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}' ,align='center',font=('Arial',20,'normal'))  

    def increase_score(self):
        self.score += 1  
        self.update_score()    

    def update_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
