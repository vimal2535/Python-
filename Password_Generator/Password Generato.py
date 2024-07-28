from random import choice
import random
from file import letters

print("Welcome to the PyPassword Generator!")

let=int(input("Enter the number of letters\n"))
num=int(input("Enter the number of numbers\n"))
sym=int(input("Enter the number of symbols\n"))
password=""
l=[]
for i in range(0,let):
    l.append(choice(letters))
for i in range(0,num):
    l.append(choice(numbers))
for i in range(0,sym):
    l.append(choice(symbols))
random.shuffle(l)
for i in l:
    password+=i
print(password)


    
