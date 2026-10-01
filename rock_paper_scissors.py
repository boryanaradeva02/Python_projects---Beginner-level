
import random

print("Welcome to my mini game: ROCK / PAPER / SCISSORS")

while True:
    choice = input("Rock, paper, scissors? (r / p / s): ").lower()

    computer_choice = random.randint(1, 3)

    if choice == 'r':
        print("You chose rock!")
        player_choice = 1
    elif choice == 'p':
        print("You chose paper!")
        player_choice = 2
    elif choice == 's':
        print("You chose scissors!")
        player_choice = 3
    else:
        print("Please enter a valid input.")
        continue

    if computer_choice == 1:
        print("Computer chose rock!")
    elif computer_choice == 2:
        print("Computer chose paper!")
    else:
        print("Computer chose scissors!")

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You lose!")

