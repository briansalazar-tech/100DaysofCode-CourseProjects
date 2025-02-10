import os
from art import logo

entrants = {}
highest_bidder = ""
highest_bid = 0


def clear_screen():
        """Clears the screen based on users OS."""
    # Clear screen for Windows
        if os.name == "nt":
            os.system("cls")
            print(logo)
        # Clear screen for Mac/Linux
        else:
            os.system("clear")
            print(logo)
while True:
    print(logo)
    print("Welcome to the secret auction program.")
    
    still_bidding = True
    while still_bidding:
        # Ask for name - Dictionary key
        entry = input("What is your name?: ")
        # Ask for bid - Dictionary value
        bid = float(input("What is your bid?: $"))
        # Ask if other bidder?
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        # Add name and bid to dictionary
        entrants[entry] = bid

        # If yes, clear screen and repeat process above
        if other_bidders == "yes":
            clear_screen()
        else:
            clear_screen()
            still_bidding = False

    # After all bids submitted, check who has submitted the highest bid and declair winner
    for key in entrants:
        if entrants[key] > highest_bid:
            highest_bidder = key
            highest_bid = entrants[key]

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")
    
    new_auction = input("Would you like to start a new auction? Type 'yes' or 'no'. ").lower()
    if new_auction == "yes":
        clear_screen()
        highest_bidder = ""
        highest_bid = 0
        entrants = {}
        still_bidding = True
    else:
        print("Goodbye!")
        break