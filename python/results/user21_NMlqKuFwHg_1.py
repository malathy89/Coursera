# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import math
import random

def number_to_name(number):
    # fill in your code below  
    # convert number to a name using if/elif/else
    if(number==0):
        return "rock"
    elif(number==1):
        return "Spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"
    else:
        return "select number between 0 and 4."
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    if(name=="rock"):
        return 0
    elif(name=="Spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return "Invalid name ."
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    # convert name to player_number using name_to_number    
    player_number=name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,4)
    # compute difference of player_number and comp_number modulo five
    diff=player_number-comp_number
    # use if/elif/else to determine winner
    wins=""
    if(diff>0):
       wins="Player wins!"
    elif(diff<0):
       wins="Computer wins!"
    else:
       wins="Player and computer tie!"
    # convert comp_number to name using number_to_name
    computer_name=number_to_name(comp_number)
    # print results
    print
    print "Player chooses ",name
    print "Computer chooses ",computer_name
    print wins
   

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
