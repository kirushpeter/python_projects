import random
import time

roll_again = "yes"
"""lets see"""
while roll_again == "yes" or roll_again == "y":
    print("\n Rolling the dice ...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("the values are:")
    print("Dice 1 =", dice1,"\nDice 2 =", dice2)

    if dice1 == dice2:
        print("you rolled a double!")
    else:
        print("keep trying!")
 
    roll_again = input("\n Roll the dice again? (y/n)")