import random
print("Welcome to my little Dice rolling game! Have fun!")


while True:
    roll_question = input("Do you want to roll the dice? (y/n)").strip().casefold() #  Standardizing User Input Y = y, N = n
    num_1 = random.randint(1,6)
    num_2 = random.randint(1,6)

    if roll_question == 'n':
        print("Thank you for playing!")
        break
    if roll_question == 'y':
        print(f"({num_1},{num_2})")
    else:
        print("Invalid input")
        roll_question = input("Do you want to roll the dice? (y/n)")
