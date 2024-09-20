from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",80,"normal")
class Score:
    def __init__(self):
        self.tim=Turtle()
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.color("white")
        self.left_score = 0
        self.tim.goto(-100, 180)
        self.tim.write(self.left_score, align=ALIGN, font=FONT)
        self.tin=Turtle()
        self.tin.penup()
        self.tin.hideturtle()
        self.right_score = 0
        self.tin.color("white")
        self.tin.goto(100, 180)
        self.tin.write(self.right_score, align=ALIGN, font=FONT)
    def r_point(self):
        self.tin.clear()
        self.right_score += 1
        self.tin.write(self.right_score, align=ALIGN, font=FONT)
    def l_point(self):
        self.tim.clear()
        self.left_score += 1
        self.tim.write(self.left_score, align=ALIGN, font=FONT)
