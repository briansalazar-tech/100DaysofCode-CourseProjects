import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.10
        self.starting_bounce()

    def starting_bounce(self):
        """Randomizes the direction the ball will start moving at the start of the game"""
        direction = [1, -1]
        self.x_move = 10 * random.choice(direction)
        self.y_move = 10 * random.choice(direction)

    def move(self):
        """Move the ball to the new x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y= new_y)

    def bounce_y(self):
        """Inverts the value of y_move"""
        self.y_move *= -1

    def bounce_x(self):
        """Inverts the value of x_move"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        """Resets the ball to the center of the screen, movement speed and changes the direction of bounce_x"""
        self.goto(0,0)
        self.move_speed = 0.10
        self.bounce_x()