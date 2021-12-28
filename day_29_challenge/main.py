from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# inputs
input_row_num = 1
for l in labels[:2:]:
    l = Entry(width=35)
    l.grid(column=1, row=input_row_num, columnspan=2)
    input_row_num += 1
password_input = Entry(width=21)
password_input.grid(column=1, row=input_row_num, columnspan=1)

# buttons
generate_button = Button(width=10, text="Generate Password")
generate_button.grid(column=2, row=3, columnspan=1)

add_button = Button(width=33)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()
