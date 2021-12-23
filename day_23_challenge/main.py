import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

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

# ScoreBoard
scoreboard = Scoreboard()

loop_num = 0
game_is_on = True
while game_is_on:
    time.sleep(0.07)
    if loop_num % 6 == 0:
        car_generator.generate_car()
    car_generator.move()

    # detect collision with cars
    for car in car_generator.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect if player has reached top edge
    if player.finished():
        player.reset_position()
        car_generator.speed_up()
        scoreboard.level_up()

    screen.update()
    loop_num += 1

screen.exitonclick()
