from turtle import Turtle
FONT= ("Arial",15,"normal")
ALIGN = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor=0
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.write("SCORE: " + str(self.scor), False, align=ALIGN,font= FONT)
    def point(self):
        self.clear()
        self.scor += 1
        self.write("SCORE: " + str(self.scor), False, align=ALIGN,font=FONT)
    def end(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER!",move=False,align=ALIGN,font=FONT)