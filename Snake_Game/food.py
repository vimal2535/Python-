import random
from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.color(randint(1, 255), randint(1, 255), randint(1, 255))
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
