# Importing the random module which allows us to generate random numbers
import random

# Defining the range for the number guessing game: 
# 'lowest_num' is the minimum possible number, and 'highest_num' is the maximum possible number
lowest_num = 1
highest_num = 100

# Generating a random number between 'lowest_num' and 'highest_num' to be the correct answer
answer = random.randint(lowest_num, highest_num)

# Initializing a variable 'guesses' to keep track of how many guesses the player has made
guesses = 0

# A boolean flag 'is_running' to control the main game loop
is_running = True

# Printing a welcome message for the player
print("Py Number Guessing Game")

# Printing instructions to let the player know the range within which they should guess
print(f"Select a number between {lowest_num} and {highest_num}")

# Starting the game loop, which will continue to run while 'is_running' is True
while is_running:
    # Prompting the user to enter a guess and storing the input as a string in the 'guess' variable
    guess = input("Enter your guess: ")

    # Checking if the entered guess is a valid digit (i.e., not letters or special characters)
    if guess.isdigit():
        # Converting the valid guess from a string to an integer
        guess = int(guess)

        # Incrementing the 'guesses' variable by 1 to count the number of attempts made by the player
        guesses += 1

        # Checking if the guess is out of the defined range
        if guess < lowest_num or guess > highest_num:
            # Informing the player that their guess is out of range and prompting them to select a valid number
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        # Checking if the guess is lower than the correct answer
        elif guess < answer:
            # Informing the player that their guess is too low and prompting them to try again
            print("Too low! Try again!")

        # Checking if the guess is higher than the correct answer
        elif guess > answer:
            # Informing the player that their guess is too high and prompting them to try again
            print("Too high! Try again!")

        # If the guess is correct
        else:
            # Informing the player that they guessed correctly and displaying the correct answer
            print(f"Correct! The answer was {answer}")
            # Displaying the number of guesses the player made
            print(f"Number of guesses: {guesses}")
            
            # Setting 'is_running' to False, which will exit the game loop
            is_running = False

    # If the entered input is not a valid digit
    else:
        # Informing the player that their guess was invalid
        print("Invalid guess")
        # Prompting the player again to select a valid number within the specified range
        print(f"Please select a number between {lowest_num} and {highest_num}")
