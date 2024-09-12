#While loop = will execute some code WHILE some condns remains true

name  = input("Enter ur name: ")

while name == "":
    print("You did not enter ur name: ")
    name = input("Enter ur name: ")#Reprompting the user to enter the name, it will give the loop way to escape or 
                                   #break out from the infinite-loop
print(f"Hello {name}")    
