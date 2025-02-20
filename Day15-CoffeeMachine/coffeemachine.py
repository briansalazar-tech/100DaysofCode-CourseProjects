MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "overkill": {
        "ingredients": {
            "water": 301,
            "milk": 201,
            "coffee": 101,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Prints a report of current resources."""

    print("Current resources: ")
    for resource in resources:
        print(f"\t{resource}: {resources[resource]}")
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
        print("Invalid entry. Please enter a valid quantity")
    
money = 0
machine_on = True

while machine_on:
    # TODO Prompt user for drink
    drink_to_make = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # print(drink_to_make)
    # Pass a drink
    if drink_to_make == "espresso"or drink_to_make == "latte" or drink_to_make == "cappuccino" or drink_to_make == "overkill":
        # TODO Check resources sufficient
        if check_resources(drink_to_make):
            print(f"A {drink_to_make} will cost ${MENU[drink_to_make]["cost"]}")
            try: 
                user_coins = process_coins()
                print(user_coins)
                # TODO Process coins & Check transaction success
                # Sufficient money entered
                if user_coins >= MENU["cappuccino"]["cost"]:
                    # User paid extra
                    if user_coins > MENU["cappuccino"]["cost"]:
                        change = user_coins - MENU["cappuccino"]["cost"]
                        rounded_change = "{:.2f}".format(change)
                        money += MENU["cappuccino"]["cost"]
                        print(f"Change due: {rounded_change}")

                        # Continue
                        print("Sufficient")
                        # TODO Make Coffee
                        subtract_resources(drink_to_make)
                        print(f"Enjoy your {drink_to_make}! ☕")

                # Insufficient money
                elif user_coins < MENU["cappuccino"]["cost"]:
                    print(f"Insufficient money entered. {drink_to_make.title()} costs ${MENU[drink_to_make]["cost"]}")
                
                print(f"Machine money: {money}")
            
            # Integer not entered
            except:
                continue
    
    # TODO Print report
    elif drink_to_make == "report":
        report()

    elif drink_to_make == "add":
        add_resources()
    
    # TODO Turn machine off
    elif drink_to_make == "off":
        print("Goodbye")
        machine_on = False
    
    else:
        print("That is not a valid choice. Try again.")



# TODO Make Coffee
# print(resources)
# subtract_resources("cappuccino")
# print("Drink has been made")
# print(resources)
# print("Adding resources")
# add_resources()
# print(resources)