print("Welcome to my basic TEMPERATURE CONVERTER")

temperature = float(input("Enter a temperature to be converted: "))

format = input(("Choose the format F or C: "))

if format == "C":
    temperature = round((temperature-32)/(1.8),2)
    print(f"The temperature in Celsium is {temperature}")

elif format == "F":
    temperature = round((temperature-32)*(1/1.8),2)
    print(f"The temperature in Fahrenheit {temperature}")
