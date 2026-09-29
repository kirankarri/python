from turtle import Turtle
from user import User

class pong_game():
    def __init__(self):
        self.left_user = User('left')
        self.right_user = User('right')
        self.middle_line()
        self.ball = self.create_ball()
        self.xmove = 10
        self.ymove = 10

    def create_ball(self):
        pong = Turtle()
        pong.color('white')
        pong.penup()
        pong.shape('circle')
        pong.goto(0,200)
        return pong
    
    def bounce(self):
        self.ymove *= -1

    def bounce_on_paddle(self):
        self.xmove *= -1


    def move(self):
        new_x = self.ball.xcor() + self.xmove
        new_y = self.ball.ycor() + self.ymove
        self.ball.goto(new_x,new_y)

    def increase_score(self,user):
        user.score += 1
        user.turtle_score.clear()
        user.turtle_score.write(f'{user.score}',align='center',font=('Arial',20,'normal'))

    def decrease_score(self,user):
        user.score -= 1
    
    def middle_line(self):
        center_line = Turtle()
        center_line.color('white')
        center_line.penup()
        center_line.goto(0,-250)
        center_line.pendown()
        center_line.goto(0,250)
        center_line.hideturtle()

    def ball_reset(self):
        self.ball.goto(0,0)    
        
    def move_up(self,user):
        if user.ycor() < 250:
            user.goto(user.xcor(),user.ycor()+20)

    def move_down(self,user):
        if user.ycor() > -250:
            user.goto(user.xcor(),user.ycor()-20)