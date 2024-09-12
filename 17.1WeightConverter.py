weight = float(input("Enter your weight: ")) # This line can raise a ValueError if the input isn't a valid number.


unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    output_unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {output_unit}")

elif unit == "L":
    weight = weight / 2.205
    output_unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {output_unit}")

else:
    print(f"{unit} was not valid")
