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

def display_scores(scores):
    print("Current Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

def record_scores(scores, winner):
    print(f"{winner} wins the game!")

def play_round(player):
    print(f"\n{player}'s turn!")
    score = 0
    dice = roll_dice()
    print(f"Roll: {dice}")
    
    score += sum(dice)

    while True: 
        if tuple_out(dice):
            print(f"You tupled out!!! You rolled {dice} Your score on this turn is zero......")
            score = 0
            return score 
        
        fixed_dice = []
        for die in dice:
            if dice.count(die) >= 2:
                fixed_dice.append(die)
            else:
                fixed_dice.append(0)
        print(f"Fixed dice: {fixed_dice}")
        

        choice = input("Do you want to reroll the dice? (yes/no): ").lower()
        if choice == "no":
            for die in range(len(dice)):
                if dice[die] not in fixed_dice:  # Check if the die is not fixed
                    score += dice[die]  # Add the value of the die to the score
            break
        elif choice == "yes":
            for die in range(len(dice)):
                if dice[die] not in fixed_dice:
                    dice[die] = random.randint(1,6)
                    
            print(f"Roll: {dice}")
    print(f"Score: {score}")
    return score

def play_game(players, max_score = 50, max_rounds = 5):
    scores = {player: 0 for player in players}
    round_counter = 0

    while round_counter < max_rounds:
        round_counter += 1
        print(f"\nRound {round_counter}")
        for player in players:
            score = play_round(player)
            scores[player] += score
            if scores[player] >= max_score:
                record_scores(scores, player)
                return 
        display_scores(scores)

# Actual functionality of the game
players = ["Player 1", "Player 2"]
play_game(players)
            

