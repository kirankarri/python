from turtle import Turtle, Screen
import random
from snake_game import Snake
from food import Food
from scoreboard import Score
import config
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

def turtle_race():
    colors = ['red','orange','yellow','green','blue','purple']
    user_bet = screen.textinput(title="Which turtle win the race",prompt='Enter a color of turtle you think will win the race ?')
    turtle_collection = []
    for i in range(len(colors)):
        temp_turtle = Turtle('turtle')
        temp_turtle.penup()
        temp_turtle.color(colors[i])
        temp_turtle.goto(-230,30*i-60)
        turtle_collection.append(temp_turtle)

    isFinish = False
    while(not(isFinish)):
        selected_turtle = turtle_collection[random.choice(list(range(0,6)))]
        selected_turtle.forward(10)
        if selected_turtle.xcor() > 230:
            isFinish = True
    if selected_turtle.pencolor() == user_bet:
        print(f'Race is won by {selected_turtle.pencolor()}')
    else:
        print(f'You lost. Race is won by {selected_turtle.pencolor()}')    


#turtle_race();

snake = Snake()
food = Food()
score = Score()
print(score.ycor())
isFailed = False
while not(isFailed):
    snake_head = snake.snake_head
    snake_tail = snake.snake_tail
    screen.onkeypress(lambda: snake.turn(snake_head, 'Up'), 'Up')
    screen.onkeypress(lambda: snake.turn(snake_head, 'Down'), 'Down')
    screen.onkeypress(lambda: snake.turn(snake_head, 'Left'), 'Left')
    screen.onkeypress(lambda: snake.turn(snake_head, 'Right'), 'Right')
    if snake_head.xcor() > 300.0 or snake_head.ycor() > 300 or snake_head.xcor() < -300 or snake_head.ycor() < -300:
        score.update_high_score()
        for snake_var in snake.turtle_collection:
            snake_var.hideturtle()
        snake = Snake()
        #score.game_over()
    else:
        screen.update()
        time.sleep(0.1)
        snake.move_snake(screen)        
    if snake_head.distance(food) < 15:
        
        time.sleep(0.01)
        screen.update()
        snake.grow_snake()
        score.increase_score()
        food.generate_food()
        
    for temp_snake in snake.turtle_collection[1:]:    
        if snake_head.distance(temp_snake) < 15:
            isFailed = True
            score.game_over()

        
    
screen.exitonclick()