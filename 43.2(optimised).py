import random  # Import the random module to allow the computer to make random choices.

# Define a tuple containing the valid choices for the game.
OPTIONS = ("rock", "paper", "scissors")

def get_computer_choice():
    """Return a random choice for the computer from the OPTIONS tuple."""
    return random.choice(OPTIONS)  # Select and return a random choice from the OPTIONS tuple.

def get_player_choice():
    """Prompt the player to enter a choice and validate it."""
    while True:  # Loop until a valid choice is entered.
        choice = input("Enter a choice (rock, paper, scissors): ").lower()  # Prompt the player and convert input to lowercase.
        if choice in OPTIONS:  # Check if the player's choice is valid.
            return choice  # If valid, return the choice and exit the loop.
        print(f"Invalid choice. Please choose from {', '.join(OPTIONS)}.")  # Inform the player of the invalid choice and prompt again.

def determine_winner(player, computer):
    """Determine the result of the game based on the player's and computer's choices."""
    if player == computer:  # If both choices are the same, it's a tie.
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):  # Check for winning conditions.
        return "You win!"
    else:  # If none of the winning conditions are met, the player loses.
        return "You lose!"

def play_game():
    """Play a single round of the game."""
    player_choice = get_player_choice()  # Get the player's choice by calling the get_player_choice function.
    computer_choice = get_computer_choice()  # Get the computer's choice by calling the get_computer_choice function.
    
    print(f"Player: {player_choice}")  # Display the player's choice.
    print(f"Computer: {computer_choice}")  # Display the computer's choice.
    
    result = determine_winner(player_choice, computer_choice)  # Determine the result of the game.
    print(result)  # Display the result to the player.

def main():
    """Main function to control the game loop."""
    print("Welcome to Rock, Paper, Scissors!")  # Greet the player and introduce the game.
    while True:  # Loop to allow multiple rounds of the game.
        play_game()  # Call the play_game function to play a round of the game.
        play_again = input("Play again? (y/n): ").strip().lower()  # Ask the player if they want to play again and handle input case-insensitively.
        if play_again != "y":  # If the player does not input "y", break the loop to end the game.
            break
    
    print("Thanks for playing!")  # Thank the player for playing the game when they choose to exit.

if __name__ == "__main__":  # Ensure that the following code runs only if the script is executed directly, not if imported as a module.
    main()  # Call the main function to start the game.
