import os
from random import choice
from art import logo, vs
from game_data import data


def clear_screen():
    """Clears the screen based on user's OS"""
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def unique_choice(p1):
    """Ensures that the second selection is not the same as the first selection"""
    
    p2 = choice(data)
    if p2 == p1:
        return choice(data)
    return p2


def play_game():
    """Main function to play the game. Function calls on the compare_followers function to check user's answer"""
    
    print(logo)
    if score > 0:
        print(f"Your current score is: {score}")
    print(f"Compare A: {person1['name']}, {person1['description']}, from {person1['country']}")
    print(vs)
    print(f"Against B: {person2['name']}, {person2['description']}, from {person2['country']}")
    # Prompt who has more followers. If choice is not valid, prompt user again
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    while answer != 'a' and answer != 'b':
        answer = input("Invalid input. Please type 'A' or 'B': ").lower()
    
    return compare_followers(answer, person1, person2)
    

def compare_followers(answer, p1, p2):
    """Compares the follower counts of person 1 and person 2. If the user's answer is correct, then True is returned"""
    
    # If person1_more_followers is True, person1 has more followers. If false is returned, person2 has more followers
    person1_more_followers = p1['follower_count'] > p2['follower_count']
    
    # Check if user's answer is correct
    if person1_more_followers and answer == 'a':
        clear_screen()
        print(f"Correct, {p1['name']} has more followers and you guessed the right answer!")
        return True
    elif not person1_more_followers and answer == 'b':
        clear_screen()
        print(f"Correct, {p2['name']} has more follwers and you guessed the right answer!")
        return True
    else:
        clear_screen()
        return False


score = 0
person1 = choice(data)
person2 = unique_choice(person1)


keep_playing = True
while keep_playing:
    current_game = True
    while current_game:
        game = play_game()
        if game == True:
            score += 1
            person1 = person2
            person2 = unique_choice(person1)

        else:
            print(f"Sorry, your answer is wrong!\nYour final score is: {score}\n")
            current_game = False
            play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again[0] == 'y':
                clear_screen()
                score = 0
                person1 = choice(data)
                person2 = unique_choice(person1)

            else:
                keep_playing = False
                clear_screen()
                print("Goodbye!")
                break