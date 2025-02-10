from random import choice

choices = ["🪨", "📃", "✂️"]
user_wins = 0
computer_wins = 0

while True:
    if user_wins == 3 or computer_wins == 3:
        break
    
    computer_choice = choice(choices)
    user_input = input("First to three wins! Rock, Paper or Scissors? Type 1 for rock, 2 for paper, or 3 for scissors: ")
    
    # Verify valid input
    if user_input == "1" or user_input == "2" or user_input == "3":
        user_choice = choices[int(user_input) - 1]
        print(f"\nUser's choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}\n")
        
        # User Wins
        # User choice = Rock, computer choice = Scissors
        if user_choice == "🪨" and computer_choice == "✂️":
            print("🪨 beats 📃. You win!\n")
            user_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        # User choice = Paper,  compuputer choice = Rock
        elif user_choice == "📃" and computer_choice == "🪨":
            print("📃 beats 🪨. You win!\n")
            user_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        # User choice = Scissors ,computer choice = Paper
        elif user_choice == "✂️" and computer_choice == "📃":
            print("✂️ beats 📃. You win!\n")
            user_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        
        # Computer Wins
        # User choice = Scissors, computer choice = Scissors
        elif computer_choice == "🪨" and user_choice == "✂️":
            print("🪨 beats 📃. You lose!\n")
            computer_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        # User choice = Rock,  compuputer choice = Paper
        elif computer_choice == "📃" and user_choice == "🪨":
            print("📃 beats 🪨. You lose!\n")
            computer_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        # User choice = Paper ,computer choice = Scissors
        elif computer_choice == "✂️" and user_choice == "📃":
            print("✂️ beats 📃. You lose!\n")
            computer_wins += 1
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
        
        # Tie
        if computer_choice == user_choice:
            print(f"{user_choice} and {computer_choice}. Tie!\n")
            print(f"User wins: {user_wins}, Computer wins: {computer_wins}\n")
    
    else:
        print("Invalid input. Try again.")
print(f"\nFinal Score: \n\tUser wins: {user_wins}\n\tComputer wins: {computer_wins}")