from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question = Question(text=question, answer=answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()