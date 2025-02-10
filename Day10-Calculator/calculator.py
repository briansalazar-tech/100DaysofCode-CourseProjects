# Program Walk through
# Ask for first number to calculate
# Ask for operation (+ - * /)
# Ask for second number
# Perform operation
# Display result
# Ask user to continue calculating by typing y, or n to start a new calculation


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
              }

print(operations["*"](4, 5))