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

money = 0
machine_on = True

while machine_on:
    # Prompt user for drink
    drink_to_make = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(drink_to_make)
    # Print report
    if drink_to_make == "report":
        report()
    # Turn machine off
    elif drink_to_make == "off":
        print("Goodbye")
        machine_on = False