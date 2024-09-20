from turtle import Turtle
class Object:
    def __init__(self):
        self.tim = Turtle("turtle")
        self.tim.penup()
        self.tim.goto(0,-280)
        self.tim.setheading(90)
    def move(self):
        xcor = self.tim.xcor()
        ycor = self.tim.ycor() + 20
        self.tim.goto(xcor,ycor)
    def level(self):
        self.level=1
        self.sco = Turtle()
        self.sco.penup()
        self.sco.goto(-240, 270)
        self.sco.hideturtle()
        self.sco.write("Level: "+str(self.level),align="center",font=("Arial",15,"normal"))
    def next_level(self):
        self.tim.goto(0,-280)
        self.sco.clear()
        self.level+=1
        self.sco.write("Level: " + str(self.level), align="center", font=("Arial", 15, "normal"))
