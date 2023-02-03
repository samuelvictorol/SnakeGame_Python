from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.resetPosition()

    def resetPosition(self):
        random_x = random.randint(-280, 0)
        random_y = random.randint(-280, 0)
        self.goto(random_x, random_y)
