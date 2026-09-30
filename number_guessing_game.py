print("Welcom to my beginner number guessing game!")
print("Have fun! :)")

number = 13


while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))
        
        if guess >= 30:
            print("Too high!")
        elif (guess >= 20 and guess <= 29):
            print("You are close... Try again!")
            guess
        elif (guess < 20 and guess > 10 and guess != 13):
            print("You are closer...Keep going!")
            
        elif (guess > 0 and guess < 9) or (guess < 0):
            print("Too low. Try agian!")
            
        elif guess == 13:
            print("You did it! Bravisiomo!")
            break

        else:
            print("Please enter a number between 1 and 100.")

    except ValueError:
        print("Please enter a valid number.")

        