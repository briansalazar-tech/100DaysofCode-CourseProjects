import os
from art import logo
from random import choice

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []
user_score = 0
dealer_score = 0

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def deal_card():
    return choice(CARDS)


# Start game (or quit)

# play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# while play_game == "y":
#     print(logo)
#     print("Let's play Blackjack!")
#     play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     clear_screen()
# print("Goodbye!")


# Deal cards to user and dealer
for card in range(2):
    user_hand.append(deal_card())
    dealer_hand.append(deal_card())
user_score = sum(user_hand)
dealer_score = sum(dealer_hand)

print(f"Your hand: {user_hand}, current score: {user_score}")
print(f"Dealer's first card is: {dealer_hand[0]}")

# Users turn
# user_turn = True
# while user_turn:
#     # user_hand = [12, 2, 10] ## Test hand
#     user_hand.append(deal_card())
#     user_score = sum(user_hand)
#     draw_card = input("\nDo you want to draw another card? Type 'y' or 'n': ")
#     # Check if user has 11 in hand and over 21
#     if 11 in user_hand and user_score > 21:
#         user_hand.remove(11)
#         user_hand.append(1)
#         user_score = sum(user_hand)
#         print(user_hand)
#         print(user_score)
#     print(f"\nYour hand: {user_hand}, current score: {user_score}")
#     print(f"Dealer's first card is: {dealer_hand[0]}")
#     # Check if user busts
#     if user_score > 21:
#         print(f"\nYour final hand: {user_hand}, final score: {user_score}")
#         print("You went over 21, you lose!")
#         user_turn = False
#         # Do not proceed to dealer turn if busts
#     # End user turn
#     if draw_card == "n":
#         print("Dealer's Turn")
#         user_turn = False
        
# Dealers turn
dealer_turn = True
while dealer_turn:
    print(dealer_score)
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = sum(dealer_hand)
        if 11 in dealer_hand and dealer_score > 21:
            dealer_hand.remove(11)
            dealer_hand.append(1)
            dealer_score = sum(dealer_hand)
    if dealer_score >= 17:
        print(dealer_hand)
        print(dealer_score)
        dealer_turn = False

# Compare scores and determine winner