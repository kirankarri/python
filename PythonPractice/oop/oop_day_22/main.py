from turtle import Turtle, Screen
from user import User
from pong_game import pong_game
import random
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.listen()
screen.tracer(0)
screen.title('Pong')
screen.bgcolor('black')
pong = pong_game()


speed = 0.1
while pong.left_user.score < 10 and pong.right_user.score < 10:
    screen.update()
    time.sleep(speed)
    pong.move()
    #print(pong.ball.distance(pong.left_user))
    #print(pong.ball.distance(pong.left_user))
    if pong.ball.distance(pong.left_user) < 30 or pong.ball.distance(pong.right_user) < 30:
        print('distance')
        if pong.ball.xcor() > 0:
            pong.increase_score(pong.right_user)
        else:
            pong.increase_score(pong.left_user)
        pong.bounce_on_paddle()
        speed /= 10
        
    elif pong.ball.xcor() > 280 or pong.ball.xcor() < -280:
        if pong.ball.xcor() > 0:
            pong.increase_score(pong.left_user)
        else:
            pong.increase_score(pong.right_user)
        pong.ball_reset()
    if pong.ball.ycor() > 280 or pong.ball.ycor() < -280:
        pong.bounce()
        

    screen.onkeypress(lambda:pong.move_up(pong.left_user),'w')
    screen.onkeypress(lambda:pong.move_up(pong.right_user),'Up')
    screen.onkeypress(lambda:pong.move_down(pong.left_user),'s')
    screen.onkeypress(lambda:pong.move_down(pong.right_user),'Down')



screen.exitonclick()