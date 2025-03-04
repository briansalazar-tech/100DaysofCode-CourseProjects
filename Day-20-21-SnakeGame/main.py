# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail
from snake import Snake
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()