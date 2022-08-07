#Rock paper scissors game

#import random
from random import randint

print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())

print("-----------------------------------")

#randomNumber = random.randint(0,2)
randomNumber = randint(0,2)
computerNumber = "rock"

if randomNumber == 0:
    computerNumber = "rock"
elif randomNumber == 1:
    computerNumber = "paper"
elif randomNumber == 2:
    computerNumber = "scissors"
#print(computerNumber)

Player_1 = input("player_1 , Make your move : ").lower()
Player_2 = computerNumber
print(f"player_2 , Make your move : {computerNumber} ")

if Player_1 == Player_2 :
    print("thats a tie!")

elif Player_1 == "rock":
    if Player_2 == "paper":
        print("player_2 wins!")
    elif Player_2 == "scissors":
        print("player_1 wins!")
        
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("player_1 wins!")
    elif Player_2 == "scissors":
        print("player_2 wins!")
        
elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("player_1 wins!")
    elif Player_2 == "rock":
        print("player_2 wins!")
        
else:
    print("something went wrong!")
    
    
    
# if Player_1 == "rock" and Player_2 == "paper" :
#     print("player_2 wins!")
# elif Player_1 == "rock" and Player_2 == "scissors":
#     print("player_1 wins!")
    
# elif Player_1 == "paper" and Player_2 == "rock":
#     print("player_1 wins!")
# elif Player_1 == "paper" and Player_2 == "scissors":
#     print("player_2 wins!")
    
# elif Player_1 == "scissors" and Player_2 == "paper":
#     print("player_1 wins!")
# elif Player_1 == "scissors" and Player_2 == "rock":
#     print("player_2 wins!")
    



