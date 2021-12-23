from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.speed(3)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(x=randint(20, 700), y=randint(-240, 240))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)




