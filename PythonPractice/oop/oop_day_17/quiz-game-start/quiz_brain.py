class QuestionBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0
    def next_question(self):
        if self.question_number < len(self.question_bank):
            current_question = self.question_bank[self.question_number]
            self.question_number += 1
            user_input = input(f'Q. {self.question_number}: {current_question.Question} (True/False)')
            final_answer = self.validate_answer(current_question,user_input)
        else:
            self.question_number += 1
            print('No questions left')

    def is_still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def validate_answer(self,current_question,user_input):
        if current_question.Answer == user_input:
            print('You got it right!')
            print(f'The correct answer is {user_input}')
            self.score += 1
            print(f'Your current score {self.score}/{self.question_number}')
        else:
            print('You got it Wrong. But keep trying!')
            print(f'The correct answer is {current_question.Answer}')
            print(f'Your current score {self.score}/{self.question_number}')
