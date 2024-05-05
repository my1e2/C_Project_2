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

def play_round(player):
    print(f"\n{player}'s turn!")
    dice = roll_dice()
    score = 0
    print(f"Roll: {dice}")

    while True: 
        if tuple_out(dice):
            print("You tupled out!!! Your score on this turn is zero......")
        
        fixed_dice = []
        for die in dice:
            if dice.count(die) >= 2:
                fixed_dice.append(die)
            else:
                fixed_dice.append(0)
        print(f"Fixed dice: {fixed_dice}")

        choice = input("Do you want to reroll the dice? (yes/no): ").lower()
        if choice == "no":
            score += sum(die for die in dice if die != 0)
            break
        elif choice == "yes":
            for die in range(len(dice)):
                if dice[die] not in fixed_dice:
                    dice[die] = random.randint(1,6)
    print(f"Score: {score}")
    return score
    
    

