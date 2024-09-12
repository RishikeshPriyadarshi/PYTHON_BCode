unit = input("Is this temprature in celcius or Fahrenheit (C/F): ")
temp = float(input("Enter th temprature: "))

if unit == "C":
    temp = round((temp*9)/5 + 32, 1)
    print(f"The temperature is in fahrenheit: {temp} F ")
elif unit == "F":
    temp = round((temp-32)*5/9, 1)
    print(f"THe temprature in celcius is in celcius: {temp} C ")
else:
    print(f"{unit} is an invalid unit of measurement ")
