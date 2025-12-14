import random
import sys
import argparse


lowest_num = 1
highest_num = 3
ans = random.choice([1,2,3])
is_playing = True
guesses = 0
gamecount = 1
parser = argparse.ArgumentParser(
    description="for asking name"
)
parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="U have to enter name"
)
args = parser.parse_args()



def game():
    name = args.name
    print(f" {name}, Make a choice 1,2 or 3")
    num = int(input())
    if num == ans:
        print(f"you won! YES i was thinking of {ans}")
    global gamecount
    gamecount += 1 
    if num  != ans:
        print(f"you lose! i was thinking of {ans}")
    print(f"gamecount: {gamecount}")
    print("Want to play again? Y/Q")
    nu_m = input()
    if nu_m == "Y":
        game()
    else:
        sys.exit()       

game()