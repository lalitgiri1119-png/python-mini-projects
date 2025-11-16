import random

def number_guessing_game():
    """
    A number guessing game where the computer picks a random number
    and the user tries to guess it.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("-" * 40)
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize game variables
    attempts = 0
    max_attempts = 7
    guessed_correctly = False
    
    # Main game loop
    while attempts < max_attempts and not guessed_correctly:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                guessed_correctly = True
                print(f"*** Congratulations! You guessed it correctly! ***")
                print(f"The number was {secret_number}")
                print(f"You won in {attempts} attempts!")
                
            elif guess < secret_number:
                print("^ Too low! Try a higher number.")
                
            else:  # guess > secret_number
                print("v Too high! Try a lower number.")
                
            # Show remaining attempts
            if not guessed_correctly and attempts < max_attempts:
                remaining = max_attempts - attempts
                print(f"You have {remaining} attempt(s) left.")
                
        except ValueError:
            print("X Please enter a valid number!")
            attempts += 1
            if attempts < max_attempts:
                remaining = max_attempts - attempts
                print(f"You have {remaining} attempt(s) left.")
    
    # Game over - check if player lost
    if not guessed_correctly:
        print(f"\n*** Game Over! You've used all {max_attempts} attempts. ***")
        print(f"The number I was thinking of was {secret_number}")
    
    print("-" * 40)

def play_again():
    """Ask if the player wants to play again"""
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

def main():
    """Main function to run the game with replay option"""
    print("*** Number Guessing Game ***")
    
    # Game loop with replay option
    while True:
        number_guessing_game()
        
        if not play_again():
            print("\nThanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()