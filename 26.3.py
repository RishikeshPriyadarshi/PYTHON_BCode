#using logical-operator(or ) in while loop

num = int(input("Enter a number b/w 1 - 10: "))

while num <1 or num >10:
    print(f"{num} is not valid ")
    num = int(input("Enter a number b/w 1 -10: "))#reprompting the user for escapin the infinite-loop

print(f"Your number is {num}")    


