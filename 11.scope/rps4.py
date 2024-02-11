import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK =1
    PAPER=2
    SCISSOR=3
playagain = True

game_count =0
def playgame(playagain):
    if playagain ==False:
        print("Good bye👋👋👋👋")
        sys.exit("Take care!!🙌🙌🙌")
    
    player= input("\nEnter.. \n1 for Rock, \n2 for paper, or \n3 for Scissoers:\n\n ")

    

    if player not in ["1","2","3"]:
        print("you must enter 1 ,2, 3") 
        playgame(playagain)
        # It will exit from runtime cmd
    player = int(player)
    

    computerchoice = random.choice("123")
    compchoice = int(computerchoice)

    print("")
    print("your Choice : "+ str(RPS(player)).replace("RPS.","" )+"\n")
    print("computerchoice :"+str(RPS(compchoice)).replace("RPS.","" )+"\n")
    print("")
    def decide_winner(player, computerchoice):
        if player == 1 and computerchoice==3:
            return "🎉🎉You wins"
        elif player == 2 and compchoice ==1:
            return "🎉🎉You wins"
        elif player == 3 and compchoice ==2:
            return "🎉🎉You wins"
        elif player == compchoice:
            return "🤷‍♂️Match Tie"
        else :
            return "🐍 python wins\n\n"
    game_result = decide_winner(player, computerchoice) 
    print(game_result)
    global game_count
    game_count += 1  
    print(f"Your game count is :{game_count}")  
    user_inp= input("\nDo you want to play again ?:\nIf yes enter :Y \nElse Enter   :N\n\n")
    playgame(True if user_inp.lower()=='y' else False)

playgame(playagain) 


