from turtle import Turtle
INITIAL_SCORE = -1
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreValue = INITIAL_SCORE
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.addScore()
    
    def addScore(self):
        self.scoreValue += 1
        self.clear()
        self.write(f"Score = {self.scoreValue}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over !!", align=ALIGNMENT, font=FONT)