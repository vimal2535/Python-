import turtle
import pandas
import csv
from turtle import Turtle,Screen
from time import sleep
sc=Screen()
sc.screensize(400,300)
sc.title("Indian States Game")
sc.bgpic("india-outline-map.gif")
data = pandas.read_csv("indian_states_coordinates.csv")
state_names = data["state"].tolist()
pro = "Start Guessing"
a=0
game_is_on = True
while game_is_on:
    answer = sc.textinput(title=f"{a}/36 Guess the State Name", prompt=pro)
    answer = answer.lower()
    if answer == "exit":
        new_data=pandas.DataFrame(state_names)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer not in state_names:
        pass
    else:
        pro="Keep Going"
        a += 1
        man=data[data.state==answer]
        state_names.remove(answer)
        mean=answer.title()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(man.x.item()),int(man.y.item( )))
        turtle.write(mean,True,"center",("Arial",8,"normal"))
    if a==36:
        turtle.hideturtle()
        turtle.goto(0,0)
        turtle.color("red")
        turtle.write("Congratualtions You've Completed!",False,"center",("Arial",24,"normal"))
        sleep(2)
        game_is_on = False




# def get_mouse_click_cor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()







