How the program generally works:

Simple dice game called "Tuple Out Dice Game." In this game, players take turns rolling three dice, attempting to achieve a "tuple out" where all three dice show the same value.
However, if a player rolls a tuple out, their score for that turn becomes zero. The game continues until one player reaches or exceeds a predetermined maximum score or until a set
number of rounds is completed.

Fixed dice means that the player rolled two of the same dice values on that turn, and any rerolls after that won't go toward their score calculation. Displayed the same way that 
rolls are. If you see two of the same number indices in a roll, the program will show these two numbers again as "fixed dice" with the third index as zero. If there are no dice
indices that end up as the same number value that turn, then all the (all 3) indices will be displayed as zero for the fixed dice. 

Hidden feature right now that doubles the score of the player if they choose not to reroll after the first roll on their turn to go! 
(I had trouble fixing this so I left it as a feature).

Score calculations are given after each player turn, but the actual total scores for each player won't show until after one cycle of turns goes through 
(Meaning both players have gone in that cycle)

Game ends when one player either hits 50 points or hits 5 turns.

Displays each round as "Round 1, Round 2" and so on!

Displays each player's turn as "Player 1/2's turn" depending on who exactly is going at the time

Currently, the players can only choose to reroll their three dice one time before they must say no afterwards due to complications I ran into while making the program!
If they don't the score will not properly display the right values due to buggy behavior. However, if this rule is followed, everything works smoothly. 

How to run the program (code):

1. Begin the program and examine the roll you are given (assuming you don't "tuple out" and lose the turn from rolling the same number on all dice).
2. It will tell you what round it is each time (Round 1 to start), and tell you what turn it is each time (Player 1's turn).
3. It will show you your roll alongside "Fixed dice", with both placed into brackets.
4. Program will then prompt the player if they want to reroll the dice.
5. If the player chooses no, their turn will end, and they will be given their dice summed up score times two.
6. If the player chooses yes, their turn will continue, and they will be shown another roll alongside "Fixed dice".
7. However, they can't select yes anymore after this or the score won't keep track properly (Must say no after the first reroll)!!
8. Following this criteria for each consecutive player turn will have the game run smoothly and repeat from step 1 until player's hit 5 turns or 50 game score.
9. Still the possibility of tupling out!


