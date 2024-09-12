import random  # Importing the random module, which allows us to use the `random.choice()` function later in the program.

# Since we are not going to change the options ("rock", "paper", "scissors"), we define them using a Tuple.
# Tuples are immutable, meaning their values cannot be changed after creation.
options = ("rock", "paper", "scissors")

# This variable controls whether the game is running or not.
# We set `running = True` initially to start the game loop.
running = True

# The game will keep running while `running` is True.
# This loop will allow the player to play multiple rounds until they decide to quit.
while running:

    # `player` is initialized as `None` to represent that the player has not yet chosen their move.
    player = None

    # The computer randomly selects one of the options: "rock", "paper", or "scissors" using `random.choice()`.
    # This function picks one item from the `options` tuple.
    computer = random.choice(options)

    # This inner loop ensures that the player's input is valid.
    # The loop will continue asking the player for a choice until the input matches one of the options in the tuple.
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()  # The `.lower()` ensures case insensitivity.

    # After exiting the inner loop, the player's choice and the computer's choice are displayed.
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # The following conditions check the game's rules to determine the winner:
    
    # Case 1: If the player's choice is the same as the computer's choice, the game is a tie.
    if player == computer:
        print("It's a tie!")

    # Case 2: The player wins if they choose "rock" and the computer chooses "scissors".
    elif player == "rock" and computer == "scissors":
        print("You win!")

    # Case 3: The player wins if they choose "paper" and the computer chooses "rock".
    elif player == "paper" and computer == "rock":
        print("You win!")

    # Case 4: The player wins if they choose "scissors" and the computer chooses "paper".
    elif player == "scissors" and computer == "paper":
        print("You win!")

    # If none of the previous conditions are met, it means the player lost the round.
    # The computer has won.
    else:
        print("You lose!")

    # After each round, the program asks if the player wants to play again.
    # The input is converted to lowercase to make the comparison case-insensitive.
    play_again = input("Play again? (y/n): ").lower()

    # If the player does not input "y" (i.e., any input other than "y"), we exit the loop by setting `running = False`.
    if not play_again == "y":
        running = False

# This message is printed once the loop has ended, meaning the player has chosen not to play again.
print("Thanks for Playing!")
