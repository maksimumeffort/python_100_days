from turtle import Turtle
score = ('Courier', 18, 'normal')
game = ('Courier', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=score)

    def refresh(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align='center', font=game)

