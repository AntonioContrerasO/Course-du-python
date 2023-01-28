from turtle import Turtle


class State(Turtle):

    def __init__(self,name,x,y):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write(f"{name}", align="center")


