from time import sleep
from os import system
from alphabets import alphabet
from pic import logo
def encrypt_decrypt(direct,sample_text,shift_number):
    empty=""
    for i in sample_text:
        if i in  alphabet:
            index_value=alphabet.index(i) 
            if direct=="encode":
                shifts=index_value+shift_number
                if shifts>25:
                    shifts-=26
                    empty+=alphabet[shifts]
                else:
                    shifts=shifts
                    empty+=alphabet[shifts]
            elif direct=="decode":
                shifts=index_value-shift_number
                empty+=alphabet[shifts]
        else:
            empty+=i
    print(f"The {direct}d text is : \"{empty}\"")


repeat=True
while repeat:
    system('cls')
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26
    encrypt_decrypt(direction,text,shift)
    result=input("type \"yes\" to encrypt/decrypt again ,type \"no\" to stop\n")        
    if result=="no":
        repeat=False
        system('cls')
        print("GoodBye!")
        sleep(3)



 

