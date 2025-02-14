import random
from art import logo


def number_guessing_game():
    """Number guessing game. Random number is selected between 1 and 100. User has 5 or 10 attempts to guess the number."""

    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    # Generate a random number
    random_number = random.randint(1, 100)
    print(f"For Testing... the correct number is: {random_number}")
    # Chose dificulty - hard (5) or easy (10)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attempts remaining to guess the nummber.")

    while lives > 0:
        # Ask user to make a guess
        user_guess = int(input("Make a guess: "))
        # Check users guess. User guess to high. -1 life
        if user_guess > random_number:
            print("To high\nGuess again.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the nummber.")
            if lives == 0:
                print("You have run out of guesses, you lose.")
                break
        # Check users guess. User guess to low -1 life
        elif user_guess < random_number:
            print("To low\nGuess again.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the nummber.")
            if lives == 0:
                print("You have run out of guesses, you lose.")
                break
        # Check users guess. User guess correct user wins
        elif user_guess == random_number:
            print(f"Congratulations! You guessed the correct number!\nYour guess: {user_guess}\nCorrect number: {random_number}")
            break


while True:
    number_guessing_game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == "n":
        print("Goodbye!")
        break