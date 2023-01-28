import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 0
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def new_level(self):
        self.level += 0.1

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE +(MOVE_INCREMENT)*self.level)

