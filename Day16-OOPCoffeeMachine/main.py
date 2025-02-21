from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

on = "on"
# Opperate while on
while on == "on":
    # Ask user to enter drink
    drink_to_make = input(f"What would you like? ({menu.get_items()}): ").lower()
    
    # User types Off
    if drink_to_make == "off" or drink_to_make == "exit":
            print("Goodbye!")
            on = "off"

    # Check if a drink is selected
    elif menu.find_drink(drink_to_make):
        # Check if sufficient resources
        drink = menu.find_drink(drink_to_make)
        
        if coffee_machine.is_resource_sufficient(drink):
            
            try:
                # Ask User for Coins
                transaction = register.make_payment(drink.cost)
                
                # Transaction Successful
                if transaction:
                    # Make Drink
                    print(f"Enjoy your {drink_to_make} ☕")
            
            except:
                print("Invalid entry for money.")
        
        else:
            print("Insufficient resources... Please select another drink.")
    
    # User types report
    elif drink_to_make == "report":
        print("CURRENT RESOURCES AND CASH\n--------------------------")
        coffee_machine.report()
        register.report()
    
    # Add a drink to menu
    elif drink_to_make == "add":
        name = input("Enter new menu item's name: ").lower()
        water = int(input("Enter water quantity: "))
        milk = int(input("Enter milk quantity: "))
        cofee = int(input("Enter coffee quantity: "))
        cost = float(input("Enter the price of the new drink: $"))
        menu.menu.append(MenuItem(name="tea", water=100, milk=0, coffee=0, cost=1.00))