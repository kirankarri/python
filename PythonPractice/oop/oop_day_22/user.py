from turtle import Turtle

class User(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.position = ''
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.turtle_score = Turtle()
        self.turtle_score.color('white')
        self.turtle_score.hideturtle()
        self.turtle_score.penup()
        if position == 'left':
            self.goto(-280,0)
            self.position = 'left'
            self.turtle_score.goto(-20,250)
            self.turtle_score.write(f'{self.score}',align='center',font=('Arial',20,'normal'))
            
        else:
            self.goto(280,0)
            self.position = 'right'
            self.turtle_score.goto(20,250)
            self.turtle_score.write(f'{self.score}',align='center',font=('Arial',20,'normal'))
            
        
