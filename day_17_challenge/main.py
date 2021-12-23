# setup code

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO: 1. create question bank
question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")