from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.goto(random.choice(list(range(-300,300))),random.choice(list(range(-300,300))))
        


    def generate_food(self):
        self.goto(random.choice(list(range(-300,300))),random.choice(list(range(-300,300))))
