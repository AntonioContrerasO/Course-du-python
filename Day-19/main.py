import random
from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.back(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def clear_screen():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=clear_screen, key="c")
# screen.exitonclick()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles = []
for color in colors:
    turtles.append(Turtle(shape="turtle"))
extra_y = 0
for i in range(0, 6):
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].setposition(-230, -125 + extra_y)
    extra_y += 50

if user_bet:
    is_race_on = True

number = 0
while is_race_on:
    if turtles[number].xcor() > 230:
        winner_color = turtles[number].pencolor()
        if winner_color.lower() == user_bet.lower():
            print(f"You've won!, The turtle {winner_color} wins")
        else:
            print(f"You've lost!, The turtle {winner_color} wins")
        break
    random_distance = random.randint(0, 10)
    turtles[number].forward(random_distance)
    number += 1
    if number == 6:
        number = 0
