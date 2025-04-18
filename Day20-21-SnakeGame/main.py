import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
