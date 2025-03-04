from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.starting_x = 0
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        """Generates 3 segments for the starting snake body"""
        for segment in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=self.starting_x, y =0)
            self.starting_x -= 20
            self.snake_body.append(snake)

    def move(self):
        """Moves the segments in the snake body to the previous position of the leading segment"""
        for segment in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[segment -1].xcor()
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets the heading north"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets the heading south"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets the heading west"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets the heading east"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)