from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
from time import sleep
sc=Screen()
sc.setup(800,600)
sc.bgcolor("black")
sc.title("PING PONG")
sc.tracer(0)
score=Score()
pad=Paddle()
ball = Ball()
sc.listen()
sc.onkeypress(pad.right_up,"Up")
sc.onkeypress(pad.right_down,"Down")
sc.onkeypress(pad.left_up,"w")
sc.onkeypress(pad.left_down,"s")
game=True
while game:
    sleep(ball.ball_speed)
    sc.update()
    ball.move()
    #Detect Collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285 :
        ball.bounce_y()
    #Detect Collision with right paddle
    if ball.distance(pad.total[0]) < 50 and ball.xcor() > 340 :
        ball.bounce_x()
    if ball.distance(pad.total[1]) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    #Ball passes the line
    if ball.xcor() > 405 :
        ball.refresh()
        score.l_point()
    if ball.xcor() < -405:
        ball.refresh()
        score.r_point()


sc.exitonclick()
