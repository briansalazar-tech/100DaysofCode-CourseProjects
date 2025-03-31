import pandas
from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
FOLDER_PATH = "./Day31-Capstone-FlashCardApp"

# Word Bank Data
CSV_DATA = pandas.read_csv(FOLDER_PATH + "/data/french_words.csv")
CSV_DICT = pandas.DataFrame.to_dict(CSV_DATA, orient="records")
# print(choice(csv_dict))


## FUNCTIONS ##
def next_card():
    """"""
    current_card = choice(CSV_DICT)
    print(current_card)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

## UI SETUP ##
# Window
window = Tk()
window.title("Flashy Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, borderwidth=0)

# Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file= FOLDER_PATH + "/images/card_front.png")
canvas.create_image(400, 263, image=card_image)
language_text = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text= "Word", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
incorrect_image = PhotoImage(file=FOLDER_PATH + "/images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_card)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_image = PhotoImage(file=FOLDER_PATH + "/images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=next_card)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()