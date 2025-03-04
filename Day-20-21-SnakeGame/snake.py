from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.starting_x = 0
        self.snake_body = []
        self.create_snake()
        
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
        self.snake_body[0].forward(MOVE_DISTANCE)