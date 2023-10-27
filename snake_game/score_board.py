from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def count_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", align="center", font=("Arial", 24, "normal"))
















