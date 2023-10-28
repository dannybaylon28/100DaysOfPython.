from turtle import Turtle
from car_manager import CarManager
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"SCORE:{self.level}", False, "Center", FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align="center", font=("Arial", 24, "normal"))



