from os import system
from art import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return (round((n1/n2),1))
opera={
"+":add,
"-":sub,
"*":mul,
"/":div
}
print(logo)
def operation():
    num1=float(input("Enter the first number?: "))
    for i in opera:
        print(i)
    cont=True
    while cont:
        process=input("Select the operator: ")
        num2=float(input("Enter the next number?: "))
        function=opera[process]
        result=function(num1,num2)
        print(f"{num1} {process} {num2} = {result}")
        conti=input("Type 'y' to continue with the result / type 'n' to perform a new calculation: ")
        if conti=='y':
            num1=result
        else:
            system('cls')
            operation()

operation()

