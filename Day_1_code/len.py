import random

count = 0
dice1 = 1
dice2 = 0
dice3 = 2

answer = input("How many tries do you think it will take?")
bet = input("How much money would you like to bet?")

while (dice1 != dice2) or (dice1 != dice3):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print(dice1, dice2, dice3)
    count+= 1

if(count == answer):
    print("You are correct! You win", bet)
else:
    print("You lose! It took", count, "tries and you lost", bet, "dollars.")
