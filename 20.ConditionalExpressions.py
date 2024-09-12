# Conditional expression = A one-line shortcut for the if-else statement (ternary operator i.e similar to ternary operator in other programming language)
#                          Print or assign one of two values based on condition
#  Formula is            :   X if condition  else Y
#------------------------------------------------------------------------------

num = 9

a = 6
b = 7

age = 1

temprature = 30

user_role = "guest"

#print("possitive" if num > 0 else "Negative")

#result = "Even" if num%2==0 else "Odd"
#print(result)

#max_num = a if a>b  else b
#min_num = a if a<b  else b
#print(max_num)
#print(min_num)

#status = "Adult"  if age>=18 else "child"
#print(status)

#weather = "Hot" if temprature>25 else "Cold"
#print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
