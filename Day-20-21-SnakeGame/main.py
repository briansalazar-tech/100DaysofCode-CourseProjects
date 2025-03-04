# TODO: Move the snake
# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

# TODO: Create a snake body
starting_x = 0
snake_body = []
for segment in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x=starting_x,y=0)
    starting_x -= 20
    snake_body.append(segment)


screen.exitonclick()