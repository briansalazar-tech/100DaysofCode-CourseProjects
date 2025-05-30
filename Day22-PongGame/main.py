import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Net

screen = Screen()
screen.title("Python Pong Game")
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
net=Net()

screen.listen()
# Right paddle
screen.onkey(fun=r_paddle.move_up,key="Up")
screen.onkey(fun=r_paddle.move_down,key="Down")
# Left paddle
screen.onkey(fun=l_paddle.move_up,key="w")
screen.onkey(fun=l_paddle.move_down,key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall y=280 or y=-280
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    # Detect when left paddle misses
    if ball.xcor()< -380:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()