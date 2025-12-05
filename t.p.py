import sys
import random
import time 

def game():
    print("Lets play a game!")
    input("To play game press Enter!")
    print("U have to guess what number i was thinking!!!")
    time.sleep(0.5)
    print("Are u ready?")
    input("press enter to continue")
    userchoice = int(input("Pick ur choice between 1 to 10   "))
    computerchoice = random.randint(1, 10)
    if userchoice == computerchoice :
        print(f"yeah! I was thinking of {userchoice}")
    else :
        print("U lose i was'nt thinking of {us}")
game()
