import turtle
from turtle import Turtle
import random
RANK=random.randint(0, 220)
RAN = random.randint(-280, 280)
SNAKERAN = random.randint(0, 255)
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
SNAKE_SPEED = 15
POSITION = [(0, 0), (-20, 0), (-40, 0)]
SCORE=0
class Snake:
    def __init__(self):
        self.total= []
        for i in POSITION:
            tim = Turtle("circle")
            tim.color("black")
            tim.penup()
            tim.goto(i)
            self.total.append(tim)
        self.head = self.total[0]
    def new(self):
        tim = Turtle("circle")
        tim.color("black")
        tim.penup()
        tim.speed("fastest")
        last_position = self.total[-1].position()
        tim.goto(last_position)
        self.total.append(tim)


    def move(self):
        for seg in range(len(self.total) - 1, 0, -1):
            xcor = self.total[seg - 1].xcor()
            ycor = self.total[seg - 1].ycor()
            self.total[seg].goto(xcor, ycor)
        self.head.forward(SNAKE_SPEED)
    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
