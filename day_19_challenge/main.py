from turtle import Turtle, Screen
import random as r

# Etch-A-Sketch app
"""
tim = Turtle()
my_screen = Screen()

# angle = 0

def go_straight():
    tim.fd(10)

def go_back():
    tim.bk(10)

def turn_right():
    new_h = tim.heading() - 10
    tim.seth(new_h)

def turn_left():
    new_h = tim.heading() + 10
    tim.seth(new_h)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=go_straight)
my_screen.onkey(key="s", fun=go_back)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()
"""

# Turtle Race

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

# Turtles assemble
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    pos_y = -125 + (50 * i)
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=pos_y)
    all_turtles.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race:")
if user_bet:
    is_race_on = True

# Starting the game
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"{winning_color.capitalize()} turtle won the race. You've won!")
            else:
                print(f"{winning_color.capitalize()} won the race. You've lost!")
        rand_dist = r.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
