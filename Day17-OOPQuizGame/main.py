from question_model import Question
from data import question_data

question_bank = []
print(f"Length of question bank = {len(question_bank)}")
# for item in question_data:
#     for entry in item:
#         q = item["text"]
#         a = item["answer"]
#         print(f"Question: {q}\nAnswer: {a}")
#     print("Next question")

for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question = Question(text=question, answer=answer)
    question_bank.append(question)

print(f"Length of question bank = {len(question_bank)}")