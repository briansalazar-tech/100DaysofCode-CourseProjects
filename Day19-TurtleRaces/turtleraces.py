from turtle import Turtle, Screen

# Screen setup & prompt
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

starting_y = -150
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=starting_y)
    turtles.append(turtle)
    starting_y += 50


screen.exitonclick()