from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        new_pos = self.ycor() + 20
        self.goto(x=0, y=new_pos)

    def finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def reset_position(self):
        self.goto(STARTING_POSITION)
