import random
from turtle import Turtle, Screen

# Screen setup & prompt
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Starting variables
starting_y = -150
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_race_on = False

# Generate turtles
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=starting_y)
    turtles.append(turtle)
    starting_y += 50

if user_bet:
    is_race_on = True

# Turtle race. Race ends when a turtle crosses the xcor specified.
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner! 🎉 ")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()