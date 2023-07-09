from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(question_data)):
    quest_obj = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(quest_obj)

quiz_obj = QuizBrain(question_bank)
quiz_obj.next_question()

while quiz_obj.still_has_question():
    quiz_obj.next_question()

print(f"Final Score: {quiz_obj.score}")