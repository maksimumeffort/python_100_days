import tkinter
# mile to km converter


def calculate():
    given_miles = float(input_field.get())
    result = round(given_miles / 0.62137119)
    output.config(text=result)


screen = tkinter.Tk()
screen.title("Miles to Kms Converter")
screen.config(width=400, height=300, padx=30, pady=30)

input_field = tkinter.Entry(width=10)
input_field.grid(row=0, column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(row=1, column=0)

km = tkinter.Label(text="Km")
km.grid(row=1, column=2)

output = tkinter.Label(text="0")
output.grid(row=1, column=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

screen.mainloop()
