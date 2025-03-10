from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self._update_level()

    def _update_level(self):
        """Updates the current level displayed on the screen"""
        self.goto(-280, 260)
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increase the current level by 1"""
        self.level += 1
        self._update_level()

    def game_over(self):
        """Displays a game over message on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)