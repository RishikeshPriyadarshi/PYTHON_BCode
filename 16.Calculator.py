operator = input("Enter an opeartor(+ - * / )")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == '/':
    result = num1/num2
    print(round(result,3))
else:
    print(f"{operator} is not valid a operator")    
