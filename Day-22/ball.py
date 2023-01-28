from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 0
        self.y = 0
        self.goto(self.x, self.y)
        self.change_in_y = 10
        self.change_in_x = 10

    def move(self):
        self.x += self.change_in_x
        self.y += self.change_in_y
        self.goto(self.x, self.y)

    def bounce(self):
        self.change_in_y *= -1

    def collision_with_paddle(self):
        self.change_in_x *= -1

    def restart(self,left_right):
        self.reset()
        self.__init__()
        if left_right == "right":
            self.change_in_x *= -1

