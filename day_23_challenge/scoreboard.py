from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-220, y=260)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT)
