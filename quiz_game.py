print("Welcome to my QUIZ GAME")

questions = ("How many elemnts are in periodic table? ",
             "Who is Ali Abdaal? ",
             "Who was the first woman in the world?",
             "What is C1 level of English speaking? ",
             "What is Pi?")

options = (("A. 12","B. 34","C. 54","D. 118"),
           ("A. blogger","B. doctor","C. scientist","D. painter"),
           ("A. Eva","B. Normani","C. IvA","D. Ava"),
           ("A. native","B. beginner","C. intermediete","D. non of these"),
           ("A. Prime number","B. 3.14","C. Negative nuber","D. Pier"))

answers = ("D", "A", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect" )
        print(f"{answers[question_num]} is correct answer")
    
    question_num += 1