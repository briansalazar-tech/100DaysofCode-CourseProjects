import os
from art import logo
from random import choice

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []
user_score = 0
dealer_score = 0


def clear_screen():
    """Clears the screen based on user's OS"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def deal_card():
    """Deals a single card to a user"""
    return choice(CARDS)


def game_setup():
    """Adds two cards to user and dealers hands and calculates the starting scores"""
    global user_score, dealer_score
    print(f"{logo}\nLet's play Blackjack!")
    for card in range(2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())
    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)
    print(f"\nYour hand: {user_hand}, current score: {user_score}")
    print(f"Dealer's first card is: {dealer_hand[0]}")
    

# Start game (or exit)
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Initialize game
if play_game == "y":
    game_setup()
elif play_game == "n":
    clear_screen()
    print("Goodbye!")
else:
    print("Invalid input. Goodbye!")

game_on = True
while game_on and play_game == "y":
    
    # Users turn
    user_turn = True
    while user_turn and game_on:
        draw_card = input("\nDo you want to draw another card? Type 'y' or 'n': ")
        if draw_card == "y":
            user_hand.append(deal_card())
            user_score = sum(user_hand)
        # Check if user has 11 in hand and over 21
        if 11 in user_hand and user_score > 21:
            user_hand.remove(11)
            user_hand.append(1)
            user_score = sum(user_hand)
        print(f"\nYour hand: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card is: {dealer_hand[0]}")
        # Check if user busts
        if user_score > 21:
            print(f"\nYour final hand: {user_hand}, final score: {user_score}")
            print("\tYou went over 21, you lose! 🥲")
            user_turn = False
            game_on = False
        # End user turn
        if draw_card == "n":
            print("\nDealer's Turn...")
            user_turn = False
            
    # Dealers turn
    dealer_turn = True
    while dealer_turn and game_on:
        while dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = sum(dealer_hand)
            if 11 in dealer_hand and dealer_score > 21:
                dealer_hand.remove(11)
                dealer_hand.append(1)
                dealer_score = sum(dealer_hand)
        if dealer_score >= 17:
            print(f"\nYour final hand: {user_hand}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
            dealer_turn = False
    
    # Compare scores and determine winner
    if game_on:
        if dealer_score > 21:
            print("\tDealer busts! You win! 🎉")
        elif user_score > dealer_score:
            print("\tYou win! 🎉")
        elif user_score < dealer_score:
            print("\tYou lose! 🥲")
        elif user_score == dealer_score:
            print("\tIt is a draw! 🙅‍♂️")
    
    # Restart game or exit
    play_again = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == "y":
        game_on = True
        user_turn = True
        dealer_turn = True
        user_hand = []
        dealer_hand = []
        dealer_score = 0
        user_score = 0
        clear_screen()
        game_setup()
    else:
        clear_screen()
        print("Thanks for playing!")
        game_on = False