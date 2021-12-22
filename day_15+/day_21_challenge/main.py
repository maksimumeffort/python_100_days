from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POS = [-350, 350]
# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paddles
l_paddle = Paddle(POS[0])
r_paddle = Paddle(POS[1])

# ball
ball = Ball()

# scoreboard
scoreboard = Scoreboard()

screen.listen()
# left paddle controls
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

# right paddle controls
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # PADDLE BUG FIX:
    right_paddle_dimension = 330 < ball.xcor() < 350
    left_paddle_dimension = -330 > ball.xcor() < 350

    right_paddle = ball.distance(r_paddle) < 50 and right_paddle_dimension
    left_paddle = ball.distance(l_paddle) < 50 and left_paddle_dimension

    # detect if missed right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if missed left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # detect collision with paddle
    if right_paddle or left_paddle:
        print(f"right paddle position: {r_paddle.position()}")
        print(f"left paddle position: {l_paddle.position()}")
        print(f"ball position: {ball.position()}")
        ball.bounce_x()

    screen.update()


screen.exitonclick()
