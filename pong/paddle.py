from turtle import Turtle

POSITION = [(360, 0), (-360, 0)]


class Paddle:
    def __init__(self):
        self.total = []
        for i in range(len(POSITION)):
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.shapesize(stretch_wid=5, stretch_len=1)
            tim.penup()
            tim.goto(POSITION[i])
            self.total.append(tim)

    def right_up(self):
        if self.total[0].ycor() < 241:
            x_cor = self.total[0].xcor()
            y_cor = self.total[0].ycor() + 20
            self.total[0].goto(x_cor, y_cor)
    def right_down(self):
        if self.total[0].ycor() > -225:
            x_cor = self.total[0].xcor()
            y_cor = self.total[0].ycor() - 20
            self.total[0].goto(x_cor, y_cor)

    def left_up(self):
        if self.total[1].ycor() < 241:
            x_cor = self.total[1].xcor()
            y_cor = self.total[1].ycor() + 20
            self.total[1].goto(x_cor, y_cor)
    def left_down(self):
        if self.total[1].ycor() > -225:
            x_cor = self.total[1].xcor()
            y_cor = self.total[1].ycor() - 20
            self.total[1].goto(x_cor, y_cor)
