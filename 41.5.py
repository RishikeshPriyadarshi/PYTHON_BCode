#Q. picking up random choice from sequence


   #choice()--> method is great use for games if we need random element

# Importing the random module which provides functions that generate random numbers and choices
import random 

# Defining two variables, 'low' and 'high', with integer values 1 and 100 respectively
# These variables are currently not used but might be intended for future operations
low = 1
high = 100

# Defining a tuple 'options' that contains the strings "rock", "paper", and "scissors"
# These represent the possible choices in a game of rock-paper-scissors
options = ("rock", "paper", "scissors")

# Using the random.choice() function to select a random element from the 'options' tuple
# This simulates choosing a random option from the given sequence (in this case, rock-paper-scissors)
option = random.choice(options)

# Printing the randomly selected option to the console
print(option)


