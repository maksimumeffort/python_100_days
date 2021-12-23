from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.color("white")
        self.goto(x=position, y=0)

    def up(self):
        # PADDLE FIX:
        if self.ycor() < 245:
            self.forward(20)


    def down(self):
        if self.ycor() > -230:
            self.backward(20)

