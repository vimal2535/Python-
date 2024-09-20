from turtle import Screen
from time import sleep
from car import Car
from element import Object
sc=Screen()
sc.colormode(255)
sc.tracer(0)
car=Car()
tu=Object()
tu.level()
sc.setup(600,600)
sc.listen()
sc.onkeypress(tu.move,"Up")
game=True
while game:
    sleep(0.1)
    sc.update()
    car.new_car()
    car.move_car()
    if tu.tim.ycor() > 280 :
        tu.next_level()
        car.next_level()
    for cars in car.total:
        if cars.distance(tu.tim) < 20:
            car.game_over()
            game=False

sc.exitonclick()
