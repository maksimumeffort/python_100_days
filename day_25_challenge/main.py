import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# database setup
db = pandas.read_csv("50_states.csv")
states_array = db.state.to_list()

# setup map turtle
map_turtle = turtle.Turtle()
correct_guesses = []

# set up input field
# print(states_array)

# TODO: 4.
while len(correct_guesses) < 50:
    # TODO: 1 & 6
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state name?").title()
    # TODO: 2.
    if answer == "Exit":
        missing_states = [state for state in states_array if state not in correct_guesses]
        """
        or
        # for state in states_array:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        """
        break
    if answer in states_array:
        # TODO: 3.
        row = db[db.state == answer]
        map_turtle.hideturtle()
        map_turtle.penup()
        map_turtle.goto(x=int(row.x), y=int(row.y))
        map_turtle.write(arg=f"{answer}", move=False, align='center', font=('Arial', 8, 'normal'))
        # TODO: 5.
        correct_guesses.append(answer)

missing_states_dict = {
    "states": missing_states
}

df = pandas.DataFrame(missing_states_dict)
df.to_csv("states_to_learn.csv")


# setup comparison logic
# def get_mouse_click_cords(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_cick_coor)
#
# turtle.mainloop()
# # replaces exitonclick()

