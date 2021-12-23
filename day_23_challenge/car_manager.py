from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(x=300, y=randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

        # print(self.run)
