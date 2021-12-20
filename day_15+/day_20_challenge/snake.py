from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_seg = Turtle(shape="square")
            new_seg.color("white")
            # new_seg.speed(1)
            new_seg.penup()
            pos_x = new_seg.xcor() - 20 * i
            new_seg.setpos(x=pos_x, y=0)
            self.segments.append(new_seg)

    def move(self, direction=""):
        # for body_num in range(start, stop, step):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)

    # directions
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)

