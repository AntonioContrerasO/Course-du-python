import random
from turtle import Turtle as t, Screen
import random as rd

tim = t()
tim.shape("turtle")
tim.color("Blue", "DarkOrange")

# Square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()
# print(heroes.gen())

# Linea punteada
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # simular Pi
# for i in range(3,100):
#     tup = (rd.random(), rd.random(), rd.random())
#     tim.pencolor(tup)
#     for w in range(1,i+1):
#         tim.forward(20)
#         tim.left(360/i)

# random caminata
# directions = [0,90,180,270]
#
# size = 2
# tim.speed(0)
# while True:
#     tim.forward(30)
#     tup = (rd.random(), rd.random(), rd.random())
#     tim.pencolor(tup)
#     tim.pensize(size)
#
#     tim.setheading(directions[rd.randint(0,3)])
#     if size == 9:
#         break
#     size += 0.01

tim.speed(0)
angle = 0
size = 1
for _ in range (100):
    tup = (rd.random(), rd.random(), rd.random())
    tim.pencolor(tup)
    tim.circle(100)
    angle += 1
    size += 1/360
    print(angle)
    tim.left(angle)
    tim.pensize(size)


screen = Screen()
screen.exitonclick()
