from turtle import Turtle
FONT = ("Arial", 10, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", move=False, align="center", font=("Courier", 15, "italic"))


    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", move=False, align="center", font=FONT)

