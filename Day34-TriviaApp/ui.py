from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="./Day34-TriviaApp/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command="")
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./Day34-TriviaApp/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command="")
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()