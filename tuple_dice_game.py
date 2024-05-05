# tuple out dice game

import random 

def roll_dice():
    dice = []
    for die in range(3):
        roll = random.randint(1,6)
        dice.append(roll)
    return dice

def tuple_out(dice):
    return len(set(dice)) == 1

def manage_scores(scores, winner):
    if winner:
        print(f"{winner} won the game!!!")
    else:
        print("Current Scores:")
        for player, score in scores.items():
            print(f"{player}: {score}")

            