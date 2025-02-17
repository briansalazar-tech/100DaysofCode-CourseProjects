# Import random, art and game data
from random import choice
from art import logo, vs
from game_data import data


# Initiate start
def play_game():
    """Main function to play the game. Function calls on the compare_followers function to check user's answer"""
    print(logo)
    if score > 0:
        print(f"Your current score is: {score}")
    # Assign person 1
    print(f"Compare A: {person1['name']}, {person1['description']}, from {person1['country']}")
    print(vs)
    # Assign person 2
    print(f"Against B: {person2['name']}, {person2['description']}, from {person2['country']}")
    # Prompt who has more followers
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return compare_followers(answer, person1, person2)
    

# Compare Followers
def compare_followers(answer, p1, p2):
    """Compares the follower counts of person 1 and person 2. If the user's answer is correct, then True is returned"""
    # If person1_more_followers is True, person1 has more followers. If false is returned, person2 has more followers
    person1_more_followers = p1['follower_count'] > p2['follower_count']
    if person1_more_followers and answer == 'a':
        print("Correct, person 1 has more followers and you guessed the right answer!")
        return True
    elif not person1_more_followers and answer == 'b':
        print("Correct, person 2 has more follwers and you guessed the right answer!")
        return True
    else:
        return False


score = 0
person1 = choice(data)
person2 = choice(data)
if person2 == person1:
    person2 = choice(data)

# Main game loop. If user's answer is incorrect, then game is ended.
while True:
    game = play_game()
    if game == True:
        score += 1
        person1 = person2
        person2 = choice(data)
        if person2 == person1:
            person2 = choice(data)
    else:
        print(f"Sorry, your answer is wrong!\nYour final score is: {score}")
        break
