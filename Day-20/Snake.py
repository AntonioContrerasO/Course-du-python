import random
from turtle import Turtle

UP = 90
Down = 270

position = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.snake = []
        for i in range(3):
            self.add_segment(position[i])

    def move(self):
        x = random.random()
        y = random.random()
        z = random.random()
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
            self.snake[i].color((x,y,z))
        self.snake[0].forward(20)
        self.snake[0].color((x, y, z))



    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)


    def add_segment(self,postion):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(postion)
        self.snake.append(segment)

    def grow(self):
        self.add_segment(self.snake[-1].position())
