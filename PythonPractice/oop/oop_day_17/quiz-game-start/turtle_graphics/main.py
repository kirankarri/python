from turtle import Turtle, Screen
import turtle as t
import random
import string
import colorgram

t.colormode(255)
timmy = Turtle()
screen = Screen()
directions = [0,90,180,360]
angle = list(range(0,361))
timmy.shape('arrow')
colors = colorgram.extract('download1.png', 100)
print(len(colors))

def draw_shape(timmy, sides):
    for i in range(sides):
        angle = 360/sides
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
        timmy.pencolor
        timmy.circle(100)
        timmy.right(angle[i])
        i += 1

def hirst_painting(timmy):
    timmy.penup()
    for x in range(10):
        for y in range(10):  
            timmy.goto(-100+50*x,-100+50*y)
            timmy.dot(20,colors[random.choice(list(range(1,len(colors))))].rgb)
    


hirst_painting(timmy)

#timmy.forward(100)
#timmy.right(60)



screen.exitonclick();
