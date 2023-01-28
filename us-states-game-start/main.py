import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
states_list_x = data["x"].to_list()
states_list_y = data["y"].to_list()

guessed_states = []

score = 50 - len(states_list)
game_is_on = True
while game_is_on:
    screen.update()
    answer_state = screen.textinput(title=f"{score}/50 Guess the State",prompt="What's another state?")
    for check in states_list:
        if check.lower() == answer_state.lower():
            score +=1
            index = states_list.index(check)
            name = states_list[index]
            x_pos = states_list_x[index]
            y_pos = states_list_y[index]
            State(name,x_pos,y_pos)
            states_list.remove(check)
            states_list_x.remove(x_pos)
            states_list_y.remove(y_pos)
            guessed_states.append(name)
    if answer_state.lower() == "exit":
        break


states_to_learn = {"state":states_list,"x":states_list_x,"y":states_list_y}

data = pandas.DataFrame(states_to_learn)
print(data)
data.to_csv("States_to_learn.csv")

