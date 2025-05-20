# Flask Intro
from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1> \
        <p>This is a paragraph</p> \
        <hr>' \
        '<p>This is the second paragraph</p>' # Using HTML tags

@app.route("/username/<username>") # Variable paths have <> around them
def greet(username):
    return f"Hello {username}!"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

if __name__ == "__main__": # Run flask app in debug mode. Makes it easier to reload web pages without closing the server
    app.run(debug=True)