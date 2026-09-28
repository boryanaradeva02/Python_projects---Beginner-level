print("Welocme to my very basic compound interest calculator :)")
print("This calculator uses compound interest!")
print("Have fun!")
 # Initial Investment - Amount of money that you have available to invest initially.


savings = int(input("How much do you have saved currently? "))


# Number of years

years = int(input("How many years will you save for?"))


#step Interest rate

interest_rate = float(input("What's your rate of return? "))


# Contribute - Amount that you plan to add to the principal every month, 

# or a negative number for the amount that you plan to withdraw every month.


contribute = int(input("How much extra will you contribute? "))


print("Times contribute")

print("0 - Per month")

print("1 - Per week")

print("2 - Bi-weekly")

print("3 - Per year")

times_contribute = int(input("How often will you contribute?"))
periods_per_year = 12
r = (interest_rate / 100) / periods_per_year
n = years * periods_per_year



def calculate(savings, years, interest_rate, contribute, times_contribute):

        if savings:
             savings < 0
             print("Savings can't be negative")
             

        if years:
             years < 0
             print("Years can't be negative")

        if interest_rate:
             interest_rate < 0
             print("Interest rate can't be negative")

        if contribute:
              contribute >= 0
              pass
            
        if times_contribute == 0:

             r = (interest_rate/100) / 12
             n = years * 12
              
        elif times_contribute == 1:
            r = (interest_rate/100) / 52
            n = years * 52

        elif times_contribute == 2:
             r = (interest_rate/100) /26
             n = years *26

        elif times_contribute == 3:
             r = interest_rate / 100
             n = years

        else:
             print("Invalid period")
        
        future_savings = (
        savings * ((1 + r) ** n)
        + contribute * (((1 + r) ** n - 1) / r)
)

        return future_savings
        


future_savings = calculate(savings, years,interest_rate,contribute,times_contribute)

print(f"After {years} years, you will have {future_savings:.2f}")
    
