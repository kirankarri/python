from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_STARTING_LINE = list(range(-270,270))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_collection=[]
        self.hideturtle()
        self.car_reset()

    def add_car(self,car):
        self.car_collection.append(car)
        
    def move_forward(self,level):
        for car in self.car_collection:
            if car.xcor() < -280:
                self.car_collection.remove(car)
                car.hideturtle()
                new_car = Car()
                new_car.create_car()
                self.car_collection.append(new_car)
                pass
            else:
                new_x = car.xcor() - STARTING_MOVE_DISTANCE - (level-1) * MOVE_INCREMENT
                new_y = car.ycor()
                car.goto(new_x,new_y)

    def car_reset(self):
        for i in range(10):
            car = Car()
            self.add_car(car)
    
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape('square')
        self.seth(90)
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(2,1)
        self.goto(random.choice(list(range(180,300))),random.choice(CAR_STARTING_LINE))
        
