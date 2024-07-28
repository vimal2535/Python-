from random import choices
from os import system
from time import sleep
from art import logo
a=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def generator():
        l=[]
        result=choices(a)
        l.append(*result)
        return(l[0])
def compare(user,computer):
    if user==computer:
        return "It's A Draw"
    elif user==0:
        return "You Won"
    elif computer==0:
        return "You Lose!"
    elif user>21:
        return "You went Over, You Lose"
    elif computer>21:
        return "Opponent went over,You Win"
    elif user_score>computer_score:
        return "You Win!"
    else:
        return "You Loose!"
def calculate(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return(sum(cards))
print(logo)
def gaming():
        user=[]
        computer=[]
        game=True
        for i in range(2):
                user.append(generator())
                computer.append(generator())
        while game:
            user_score=calculate(user)
            computer_score=calculate(computer)
            print(f"Your cards: {user}, Your score{user_score}")
            print(f"Computer's first card: {computer[0]}")
            if user_score==0 or computer_score==0 or user_score>21:
                game=False
            else:
                draw=input("Enter 'y' to draw a card, type 'n' to pass: ")
                if draw=='y':
                        user.append(generator())
                else:
                        game=False
        while computer_score!=0 and computer_score<17:
                computer.append(generator())
                computer_score=calculate(computer)
                
        print(f" Your final cards:{user}, final score: {user_score}")
        print(f" Computer's final hand: {computer}, final score: {computer_score}")
        print(compare(user_score,computer_score))
        sleep(5)
gaming()

while input("Do you want to play again? Type 'y' or 'n': ")=="y":
        system("cls")
        gaming()

    
    
    

    
    
    
