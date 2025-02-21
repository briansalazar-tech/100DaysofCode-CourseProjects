# Day 16: OOP Coffee Machine Project
##  Lesson Overview
Day 16 of the course introduces the concept of Object Oriented Programming (OOP). Whereas the previous coffee machine project used procedural programming to achieve the end goal. This lesson uses OOP to create a cleaner project and break the functionalities of the program into seperate components.

## Project
The project essentially achieves the same goals as the previous Coffee Machine Project from day 15. However, the functionality of this project is broken down into multiple files. Since the project is essentailly the same, I will not go into to much details as to how the program works. However, here is a breakdown of the functionality provided by the various files in the project.

### coffee_maker.py
**Coffee_maker.py** has a single function called **CoffeeMaker**. **CoffeeMaker** has an attribute called resources which contain the starting resources for the coffee machine.

Within the class there are three methods. The **report** method returns the values for the resources in the coffee machine. The **is_resource_sufficient** method is used to check if the coffee machine has sufficient resources to make the drink that the user specified. Finally, the **make_coffee** method is used to inform the user that their order was successfully made. Additionally, resources are subtracted from the coffee machine’s resources.

### menu.py
**Menu.py** has two classes -  **MenuItem** and **Menu**.

**MenuItem** is used to define individual items in the menu including the ingredients required and the cost of the menu item. The Menu class creates four default drinks – latte, espresso, cappuccino and overkill. However, MenuItem can be used to add new entries to the Menu.

**Menu** starts out by creating four drinks using the **MenuItem** class. The Menu class has two methods, the first being **get_items** which returns all the names of the available menu items. This method is used to inform the user what drink options are available. The second method **find_drink** is used to see if the drink the user entered is in the menu. If the drink is in the menu, the item is returned. If not, the user is informed that the drink is not available.

### money_machine.py
**Money_machine.py** has a single class called **MoneyMachine**. This class is used to handle cash transactions in the coffee machine project. **MoneyMachine** has three methods. **Report** is used to return the profit attribute when the user types report when prompted for a drink. **Process_coins** is used to ask the user to enter money into the machine. The quantities entered are then added up to return a total. The **make_payment** method uses the **process_coins** method to check if the user entered sufficient money. If the user entered more money than necessary, they are given change. If they do not enter sufficient money, they are informed that they need to enter more money.

### main.py
**Main.py** puts all the components of the project together and are where the program runs. For day 16, main.py accomplishes all of the same functionality of coffeemachine.py from day 15.