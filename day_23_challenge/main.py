import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player
player = Player()
screen.onkey(fun=player.up, key="Up")

# CarManager
car_generator = CarManager()

loop_num = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if loop_num % 6 == 0:
        car_generator.generate_cars()
    car_generator.move()

    # detect collision with cars
    for car in car_generator.cars:
        if player.distance(car.xcor(), car.ycor()) < 25:
            game_is_on = False

    # detect if player has reached top edge
    if player.finished():
        player.reset_position()
        car_generator.speed_up()

    screen.update()
    loop_num += 1

# TODO 5: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
#  successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the
#  centre.

screen.exitonclick()
