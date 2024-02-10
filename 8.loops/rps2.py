import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK =1
    PAPER=2
    SCISSOR=3
playagain = True

while playagain==True:        
    
    playerchoice= input("\nEnter.. \n1 for Rock, \n2 for paper, or \n3 for Scissoers:\n\n ")

    player = int(playerchoice)

    if player <1| player > 3:
        sys.exit("you must enter 1 ,2, 3") 
        # It will exit from runtime cmd


    computerchoice = random.choice("123")
    compchoice = int(computerchoice)

    print("")
    print("your Choice : "+ str(RPS(player)).replace("RPS.","" )+"\n")
    print("computerchoice :"+str(RPS(compchoice)).replace("RPS.","" )+"\n")
    print("")


    if player == 1 and computerchoice==3:
        print("🎉🎉You wins")
    elif player == 2 and compchoice ==1:
        print("🎉🎉You wins")
    elif player == 3 and compchoice ==2:
        print("🎉🎉You wins")
    elif player == compchoice:
        print("🤷‍♂️Match Tie")
    else :
        print("🐍 python wins\n\n")
    
    user_inp= input("\nDo you want to play again ?:\n  If yes enter Y: \n  else :N\n\n")
    if user_inp.lower()=="y":
        continue
    else :
        playagain = False
        print("Good bye👋👋👋👋")
sys.exit("Take care!!🙌🙌🙌")


