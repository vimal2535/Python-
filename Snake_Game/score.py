from turtle import Turtle
from time import sleep
FONT= ("Arial",15,"normal")
ALIGN = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor=0
        with open("high_score.txt", mode="r") as fill:
            self.high_score = int(fill.read())
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.write(f"SCORE:{self.scor} HIGH SCORE:{self.high_score}", False, align=ALIGN,font=FONT)
    def point(self):
        self.clear()
        self.scor += 1
        self.goto(0, 290)
        self.write(f"SCORE:{self.scor} HIGH SCORE:{self.high_score}", False, align=ALIGN, font=FONT)

    def end(self):
        self.clear()
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        if self.scor > int(self.high_score):
            with open("high_score.txt","w") as new:
                new.write(str(self.scor))
            with open("high_score.txt") as final:
                self.high_score = int(final.read())
        self.scor=0
        self.color("black")
        self.goto(0,290)
        self.write(f"SCORE:{self.scor} HIGH SCORE:{self.high_score}", False, align=ALIGN, font=FONT)
