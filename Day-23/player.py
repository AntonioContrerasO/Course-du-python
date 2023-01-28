import random
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color((random.random(), random.random(), random.random()))
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_y = 10

    def move(self):
        self.goto(0,self.ycor()+self.move_y)

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            self.__init__()
            return True
        return False





