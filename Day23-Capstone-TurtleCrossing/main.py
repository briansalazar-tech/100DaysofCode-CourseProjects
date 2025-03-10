import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    cars.move_cars()

    if player.ycor() >= 280:
        player.level_up()
        scoreboard.level_up()
        cars.increase_speed()
        # Add a new car to the list of cars every other time the level is increased
        if scoreboard.level % 2 == 0:
            cars.create_car()

    # Game ends if the player collides with a car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()
