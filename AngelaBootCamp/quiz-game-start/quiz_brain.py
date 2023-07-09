class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_text = self.question_list[self.question_number].text
        self.question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        print("Please answer in True/False:")
        self.user_response = input(f"Q.{self.question_number}: {self.question_text} : \t")
        self.check_answer()

    def check_answer(self):
        if self.user_response.lower() == self.question_answer.lower():
            print(f"Your answer: {self.user_response}")
            self.score += 1
        else:
            print("Wrong Answer")
        print(f"Correct Answer: {self.question_answer}")
        print(f"Current Score: {self.score} / {self.question_number} \n")
