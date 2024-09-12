age = int(input("Enter the age: "))

if age>=100:
    print("You r too old to sign up!")      
elif age>=18:
    print("You r signed up! ")
elif  age<0:
    print("You r not born yet! ")
else:
    print("You r not 18+ ")    