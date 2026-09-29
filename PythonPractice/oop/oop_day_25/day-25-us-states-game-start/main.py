from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.screensize(400,400)
screen.title('US States quiz')
screen.bgpic('blank_states_img.gif')
states_data = pandas.read_csv('50_states.csv')
states_length = len(list(states_data.state))
i = 0
while i < states_length:
    input_state = screen.textinput(title='Enter US State name',prompt='Enter state name');
    if input_state in list(states_data.state):
        print('hit')
        state_record = states_data[states_data['state']==input_state]
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(state_record['x'].item(),state_record['y'].item())
        state.write(f'{input_state}')
        i += 1



screen.exitonclick()