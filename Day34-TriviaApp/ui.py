from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # Required to use QuizBrain
        self.quiz = quiz_brain
        # Window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Score label
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # Current Question canvas
        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="Question", font=("Arial", 20, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # True button
        self.true_image = PhotoImage(file="./Day34-TriviaApp/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        # False button
        self.false_image = PhotoImage(file="./Day34-TriviaApp/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        """Gets the next question from quiz brain and displays it in the UI. If there are no more questions, buttons are disabled"""
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        """Checks if the True button is pressed. If answer is correct, score increased by 1"""
        answer_check = self.quiz.check_answer("True")
        if answer_check:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.give_feedback(answer_check)


    def false_pressed(self):
        """Checks if the False button is pressed. If answer is correct, score increased by 1"""
        answer_check = self.quiz.check_answer("False")
        if answer_check:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.give_feedback(answer_check)


    def give_feedback(self, is_right):
        """Change the background of the canvas based on if the aanswer provd by the user is correct or not"""
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        