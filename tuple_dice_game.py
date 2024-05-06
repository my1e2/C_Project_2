# tuple out dice game

import random 

def roll_dice(): # function for rolling 3 dice
    dice = []
    for die in range(3):
        roll = random.randint(1,6)
        dice.append(roll)
    return dice

def tuple_out(dice): # function that says if the three dice values are the same, you "tuple out" 
    return len(set(dice)) == 1

def display_scores(scores): # function to display scores
    print("Current Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

def record_scores(scores, winner): # function to determine the winner later on after scores are displayed
    print(f"{winner} wins the game!")

def play_round(player): # function to keep track of player rolls each round, and the option to reroll
    print(f"\n{player}'s turn!")
    score = 0
    dice = roll_dice()
    print(f"Roll: {dice}")
    
    score += sum(dice)

    while True: 
        if tuple_out(dice): # if a player tuples out, they score nothing for that turn and it ends!
            print(f"You tupled out!!! You rolled {dice} Your score on this turn is zero......")
            score = 0
            return score 
        
        fixed_dice = []
        for die in dice:
            if dice.count(die) >= 2: # checking if 2 dice are fixed (equal the same value)
                fixed_dice.append(die)
            else:
                fixed_dice.append(0)
        print(f"Fixed dice: {fixed_dice}")
        

        choice = input("Do you want to reroll the dice? (yes/no): ").lower() # can only reroll once right now before you must choose no for proper scoring...
        if choice == "no":
            for die in range(len(dice)): # looping through list
                if dice[die] not in fixed_dice:  # Check if the die is not fixed
                    score += dice[die]  # Add the value of the die to the score
            break # break out of the while loop and restart for the next player's turn
        elif choice == "yes": # continue with the loop until the player says no or tuples out
            for die in range(len(dice)):
                if dice[die] not in fixed_dice:
                    dice[die] = random.randint(1,6) # rerolling process of die from 1 to 6
                    
            print(f"Roll: {dice}")
    print(f"Score: {score}")
    return score # returning final score from the process

def play_game(players, max_score = 50, max_rounds = 5): # function giving conditions for the ending of the game
    scores = {player: 0 for player in players}
    round_counter = 0

    while round_counter < max_rounds: 
        round_counter += 1 # appending 1 each time a round goes by
        print(f"\nRound {round_counter}")
        for player in players:
            score = play_round(player) # calling earlier function 
            scores[player] += score
            if scores[player] >= max_score:
                record_scores(scores, player) # calling earlier function to keep tabs on score
                return 
        display_scores(scores) # displaying final scores

# Actual functionality of the game
players = ["Player 1", "Player 2"] # introducing player 1 and 2 as a list for game functionality
play_game(players) # calling function to actually play the game 
            

