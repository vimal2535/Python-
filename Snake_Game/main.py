from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Score
from gamebox import Box
sc=Screen()
box=Box()
sc.colormode(255)
sc.title("Snake Game")
sc.setup(640,650)
sc.tracer(0)
snake = Snake()
food=Food()
score=Score()
snake.create_snake()
sc.listen()
sc.onkey(snake.up , "Up")
sc.onkey(snake.down , "Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right, "Right")
while snake.setup:
    sc.update()
    sleep(0.1)
    snake.move()
    #food
    if snake.head.distance(food) < 10:
        score.point()
        food.refresh()
        snake.new()
    #wall collision
    if (snake.head.xcor() > 287 or snake.head.xcor()< -287 ) or (snake.head.ycor() > 287 or snake.head.ycor()< -287):
        sleep(2)
        snake.reset()
        score.end()

    #body collision
    for inch in range(1, len(snake.total)):
        if snake.head.distance(snake.total[inch]) < 10:
            sleep(2)
            snake.reset()
            score.end()















sc.exitonclick()
