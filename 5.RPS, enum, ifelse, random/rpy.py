import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK =1
    PAPER=2
    SCISSOR=3

""""Enum stands for enumeration. It is a class in the enum 
module that provides a way to create symbolic names
 (members) that are mapped to unique, constant values.
"""
"""used in situations where you have a fixed set of options that you want
 to represent with meaningful names rather than arbitrary 
 integers or strings."""

# print(RPS(2))
# print (RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()

print("")
playerchoice= input("Enter.. \n1 for Rock, \n2 for paper, or \n3 for Scissoers:\n\n ")

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
    print("🐍 python wins")
