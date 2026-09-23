print("Welcome to my weigh converter! You can choose between LB or KG")

metric = input("Select the unit of measurement used for your weight: ")

weight = float(input("Enter your weght: "))

if metric == 'lb':
    weight = weight * 0.45359237
    print(f"Your weigh in KG is {weight}")
elif metric == 'kg':
    weight = weight / 0.45359237
    print(f"Your weigh in LB is {weight}")
