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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align='center', font=score)

    def refresh(self):
        self.score += 1
        self.show_score()

    # change high score if greater than previous high score
    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.show_score()

