import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# # setup input field
# guess_window = turtle.Turtle()
# guess_window.textinput(title="Guess the State", prompt="What's another state name?")

# database setup
db = pandas.read_csv("50_states.csv")
states_array = db.state.to_list()

# setup map turtle
map_turtle = turtle.Turtle()
correct_guesses = []

# set up input field

guessing = True
# TODO: 4.
while guessing:
    # TODO: 1 & 6
    answer = screen.textinput(title=f"{len(correct_guesses)}/{len(states_array)} States Correct", prompt="What's another state name?").title()
    # TODO: 2.
    if answer in states_array:
        # TODO: 3.
        row = db[db.state == answer]
        map_turtle.penup()
        map_turtle.hideturtle()
        map_turtle.goto(x=int(row.x + 1), y=int(row.y))
        map_turtle.write(arg=f"{answer}", move=False, align='center', font=('Arial', 8, 'normal'))
        # TODO: 5.
        correct_guesses.append(answer)


# setup comparison logic
# def get_mouse_click_cords(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_cick_coor)
#
# turtle.mainloop()
# # replaces exitonclick()

screen.exitonclick()
