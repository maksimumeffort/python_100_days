from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
EMAIL = "alexmaksimets@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    key_letters = [choice(letters) for _ in range(randint(8, 10))]

    key_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    key_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = key_letters + key_symbols + key_number
    shuffle(password_list)

    password_input.delete(0, END)
    password_input.insert(0, "".join(password_list))
    pyperclip.copy("".join(password_list))
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Entered: \nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


screen = Tk()
screen.title("Password Manager")
screen.config(pady=50, padx=50)
labels = ["Website:", "Email/Username:", "Password:"]

# canvas
logo_canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

# labels
label_row_num = 1
for l in labels:
    l = Label(text=f"{l}")
    l.grid(column=0, row=label_row_num)
    label_row_num += 1

# variables
website = StringVar()
email = StringVar()
password = StringVar()

# inputs
website_input = Entry(screen, width=35, textvariable=website)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(screen, width=35, textvariable=email)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, EMAIL)

password_input = Entry(screen, width=21, textvariable=password)
password_input.grid(column=1, row=3)

# buttons
generate_button = Button(width=10, text="Generate Key", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=33, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()
