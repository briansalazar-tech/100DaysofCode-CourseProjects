import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
STARTING_Y = [-230, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
STARTING_X = [300, 350, 400, 450, 500, 550, 600, 650, 700]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(random.choice(STARTING_X), random.choice(STARTING_Y))

class CarManager:
    
    def __init__(self):
        """Creates 15 cars to start out the game and appends them to the all_cars list. CarManager will be used to control the movement of the cars in the all_cars list"""
        self.all_cars = []
        for car in range(15):
            self.create_car()

    def create_car(self):
        """Creates a single car and appends it to the all_cars_list"""
        new_car = Car()
        self.all_cars.append(new_car)
        print(len(self.all_cars))

    def move_cars(self):
        """Moves the cars in the all_cars list to the left. Once a car reaches the left side of the screen, it is respawned off screen on the right side"""
        for car in self.all_cars:
            if car.xcor() < -300:
                car.goto(random.choice(STARTING_X), random.choice(STARTING_Y))
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        """Increase the speed of the cars by the specieid MOVE_INCREMENT value"""
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT