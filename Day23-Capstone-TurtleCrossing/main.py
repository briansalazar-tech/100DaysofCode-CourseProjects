import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player.ycor() >= 280:
        player.level_up()
        scoreboard.level_up()

    if player.ycor() >= 0:
        scoreboard.game_over()
        game_is_on = False

    screen.update()

screen.exitonclick()
