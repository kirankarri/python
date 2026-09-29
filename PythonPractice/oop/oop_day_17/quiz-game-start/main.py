from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain
from turtle import Turtle

question_bank = []
timmy = Turtle()
for i in range(len(question_data)):
    q = Question(question_data[i]['text'],question_data[i]['answer'])
    question_bank.append(q)
quiz_brain = QuestionBrain(question_bank)
while quiz_brain.is_still_has_questions():
    quiz_brain.next_question()



