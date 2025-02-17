# Import random, art and game data
from random import choice
from art import logo, vs
from game_data import data

score = 0
person1 = choice(data)
person2 = choice(data)

# Initiate start
print(logo)
# Assign person 1
print(f"Compare A: {person1['name']}, {person1['description']}, from {person1['country']}")
print(vs)
# Assign person 2
print(f"Against B: {person2['name']}, {person2['description']}, from {person2['country']}")
# Prompt who has more followers
answer = input("Who has more followers? Type 'A' or 'B': ").lower()

# Compare
# print(person1['follower_count'])
# print(person2['follower_count'])

# Followrese correct?, if yes score + 1, person 2 = person 1, assign new person 2

# Incorrect, end game