from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move the ball to the new x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y= new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.goto(x=self.x_move, y=new_y)

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_x()