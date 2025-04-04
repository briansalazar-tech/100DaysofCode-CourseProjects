import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None


    def still_has_questions(self):
        """Checks if current question number is less than the list of questions (10)"""
        return self.question_number < len(self.question_list)


    def next_question(self):
        """Loads the next question from the list of questions and increments question number by 1"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        print(f"Question: {self.question_number}")
        return f"Q{self.question_number}: {q_text} (True/False): "


    def check_answer(self, user_answer):
        """Checks if the answer is correct"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():

            print("Correct")
            return True
        else:
            print("Incorrect")
            return False

