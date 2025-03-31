import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
FOLDER_PATH = "./Day31-Capstone-FlashCardApp"

## UI SETUP ##
# Window
window = Tk()
window.title("Flashy Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, borderwidth=0)

# Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file= FOLDER_PATH + "/Images/card_front.png")
canvas.create_image(400, 263, image=card_image)
language_text = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text= "Word", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
incorrect_image = PhotoImage(file=FOLDER_PATH + "/Images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_image = PhotoImage(file=FOLDER_PATH + "/Images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0)
correct_button.grid(column=1, row=1)

window.mainloop()