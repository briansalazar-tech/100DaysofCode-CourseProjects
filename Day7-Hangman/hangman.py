from random import choice
from art import logo, stages
from wordlist import word_list

lives = 6

# Select random word from word_list
selected_word = choice(word_list)
print(selected_word)

# Generate placeholder with same number of letters as selected word
correct_guesses = []
guessed_letters = []
for letter in selected_word:
    correct_guesses += "_"

display_guessed_word = " ".join(correct_guesses)

print(logo)
# print(f"***** Total Lives: {lives} *****")
print(display_guessed_word)

game_over = False
while game_over == False:
    print(stages[lives])
    print(f"***** Lives remaining: {lives} *****")
    # Check if all letters have been guessed prior to asking user to guess a letter
    if "_" not in correct_guesses:
        print("You win!")
        game_over = True
    # Check is user has lives remaining
    elif lives == 0:
        print(f"You lose!\nThe correct word was {selected_word}")
        game_over = True
    
    else:    
        # Prompt user to guess a letter
        user_guess = input("Guess a letter: ").lower()
        
        # Check if user has previously guessed the letter. Player not penalized
        if user_guess in guessed_letters:
            print(f"You've already guessed {user_guess}. Try again.")
            continue
        else:
            guessed_letters.append(user_guess)

        # Check if user guess matches letter in selected word
        for index in range(len(selected_word)):
            if user_guess == selected_word[index]:
                correct_guesses[index] = user_guess
        
        if user_guess not in selected_word:
            print(f"Incorrect Letter! {user_guess} is not in the word.")
            lives -= 1
            
        
        display_guessed_word = " ".join(correct_guesses)
    print(display_guessed_word)