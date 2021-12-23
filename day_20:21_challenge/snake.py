from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        # new_seg.speed(1)
        new_seg.penup()
        new_seg.setpos(position)
        self.segments.append(new_seg)

    def extend(self):
        # add new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self, direction=""):
        # for body_num in range(start, stop, step):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(x=new_x, y=new_y)
        self.head.forward(20)

    # directions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

