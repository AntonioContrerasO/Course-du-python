from turtle import Turtle, Screen
from random import randint
from  ColorsData import colors
# import colorgram
#
# colors = colorgram.extract("image.jpg",30)
# color_list = []
# for i in range(0,len(colors)):
#     red = colors[i].rgb[0]
#     green = colors[i].rgb[1]
#     bleu = colors[i].rgb[2]
#     color_list.append((red,green,bleu))
#
# print(color_list)

screen = Screen()
screen.colormode(255)
screen.setup(534,534)
timmy = Turtle()
timmy.penup()
extraY = 0
timmy.setposition(-225,-200)
for i in range(1,101):
    timmy.dot(20,colors[randint(0,len(colors)-1)])
    timmy.forward(50)
    if i % 10 == 0:
        extraY += 50
        timmy.setposition(-225, -200 + extraY)


screen.exitonclick()
