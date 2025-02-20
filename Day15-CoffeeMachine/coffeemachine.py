from art import logo
from menu import menu

MENU = menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Prints a report of current resources."""
    print("Current resources: ")
    for resource in resources:
        print(f"\t{resource.title()}: {resources[resource]}")
    print(f"\tMoney : ${money}")


def check_resources(drink_name):
    """Checks if the coffee machine has sufficient resources for the drink that is passed through."""
    make_drink = True
    drink = MENU[drink_name]["ingredients"]
    print(f"{drink_name.title()} selected...")
    for ingredient in drink:
        if resources[ingredient] >= drink[ingredient]:
            make_drink = True
        else:
            print(f"Sorry, there is not sufficient {ingredient}.")
            make_drink = False
    if make_drink == True:
        return True
    elif make_drink == False:
        print("Please try a different drink")
        return False


def subtract_resources(drink_name):
    """Update the quantity of resources in the coffee machine."""
    drink = MENU[drink_name]["ingredients"]
    for ingredient in drink:
        resources[ingredient] -= MENU[drink_name]["ingredients"][ingredient]


def add_resources():
    """Add additional resources to the coffee machine."""
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100
    print("Water, milk, and coffee replenished.")


def process_coins():
    """Asks user to enter money into the machine. Total value of coins is returned."""
    try:
        quarters = float(input("Please enter quarters ($0.25): ")) * 0.25
        dimes = float(input("Please enter dimes ($0.10): ")) * 0.10
        nickles = float(input("Please enter nickles ($0.05): ")) * 0.05
        pennies = float(input("Please enter pennies ($0.01): ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total
    
    except:
        return


money = 0
machine_on = True

while machine_on:
    print(logo)
    drink_to_make = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # User enters a drink
    if drink_to_make == "espresso"or drink_to_make == "latte" or drink_to_make == "cappuccino" or drink_to_make == "overkill":
        
        # Check if resources sufficient
        if check_resources(drink_to_make):
            print(f"A {drink_to_make} will cost ${MENU[drink_to_make]["cost"]}")
            try: 
                user_coins = process_coins()
                # Process coins & Check transaction success
                # Sufficient money entered
                if user_coins >= MENU[drink_to_make]["cost"]:
                    # User paid extra
                    if user_coins > MENU[drink_to_make]["cost"]:
                        change = user_coins - MENU[drink_to_make]["cost"]
                        rounded_change = "{:.2f}".format(change)
                        
                        print(f"Change due: ${rounded_change}")
                    # Transaction successful. Adjust resources
                    subtract_resources(drink_to_make)
                    money += MENU[drink_to_make]["cost"]
                    print(f"Enjoy your {drink_to_make}! ☕")

                # Insufficient money
                elif user_coins < MENU[drink_to_make]["cost"]:
                    print(f"Insufficient money entered. {drink_to_make.title()} costs ${MENU[drink_to_make]["cost"]}, you entered ${user_coins}")
            
            # Integer not entered
            except:
                print("Invalid entry. Please enter a valid quantity")
    
    elif drink_to_make == "report":
        report()

    elif drink_to_make == "add":
        add_resources()

    elif drink_to_make == "off" or drink_to_make == "exit":
        print("Goodbye")
        machine_on = False
    
    else:
        print("That is not a valid choice. Try again.")