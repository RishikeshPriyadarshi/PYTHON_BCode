'''
                       Dice Roller Program
    
>if we r going to create ASCCII-art , we will be utilising some UNICODE characters

> to enter the UNICODE charcaters it really varies depending upon our  operating-systems
     Bt the easiest way to do this to use Python

> to enter a UNICODE character entr a forward-slash("\") then given code for each charcater
      print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
      
          //output-> ● ┌ ─ ┐ │ └ ┘
          

'''


import random


#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")  #it will give the symbols as output below
    #● ┌ ─ ┐ │ └ ┘   #--> these r the UNICODE chars we will need to build the ASCII-art i.e. dice

#Each die will be made of 5-lines

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

#here we hv created a dictionary called  'dice art'--> our dictonry made up of key-value pairs , key will bw value from 1 to 6
#value will be a tuple
dice_art = {

    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),

        
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),


    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")                
    
}

#Let's create a list of dice --> our dice will be numbers randomly generated b/w 1 and 6
dice = []

total = 0

num_of_dice = int(input("how many dice?: "))

'''
#to generate a random number we can write randint()--> method of the random module
random.randint(1,6)

#then we need to append the above line in the dice.append()--> method  , we can move the abv line in the append method
dice.append(random.randint(1,6))

      #we need to do the number of times depending on how many dice user enters , so "so we can place the above line the for-loop"
for die in range(num_dice):
    dice.append(random.randint(1,6))

print()            

'''
for die in range(num_of_dice):
    dice.append(random.randint(1,6))


#Here we will display our ASCII art ---> the easiest way should be to create some nested-for-loop
   #the outer for loop will be the incharge of no. of dice
for line in range(5):  # We have 5 lines in each dice's ASCII art
    for die in range(num_of_dice):
        print(dice_art[dice[die]][line], end=" ")  # Print each line from each dice side by side
    print()  # Move to the next line after printing one line for all dice


#lets calculate the total, we need to iterate and sum all the elements witin our List, we can do tht with for-loop
for die in dice:
    total += die    

print(f"total: {total}")




          