# TODO: Move the snake
# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")


# TODO: Create a snake body
starting_x = 0
snake_body = []

for segment in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=starting_x,y=0)
    starting_x -= 20
    snake_body.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(snake_body) -1, 0, -1):
        new_x = snake_body[segment -1].xcor()
        new_y = snake_body[segment -1].ycor()
        snake_body[segment].goto(new_x, new_y)
    snake_body[0].forward(20)
screen.exitonclick()