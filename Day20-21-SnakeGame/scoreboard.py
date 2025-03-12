from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the text and rewrites score on screen with score value. High score is read from data.txt file"""
        self.clear()
        # Read High Score from file - Day 24
        with open("./Day20-21-SnakeGame/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase score by 1 point"""
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the score to 0 and updates the high score if the current score is higher - Day 24"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./Day20-21-SnakeGame/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()