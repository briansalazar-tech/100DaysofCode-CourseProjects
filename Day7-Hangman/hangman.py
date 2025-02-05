from random import choice

word_list = ["aardvark", "baboon", "camel"]

#TODO 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
selected_word = choice(word_list)
print(selected_word)
#TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input("Guess a letter: ").lower()
print(user_guess)
#TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if user_guess in selected_word:
    print("letter in word")
else:
    print("Letter not in word")