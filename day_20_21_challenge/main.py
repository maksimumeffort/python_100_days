from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen init
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


def game_over():
    global game_is_on
    # game_is_on = False
    # scoreboard.game_over()


while game_is_on:
    scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    # Walls
    north_wall = snake.head.ycor() > 280
    south_wall = snake.head.ycor() < -280
    west_wall = snake.head.xcor() < -280
    east_wall = snake.head.xcor() > 280

    # detect collision with wall
    if north_wall or south_wall or west_wall or east_wall:
        scoreboard.reset_scoreboard()
        # game_over()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_over()
            scoreboard.reset_scoreboard()
            snake.reset()

screen.exitonclick()
