import pandas

# Create a dictionary from the nato_phonetic_alphabet.csv file
nato_alphabet = pandas.read_csv("./Day26-NATOAlphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# Prompt user for a word and create a list from the letters in the word using the NATO phonetic alphabet
word = input("Enter a word: ")
word_list = [nato_dict[letter] for letter in word.upper()]
print(word_list)