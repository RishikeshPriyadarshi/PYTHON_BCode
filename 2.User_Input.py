#input() = A function that promts the user to enter data
#          Returns the eneterd data as string



# input()
#input(Your name is : )

name = input("What is ur name?: ")
# age = input("How old r u?: ")
age = int(input("How old r u?: "))

# age = age + 1 --> it will give error beacuse it is string in the first place , so to oncatenate we need to typecast it into integer
#age = int(age)--> we can short or condense this method at typecasting step  only
age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"you r {age} years old")




 
