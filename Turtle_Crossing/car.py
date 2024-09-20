from random import randint
from turtle import Turtle

SPEED=10
CAR_END = -290
class Car:
    def __init__(self):
        self.total=[]
        self.car_speed = 7


    def new_car(self):
        self.random = randint(1, 6)
        self.code = [self.random == 1, self.random == 1 or self.random == 2,
                     self.random == 1 or self.random == 2 or self.random == 3,
                     self.random == 1 or self.random == 2 or self.random == 3 or self.random == 4]
        if self.car_speed <= 10:
            self.joke = self.code[0]
        elif self.car_speed <= 15:
            self.joke = self.code[1]
        elif self.car_speed <= 30:
            self.joke = self.code[2]
        elif self.car_speed <= 45:
            self.joke = self.code[3]
        if self.joke:
            tim = Turtle("square")
            tim.shapesize(stretch_wid=1,stretch_len=2)
            tim.penup()
            tim.goto(320,randint(-240,260))
            tim.color(randint(1,255),randint(1,255),randint(1,255))
            self.total.append(tim)

    def move_car(self):
        for sen in self.total:
            sen.backward(self.car_speed)

    def next_level(self):
        self.car_speed+=5

    def game_over(self):
        self.car_speed=0
        self.sco = Turtle()
        self.sco.penup()
        self.sco.color("red")
        self.sco.goto(0, 0)
        self.sco.hideturtle()
        self.sco.write("GAME OVER!", align="center", font=("Arial", 20, "normal"))




