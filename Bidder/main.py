from art import logo
from time import sleep
from os import system
bidding_details={}
def function(bid): #function to check the highest bidder
    highest_bid=0
    highest_bidder=""
    for i in bid:
        a=bid[i]
        if a>highest_bid:
            highest_bid=a
            highest_bidder=i
    print("The winner is {} with a bid of ${}".format(highest_bidder,highest_bid))
print(logo)
bidding=True
while bidding: #loop to get the bidding details
    name=input("Enter the name of the bidder: ")
    bid_amount=int(input("Enter your bid amount: $"))
    bidding_details[name]=bid_amount
    bid=bidding_details
    another_bidder=input("Are there any other bidders? Type 'yes'/'no' : ") #Checking is there any other bidder
    if another_bidder=="no":
        bidding=False
        system('cls')#used to clear the screen before the OP
        function(bid)
        sleep(5)
        
    elif another_bidder=="yes":
        system('cls')#used to clear the screen after getting the details of the bidder , so that other bidder don't know the price of the previous bidder

    
