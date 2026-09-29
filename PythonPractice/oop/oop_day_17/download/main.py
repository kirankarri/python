from turtle import Turtle, Screen
import turtle as t
import random
import string

t.colormode(255)
timmy = Turtle()
screen = Screen()
directions = [0,90,180,360]
colors = list(range(1,100))
angle = list(range(0,361))
timmy.shape('turtle')
timmy.speed(0)

def draw_shape(timmy, sides):
    for i in range(sides):
        angle = 360/sides
        timmy.forward(100)
        timmy.right(angle)



def random_walk(timmy):
    count = 0 
    while count < 200:
        timmy.seth(random.choice(directions))
        timmy.pencolor((random.choice(colors),random.choice(colors),random.choice(colors)))
        timmy.forward(30)
        count += 1
        

def spirograph(timmy):
    i = 0
    while i < 361:
        timmy.pencolor((random.choice(colors),random.choice(colors),random.choice(colors)))
        timmy.circle(100)
        timmy.right(angle[i])
        i += 1


spirograph(timmy)

#timmy.forward(100)
#timmy.right(60)



screen.exitonclick();
