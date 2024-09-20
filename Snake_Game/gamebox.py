from turtle import Turtle,Screen

class Box:
    def __init__(self):
        tim=Turtle()
        sc=Screen()
        tim.hideturtle()
        sc.tracer(0)
        tim.penup()
        tim.goto(-290,290)
        tim.pensize(5)
        tim.pendown()
        tim.goto(290,290)
        tim.goto(290,-290)
        tim.goto(-290,-290)
        tim.goto(-290,290)
        sc.update()
