from random import choice
from troop import word_list
from troop import level
from troop import logo
from time import sleep
from os import system
repeat=True
print(logo)
def main():
    fru=choice(word_list)
    main_fruit=fru.upper()
    fruit=list(main_fruit) #selecting a fruit/vegetable and putting it in a list
    com="" #empty string to store the input
    for i in range(0,len(fruit)):
        com+="_"   
    com=list(com) #creating a list with dash with same no of letters of the flower
    count=0 #initializing count as 0
    life=6
    for i in com:
        print(i,end=" ") #priting the dash for user to identify the no of letters
    while count<=5 and "_" in com: #when count is greater than 5 and _ is still in com we enter the loop and get the user input
        print("\n")
        a=input("Guess the letter of the fruit/vegetable\n")
        a=a.upper()
        if a in com:
            print("You've already guessed the letter {}".format(a))
        elif a in fruit:
            for i in range(0,fruit.count(a)):
                index=fruit.index(a) #when the letter is present in the actual word then we are finding the index value of the letter
                com[index]=a #we are changing the _ in the com with appropriate letter with the correct index value
                fruit[index]="_" #after we are replacing the letter from the fruit so the loop will not be repeated
            for i in com:
                print(i,end=" ")
            if "_" not in com:
                print("\n")
                print("Hurrah!,you've won")
        else:
            count+=1
            life-=1
            if count==1:
                 print(level[0])
                 print(f"You've got {life} lives left")
                 
            elif count==2:
                 print(level[1])
                 print(f"You've got {life} lives left")
            elif count==3:
                 print(level[2])
                 print(f"You've got {life} lives left")
            elif count==4 :
                print(level[3])
                print(f"You've got {life} lives left")
            elif count==5 :
                print(level[4])
                print(f"You've got {life} lives left")
            else:
                print(level[5])
                print("Game Over-You're hanged!!")
                print(f"The correct word is: {fru.upper()}")
                
main()
while repeat:
    guess=input("Do you want to guess again? 'yes' or 'no': ")
    if guess=='yes':
        system('cls')
        main()
    else:
        print("Thank you!")
        repeat=False
        sleep(3)
