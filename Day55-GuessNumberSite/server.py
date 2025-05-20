import random
from flask import Flask

app = Flask(__name__)

def align_center(function):
    """Center the text in the middle of the page"""
    def wrapper_function():
        return f"<div style='text-align: center; margin-top: 5rem'>{function()}</div>"
    return wrapper_function


random_number = random.randint(0, 9)
print(f"The random number is {random_number}") # For testing


@app.route('/')
@align_center
def home():
    return '<h1 style="color: blue">Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def guess_number(guess):
    # Check if to low
    if guess < random_number:
        return f'<div style="text-align: center; margin-top: 5rem"><h1 style="color: red">Oh no! Your guess was to low. The correct number was {random_number}!</h1> \
                 <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></div>'
    # Check if to high
    if guess > random_number:
        return f'<div style="text-align: center; margin-top: 5rem"><h1 style="color: purple">Oh no! Your guess was to high. The correct number was {random_number}!</h1> \
                 <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></div>'
    # check if correct
    if guess == random_number:
        return f'<div style="text-align: center; margin-top: 5rem"><h1 style="color: green">Correct! The number was {random_number}!</h1> \
                 <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></div>'


if __name__ == "__main__":
    app.run(debug=True)
