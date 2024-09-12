#While loop = will execute some code WHILE some condns remains true

age  = int(input("Enter ur age: "))

while age < 0:
    print("Age can't be -ve ")
    age = int(input("Enter ur age: "))

print(f"You are {age} years Old")