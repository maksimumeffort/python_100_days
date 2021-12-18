class QuizBrain:
    def __init__(self, list):
        self.question_list = list
        self.question_number = 0
        self.score = 0

    # TODO: 1. ask questions
    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q{self.question_number}. {current_q.text} True or False?: ")
        self.check_answer(user_choice, current_q.answer)

    # TODO: 2. check if answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


    # TODO: 3. check if end of quiz
    def still_has_questions(self):
        """returns boolean"""
        return self.question_number < len(self.question_list)






"""
    quiz brain class
attributes:
    question_number
    question_list
methods:
    next_question
"""