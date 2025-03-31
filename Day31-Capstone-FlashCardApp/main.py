import pandas
from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
FOLDER_PATH = "./Day31-Capstone-FlashCardApp"
current_card = {}

# Word Bank Data
CSV_DATA = pandas.read_csv(FOLDER_PATH + "/data/french_words.csv")
try:
    with open(FOLDER_PATH + "/data/words_to_learn.csv", mode="r") as data:
        #print("Words_to_learn found")
        CSV_DATA = pandas.read_csv(FOLDER_PATH + "/data/words_to_learn.csv")
except:
    #print("words_to_learn.csv does not exist. Using starting french_words.csv")
    CSV_DATA = pandas.read_csv(FOLDER_PATH + "/data/french_words.csv")

CSV_DICT = pandas.DataFrame.to_dict(CSV_DATA, orient="records")
# print(choice(csv_dict))
print(len(CSV_DICT))



## FUNCTIONS ##
def next_card():
    """"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(CSV_DICT)
    #print(CSV_DICT[current_card])
    print(current_card)
    canvas.itemconfig(canvas_image, image=card_image_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)

def flip_card():
    """"""
    global current_card
    canvas.itemconfig(canvas_image, image=card_image_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def correct_answer():
    """"""
    CSV_DICT.remove(current_card)    
    print(len(CSV_DICT))
    next_card()

## UI SETUP ##
# Window
window = Tk()
window.title("Flashy Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, borderwidth=0)

flip_timer = window.after(3000, flip_card)

# Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image_front = PhotoImage(file= FOLDER_PATH + "/images/card_front.png")
card_image_back = PhotoImage(file= FOLDER_PATH + "/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_image_front)
language_text = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text= "Word", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
incorrect_image = PhotoImage(file=FOLDER_PATH + "/images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_card)
incorrect_button.grid(column=0, row=1)

# Correct Button
correct_image = PhotoImage(file=FOLDER_PATH + "/images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=correct_answer)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()

# Create new CSV of words to learn
words_to_learn_df = pandas.DataFrame(CSV_DICT)
words_to_learn_df.to_csv(FOLDER_PATH + "/data/words_to_learn.csv", index=False)
print("DF created")