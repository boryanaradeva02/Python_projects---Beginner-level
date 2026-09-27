print("Welcome to my second compound interest calculator")
print("Have fun! ")

principle = 0 
rate = 0
time = 0 

while principle <= 0: # we want to start the while loop again if the input value is not valid
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Principle can't be less or equal to zero! ")

while rate <= 0: # we want to start the while loop again if the input value is not valid
    rate = float(input("Enter a rate amount: "))
    if rate <= 0:
        print("Rate can't be less or equal to zero! ")

while time <= 0: # we want to start the while loop again if the input value is not valid
    time = float(input("Enter a time amount: "))
    if time <= 0:
        print("Time can't be less or equal to zero! ")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years will be $ {total:.2f}")