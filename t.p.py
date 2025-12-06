import sys
import random
import time 


def game():
    gamecount = 0
    print("Lets play a game!")
    input("To play game press Enter!")
    print("U have to guess what number i was thinking!!!")
    time.sleep(0.5)
    print("Are u ready?")
    input("press enter to continue")
    while True :
        userchoice = int(input("Pick ur choice between 1 to 10   \n"))
        computerchoice = random.randint(1, 10)
        gamecount = 0
        userchoice  = 0
        while userchoice != gamecount:
            gamecount += 1
            while True:
                if userchoice == computerchoice :
                    print(f"yeah! U WON!!! I was thinking of {userchoice}")
                else :
                    print(f"U lose i was'nt thinking of {userchoice}" )

        print(f"I was thinking of {computerchoice}")
        print("Gamecount :", gamecount)
        time.sleep(1)
        choice = input("play again? Type Y for yes or Q for quit! ").strip().lower()
        if choice == "Y":
            continue
        else:
            print("Goodbye!!!")
            break 
game()         


