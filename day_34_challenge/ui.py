from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
Q_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("MyQuiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score:", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.card = Canvas(width=300, height=250)
        self.card.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.card.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            font=Q_FONT,
            fill="grey"
        )

        t = PhotoImage(file="images/true.png")
        f = PhotoImage(file="images/false.png")
        self.t_button = Button(image=t, highlightthickness=0, command=self.click_true)
        self.t_button.grid(column=0, row=2)

        self.f_button = Button(image=f, highlightthickness=0, command=self.click_false)
        self.f_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.card.configure(bg="white")
        self.card.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question_text, text=q_text)
        else:
            self.card.itemconfig(self.question_text, text="You have reached the end of quiz")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")
    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.card.configure(bg="green")
            self.card.itemconfig(self.question_text, fill="white")
        else:
            self.card.configure(bg="red")
            self.card.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)




