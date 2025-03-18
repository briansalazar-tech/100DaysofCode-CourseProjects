# Day 26: NATO Phonetic Alphabet Challenge
## Lesson Overview
Day 26 introduced the concepts of working with **list** and **dictionary comprehensions**. The lesson provided plenty of exercises first with list comprehensions, and then with dictionary comprehensions. After completing the practice exercises, the lesson proceeded to the Day 26 challenge of creating a list of NATO alphanumeric values from a word that a user passes. 
## Project
This day’s challenge is fairly easy. In fact, the final code only needed six lines of code. This is in part due to the use of list and dictionary comprehensions. If comprehensions were not used, many more lines of code would have been needed to achieve the end goal of this challenge.

The challenge first starts by reading the **nato_phonetic_alphabet.csv** file using pandas. After reading the CSV, a dictionary comprehension is used to create a dictionary from the letters and alphabet codes.

The user is then prompted to enter a word. This word is then passed through a list comprehension to create a list of alphabet code words and is returned in the terminal.
