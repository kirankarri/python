import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
time.sleep(0.1)
screen.update()
screen.tracer(0)
screen.listen()
turtle_player = Player()
car_manager = CarManager()
level = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(lambda:turtle_player.move_forward(),'Up')
    car_manager.move_forward(level.level)
    if turtle_player.ycor() > 280:
        level.increase_level()
        turtle_player.player_reset()
    for car in car_manager.car_collection:
        if car.distance(turtle_player) < 20:
            level = Scoreboard()
            level.goto(0,0)
            level.write(f' Game Over',align='center',font=("Courier", 24, "normal"))
            game_is_on = False
            break
        

screen.exitonclick()