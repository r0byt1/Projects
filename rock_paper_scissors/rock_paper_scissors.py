# Imports and score tracking
import random
import time

user_win = 0
computer_win = 0
OPTIONS = ["rock", "paper", "scissors"]


    # Welcome message
print("******** WELCOME TO THE ROCK / PAPER / SCISSORS GAME ********")
time.sleep(1)


    # Functions
def get_user_choice():
    return input("Type Rock / Paper / Scissors (or Q to quit): ").lower().strip()

def get_computer_choice():
    return random.choice(OPTIONS)

def update_score(user_choice, computer_choice):
    """Updates and displays the score based on game rules."""
    global user_win, computer_win

    if user_choice == computer_choice:
        print("It's a tie — no points.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You won this round!")
        user_win += 1
    else:
        print("Computer won this round!")
        computer_win += 1

    time.sleep(0.3)
    print(f"Score — You: {user_win}  Computer: {computer_win}\n")


    # Main program
while True:
    y_n = input("Do you want to play? (yes / no): ").lower().strip()

    if y_n not in ("yes", "no"):
        print(f"Invalid option: '{y_n}'.")
        print("Try again :)")
        continue

    if y_n == "no":
        break


        # Play rounds until the user quits to main menu
    while True:
        user_choice = get_user_choice()
        time.sleep(0.25)

        if user_choice == "q":
            break

        if user_choice not in OPTIONS:
            print(f"Invalid option: '{user_choice}'. Try again.")
            continue

            # Calling the functions
        computer = get_computer_choice()
        print(f"Computer picked: {computer}.")
        update_score(user_choice, computer)


    # Final results
print("\nFinal score:")
print(f"Your score: {user_win} wins")
print(f"Computer score: {computer_win} wins")

if user_win > computer_win:
    print("You won the game! Great job!")
elif user_win < computer_win:
    print("You lost. Better luck next time!")
else:
    print("The game ended in a tie!")

print("\nGoodbye!")
time.sleep(0.5)