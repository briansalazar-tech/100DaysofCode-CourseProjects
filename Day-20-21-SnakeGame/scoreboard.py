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
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the text and rewrites score on screen with score value"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase score by 1 point"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)