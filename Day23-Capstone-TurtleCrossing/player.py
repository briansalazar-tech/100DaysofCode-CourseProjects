from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the turtle forward by the specified MOVE_DISTANCE"""
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        """Returns the turtle back to the STARTING_POSITION withen FINISH_LINE_Y is crossed"""
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
