import turtle

import colorgram as c
from turtle import Turtle, Screen
from random import choice

# Colors
colors = c.extract("image.jpeg", 20)
palette = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    palette.append(rgb)

# Turtle
"""10 x 10 grid, size 20, space_between 50"""
turtle.colormode(255)
indi = Turtle()
indi.speed("fastest")
indi.penup()
indi.setpos(-250, -250)
indi.hideturtle()

for i in range(10):
    new_y = indi.pos()[1] + 50
    indi.setpos(-250, new_y)
    for _ in range(10):
        indi.dot(20, choice(palette))
        indi.forward(50)
indi.home()


# Screen
my_screen = Screen()
my_screen.exitonclick()