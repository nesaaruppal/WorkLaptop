from data import all_question_data
from quiz_classes import *

question_bank = []

for question in all_question_data:
    question_text = question["question"]
    question_answer = question["coreect_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
