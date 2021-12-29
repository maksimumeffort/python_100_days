from tkinter import *
from random import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
word_pair = {}
# ------------------------DATA_MANAGER------------------------- #

try:
    with open("data/words_to_learn.csv") as data_file:
        data = pandas.read_csv(data_file)
        data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    with open("data/french_words.csv") as data_file:
        original_data = pandas.read_csv(data_file)
        data_dict = original_data.to_dict(orient="records")


# --------------------------FUNCTIONS-------------------------- #


def flip_card():
    global word_pair
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_bg, image=card_back_img)
    card.itemconfig(card_word, text=word_pair["English"], fill="white")


def generate_word():
    global word_pair, timer
    screen.after_cancel(timer)
    word_pair = choice(data_dict)
    card.itemconfig(card_bg, image=card_front_img)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=word_pair["French"], fill="black")
    timer = screen.after(3000, flip_card)


def know():
    # find out how .remove() works
    data_dict.remove(word_pair)
    words_df = pandas.DataFrame(data_dict)
    words_df.to_csv("data/words_to_learn.csv", index=False, mode="w")
    generate_word()


def not_know():
    generate_word()

# ----------------------------GUI------------------------------ #


screen = Tk()
screen.title("Flash Card App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = screen.after(3000, flip_card)
# ----------------------------Cards---------------------------- #

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card = Canvas()
card.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = card.create_image(400, 263, image=card_front_img)
card.grid(row=0, column=0, columnspan=2)
# ----------------------------Text--------------------------- #

card_title = card.create_text(400, 150, text="", font=LANG_FONT)
card_word = card.create_text(400, 263, text="", font=WORD_FONT)

# ----------------------------Buttons--------------------------- #
no_img = PhotoImage(file="images/wrong.png")
yes_img = PhotoImage(file="images/right.png")

no_button = Button(image=no_img, bd=0, highlightthickness=0, command=not_know)
no_button.grid(row=1, column=0)

yes_button = Button(image=yes_img, bd=0, highlightthickness=0, command=know)
yes_button.grid(row=1, column=1)

generate_word()

screen.mainloop()
