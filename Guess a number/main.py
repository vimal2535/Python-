from os import system
from time import sleep
from random import randint
number=randint(1,100)
def guess():
    game=True
    while game:
        print("Guess the Number between 1 to 100!...")
        difficulty_level=input("Do you want it 'easy' or 'hard'?: ")
        if difficulty_level=='easy':
            n=10
        elif difficulty_level=='hard':
            n=5
        for i in range(n,0,-1):
                if i>1:
                    user=int(input("Guess the number?: "))
                    if (user>number):
                        print("It's less than you think")
                        print("Guess again!!")
                        print(f"You have {i-1} chances left")
                    elif (user<number):
                        print("It's greater than that")
                        print("Guess again!!")
                        print(f"You have {i-1} chances left")
                    elif(user==number):
                        print("You.ve guessed it correctly!")
                        break
                        
                else:
                    user=int(input("Guess the number?: "))
                    if(user==number):
                        print("You've guessed it correctly!")
                        break
                    else:
                        print("Oops! You've lost all your chances---Game Over!!!!")
                        print(f"The correct number is: {number}")
                        break
        game=False
        
guess()
redo=input("Do you want to play again? Type 'y' or 'n': ")
if redo=='y':
    system("cls")
    guess()
    sleep(5)
else:
    system('cls')
    print("GoodBye!")
    sleep(1)

