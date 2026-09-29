from turtle import Turtle, Screen
import random
import config

class Snake():
    def __init__(self):
        self.turtle_collection = []
        self.create_snake()
        self.snake_head = self.turtle_collection[0]
        self.snake_tail = self.turtle_collection[len(self.turtle_collection)-1]

    def create_snake(self):
        for i in range(3):
            timmy = Turtle()
            #timmy.speed('fastest')
            timmy.shape('square')
            timmy.color('white')
            timmy.penup()
            if i > 0:
                timmy.goto(self.turtle_collection[i-1].xcor()-20,self.turtle_collection[i-1].ycor())
            else:
                timmy.goto(20,0)
            
            self.turtle_collection.append(timmy)

    def grow_snake(self):
        timmy = Turtle()
        timmy.speed('fastest')
        timmy.shape('square')
        timmy.color('white')
        timmy.penup()
        timmy.goto(self.snake_tail.xcor()+20,self.snake_tail.ycor())
        self.turtle_collection.append(timmy)

    def move_snake(self,screen):
        for i in range(len(self.turtle_collection)-1,0,-1):
            new_x = self.turtle_collection[i-1].xcor()
            new_y = self.turtle_collection[i-1].ycor()
            self.turtle_collection[i].goto(new_x,new_y)
        self.turtle_collection[0].forward(20)
        self.snake_head = self.turtle_collection[0]
        self.snake_tail = self.turtle_collection[len(self.turtle_collection)-1]

        
    def turn(self,timmy,key):     
        if (timmy.heading() == 0.0 or timmy.heading() == 180.00) and key == 'Up':
            timmy.seth(90)
            config.config_reset();
            config.is_moving_up = True
        elif (timmy.heading() == 0.0 or timmy.heading() == 180.00) and key == 'Down':
            timmy.seth(270)
            config.config_reset();
            config.is_moving_down = True  
        elif (timmy.heading() == 90.0 or timmy.heading() == 270.00) and key == 'Left':
            timmy.seth(180) 
            config.config_reset();
            config.is_moving_left = True
        elif (timmy.heading() == 90.0 or timmy.heading() == 270.00) and key == 'Right':
            timmy.seth(0) 
            config.config_reset();
            config.is_moving_right = True

    def is_click(self,timmy, key):
        self.turn(timmy, key)