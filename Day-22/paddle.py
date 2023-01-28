from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = 0
        self.shape("square")
        self.penup()
        self.color("White")
        self.setposition(self.x_pos, self.y_pos)
        self.shapesize(stretch_wid=5, stretch_len= 1)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
