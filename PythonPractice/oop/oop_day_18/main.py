from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(100)

def move_backward():
    timmy.backward(100)

def move_clockwise():
    timmy.seth(timmy.heading()+ 10)

def move_counter_clockwise():
    timmy.seth(timmy.heading() -10)

def clear():
    timmy.penup()
    timmy.clear()
    timmy.setpos(0,0)
    timmy.seth(0)
    timmy.pendown()

screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_backward,'s')
screen.onkeypress(clear,'c')
screen.onkeypress(move_clockwise,'a')
screen.onkeypress(move_counter_clockwise,'d')

screen.exitonclick()