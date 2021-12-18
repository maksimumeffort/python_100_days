import turtle
from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.shape("arrow")
tim.color("DarkRed")
tim.pensize(5)
tim.speed("fastest")
turtle.colormode(255)
directions = [90, -90, 0, 180]

"""
# initial solution
    angle = 360 / sides
    for sides in range(4, 11):
        color = choice(colors)
        tim.pencolor(color)
        colors.remove(color)

        for i in range(sides):
            tim.right(360/sides)
            tim.forward(100)
colors = ["DarkRed", "GreenYellow", "Khaki", "LemonChiffon", "SeaGreen", "Cyan", "CadetBlue", "DeepPink",
          "Gainsboro", "MediumSlateBlue", "DarkOrange", "Gold", "DarkSlateGray", "Wheat"]
def draw_shape(num_sides):
    tim.pencolor(choice(colors))
    for _ in range(num_sides):
        tim.right(360/ num_sides)
        tim.forward(100)


for sides in range(3, 11):
    draw_shape(sides)
"""


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


"""
random walk

def draw_path():
    tim.pencolor(random_color())
    tim.setheading(choice(directions))
    tim.forward(35)

for i in range(300):
    draw_path()
"""


def draw_spirograph(gap_size):
    for _ in range(int(360/ gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(20)

screen = Screen()
screen.exitonclick()
