from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
run = 1

class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(x=randint(50, 700), y=randint(-240, 240))
        self.cars.append(car)

    def move(self, inc=0):

        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + inc)

    def speed_up(self):
        global run
        increment = MOVE_INCREMENT * run
        self.move(increment)
        run += 1
        print(increment)





