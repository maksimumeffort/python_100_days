from turtle import Screen, Turtle
import time

# Keys
direction = 3

def up():
    global direction
    if direction != 0:
        direction = 0

def down():
    global direction
    if direction != 1:
        direction = 1

def left():
    global direction
    if direction != 2:
        direction = 2

def right():
    global direction
    if direction != 3:
        direction = 3


def turn():
    global direction
    
    if direction == 1:
        return 270
    elif direction == 0:
        return 90
    elif direction == 2:
        return 180
    elif direction == 3:
        return 0

# screen init
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# snake init
segments = []



for i in range(3):
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.penup()
    pos_x = new_seg.xcor() - 20 * i
    new_seg.setpos(x=pos_x, y=0)
    segments.append(new_seg)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for s in range(len(segments) - 1, 0, -1):
        new_x = segments[s - 1].xcor()
        new_y = segments[s - 1].ycor()
        segments[s].goto(x=new_x, y=new_y)
    segments[0].seth(turn())
    segments[0].forward(20)



screen.exitonclick()



