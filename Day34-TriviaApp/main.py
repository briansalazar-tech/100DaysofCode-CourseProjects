from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Loads questions into quiz brain
quiz = QuizBrain(question_bank)
# Loads quiz brain into UI
quiz_ui = QuizInterface(quiz)

print("Program closed")