#Number Guessing Game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0

is_running = True

print("Py Number Guessing Game ")

print("select a number b/w {lowest_num} and {highest_num}")


#while is_running == True:
while is_running:
    guess = input("Enter ur guess: ")

    if guess.isdigit():
        guess = int(guess)

        guesses += 1

        if guess <lowest_num or guess>highest_num:
            print("That number is out og range ")
            print(f"pls! select a number b/w {lowest_num} and {highest_num} ")

        elif guess < answer:
            print("Too low! Try again!")    

        elif guess > answer:
            print("Too high! Try again! ")  

        else:
            print(f"Correct! The answer was {answer}")      
            print(f"Number of guesses: {guesses}")

            is_running = False
    else:
        print("Invalid guess")
        print(f"pls! select a number b/w {lowest_num} and {highest_num}")