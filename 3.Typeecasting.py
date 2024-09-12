# Typecasting = the process of converting a variable from one data type to  another
#               str(), int(), float(), bool()


name = "Darshi"
age = 24
gpa = 8.3
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


#lets do typecasting
gpa = int(gpa)
age = float (age)
age = str(age)

name = bool(name)

print(gpa)
print(age)
print(age) # answr will gonna appear as same i.e 25 but it is not an integer but an string
print(type(age))

age += "1" #cacncentaion of string with string 

print(age)
print(name)

