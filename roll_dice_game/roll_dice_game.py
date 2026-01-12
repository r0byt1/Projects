import random 

def roll_dice ():

    min_value = 1 
    max_value = 6
    roll = random.randint (min_value, max_value)
    return roll 

while  True:
    players = input ("Enter the number of players (2 - 4): ")
    print("-" * 30)    
    print()
    print("First player to 50 - wins the game.")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4 :
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")
        
winning_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < winning_score:

    for player_idx in range(players):
        print (f"\nPlayer number {player_idx + 1}, turn has just started.")
        print ("Your current score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input ("Would you like to roll the dice? (y/n): ")
            if should_roll.lower() !="y":
                break
            
            value = roll_dice()
            if value == 1:
                print ("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += value 
                print ("You rolled a:", value)

            print ("Your current score is:", current_score)

        player_scores [player_idx] += current_score
        print ("Your total score is:", player_scores[player_idx])

final_score = max(player_scores)
winner_idx = player_scores.index(final_score)
print (f"\nPlayer number {winner_idx + 1} wins with a score of {final_score}!")
