#Game Development: Snake-Water-Gun
"""to create this game either in while or for loop run it 10 times, asks the users choice
but don't print first ask's computer's choice and then declare who won and give the point accordingly"""

import random
num=0
print("let's start the game of snake water gun!\n ")
game_d=['Snake','Water','Gun']
comp_point=0
user_point=0
while(num<10):
    num+=1
    choice1 = random.choice(game_d)
    choice2 = input("Now user what is your choice?\n")
    if choice1==game_d[0] and choice2=='Water':
        print("Computer wins!")
        comp_point+=1
    elif choice1==game_d[1] and choice2=='Snake':
        print("User wins!")
        user_point+=1
    elif choice1==game_d[1] and choice2=='Gun':
        print("Computer wins!")
        comp_point+=1
    elif choice1 == game_d[2] and choice2 == 'Water':
        print("User wins!")
        user_point+=1
    elif choice1==game_d[2] and choice2=='Snake':
        print("Computer wins")
        comp_point+=1
    elif choice1==game_d[0] and choice2=='Gun':
        print("User wins!")
        user_point+=1
    else:
        print("it's a tie!")
print("\nGameOver!\n")
print("The result is:")
print("Computer Points:",comp_point)
print("User Points:",user_point)







