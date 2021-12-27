import tkinter

# unlimited positional args with (*)
def add(*args):
    # args = tupple
    # print(args[0])
    return sum(args)
# add(3,4,5,6)

# unlimited keyword args with (**)
def calculate(**kwargs):
    pass
    # kwargs = dictionary
    # print(kwargs) => {multiply:3, add:5}
    print(kwargs["add"])  # => 5
# calculate(multiply = 3, add = 5)

def button_clicked(text="Output here"):
    my_label.config(text=f"{input.get()}")

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
# padding around edge of window
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="Label", foreground="white", font=("Arial", 20))
my_label.grid(column=0, row=0)
# important to show label on screen (pack, place/ grid) = geometry manager
# can't have more than 1 geomatry manager in one program
# padding around widget
my_label.config(padx=20, pady=20)


# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# New Button
new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()
