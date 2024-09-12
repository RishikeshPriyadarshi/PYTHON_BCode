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

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Print each dice result on a new line
for die in range(num_of_dice):
    print(f"Dice {die + 1}:")
    for line in dice_art[dice[die]]:
        print(line)
    print()  # Blank line between dice

#lets calculate the total, we need to iterate and sum all the elements witin our List, we can do tht with for-loop
for die in dice:
    total += die    

print(f"Total: {total}")
