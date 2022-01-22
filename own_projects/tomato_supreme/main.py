from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
ticks = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    counter.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    # global ticks
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
        # ticks += 1
        # counter.config(text=CHECK*ticks)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    # global ticks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # using dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            marks += CHECK
        counter.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Top Row
timer_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# Mid Row
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Row Below
start = Button(text="Start", width=1, highlightbackground=YELLOW, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", width=1, highlightbackground=YELLOW, command=reset_timer)
reset.grid(row=2, column=2)

# Bottom Row
counter = Label(bg=YELLOW, fg=GREEN)
counter.grid(row=3, column=1)


window.mainloop()
