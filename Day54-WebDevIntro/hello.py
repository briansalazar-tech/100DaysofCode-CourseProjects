# Flask Intro
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bye')
def say_bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)

# Decorators - Give function additional functionality/modify functionality
# import time


# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
    
# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")


# def say_greeting():
#     print("Greeting")

# say_hello()
# say_bye()

# # Accomplishes the same as having the @ above the function
# decorated = delay_decorator(say_greeting)
# decorated()