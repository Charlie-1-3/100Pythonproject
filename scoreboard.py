from turtle import Turtle

FONT = ("Courier", 20, "normal")
alignments = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=alignments, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align=alignments, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
