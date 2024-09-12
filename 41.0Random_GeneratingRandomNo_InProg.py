   #random --> module gives access lots of useful  methods involving random number

import random 

 # Importing the random module which provides functions that generate random numbers
import random

# help(random) --> This is a function that, if uncommented, will display the documentation 
# for the 'random' module, listing all available functions and their descriptions.
# Uncomment the line below to see the documentation.
# print(help(random))

# Using the randint function from the random module to generate a random whole integer
# between 1 and 6 (inclusive). This simulates rolling a 6-sided dice.
number = random.randint(1, 6)

# Printing the randomly generated number (the result of the dice roll).
print(number)
