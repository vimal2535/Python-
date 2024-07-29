
from side import logo,vs,data
from random import randint
from os import system
from time import sleep
def num_generator():
    return randint(0,49)
def compare(A,B):
    if A>B:
        return 'A'
    elif B>A:
        return 'B'
point=0
comparison=True
first=num_generator()
second=num_generator()
while first==second:
    second=num_generator()
    
while comparison:
    print(logo)
    print(f"Compare A: {data[first]['name']}, {data[first]['description']}, {data[first]['country']}")
    print(vs)
    print(f"Against B: {data[second]['name']}, {data[second]['description']}, {data[second]['country']}")
    if point>0:
        print("You're right! your current score is :",point)
    answer=input("Who has more followers? Type 'A' or 'B': ").upper()
    result=compare(data[first]['follower_count'],data[second]['follower_count'])
    if answer==result:
        system('cls')
        point+=1
        first=second
        second=num_generator()
            
    else:
        system('cls')
        print("Your final score is:",point)
        sleep(3)
        comparison=False

    
        

    
    
    
            
        
    
    
