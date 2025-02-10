from art import logo

previous_result = 0


def add(num1, num2):
    """Add two numbers together and return output"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers together and return output"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers together and return output"""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers together and return output"""
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
              }

print(logo)

while True:
    # First number to calculate
    if previous_result == 0:
        first_number = float(input("Enter first number: "))
    else:
        first_number = previous_result

    # Operation to perform
    for option in operations:
        print(option)
    operation = input("Enter operation to perform: ")
    # Second number to calculate
    second_number = float(input("Enter second number: "))
    # Perform operation
    result = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")

    # Continue calculating or exit
    continue_calculating = input("Type 'y' to continue with previous result.\nType 'n' to start a new calculation.\nType 'e' to exit.\n").lower()
    if continue_calculating[0] == "y":
        previous_result = result # Save previous result to be used as first number
        print("--------------------\nPrevious result: ", previous_result)
    elif continue_calculating[0] =="n":
        previous_result = 0
        print("--------------------")
    elif continue_calculating[0] == "e":
        print("--------------------\nGoodbye!")
        break
    else:
        print("--------------------\nInvalid input. Exiting...")
        break