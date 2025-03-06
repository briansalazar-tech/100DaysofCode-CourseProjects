# TODO Create another padle
# TODO Create the ball and make it move
# TODO Detect collision with wall and bounce
# TODO Detect collision with paddle
# TODO Detect when paddle misses
# TODO Keep Score

import time
from turtle import Screen, Turtle
from paddle import Paddle

# TODO Create Screen height-600 width-800
screen = Screen()
screen.title("Python Pong Game")
screen.setup(width=800 ,height=600)
screen.bgcolor("black")
screen.tracer(0)

# # TODO Create and move a paddle
# paddle = Turtle("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(x=350, y=0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# def move_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(x=paddle.xcor(), y=new_y)


# def move_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(x=paddle.xcor(), y=new_y)

screen.listen()
# Right paddle
screen.onkey(fun=r_paddle.move_up,key="Up")
screen.onkey(fun=r_paddle.move_down,key="Down")
# Left paddle
screen.onkey(fun=l_paddle.move_up,key="w")
screen.onkey(fun=l_paddle.move_down,key="s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()