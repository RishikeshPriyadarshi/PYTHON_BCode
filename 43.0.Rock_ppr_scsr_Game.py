
import random

#since we r not going to change the option therefore we will  be using Tuple
options = ("rock", "paper", "scissors")

running = True

#while running == True:
while running:

    player = None

    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock,paper,scissors):")
        
    print(f"Player: {player}")
    print(f"Computer : {computer}")

    if(player == computer):
        print ("it's a tie! ")

    elif player == "rock" and computer == "scissors":
        print("you win!")

    elif player == "rock"  and computer == "paper":
        print("you win!")

    elif player == "scissors" and computer == "paper":
        print("you win!")


    else:
        print("you loose!")


    #play_again = input("play again? (y/n): ").lower()
    #if not play_again == "y":
    #    running = False 
           #The above can also be written as:
    if not input("play again? (y/n) ").lower() == "y":
        running = False    
    

print("Thanks for Playing! ")
