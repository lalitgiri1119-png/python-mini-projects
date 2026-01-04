# Number Guessing Game

A simple Python number guessing game that demonstrates the use of loops, random number generation, and user input.

## Game Description

The computer picks a random number between 1 and 100, and you have to guess it! You get 7 attempts to find the correct number. After each guess, the game will tell you if your guess is too high or too low.

## Features

- Random number generation (1-100)
- Input validation
- Limited attempts (7 tries)
- Helpful hints (too high/too low)
- Play again option
- Clean, user-friendly interface with emojis

## Concepts Demonstrated

- **Loops**: `while` loop for the main game logic and replay functionality
- **Random**: `random.randint()` to generate the secret number
- **Input**: `input()` to get user guesses and choices
- **Exception Handling**: `try/except` for input validation
- **Functions**: Modular code organization
- **Conditional Statements**: `if/elif/else` for game logic

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory:
   ```
   cd number_guessing_game_project
   ```
3. Run the game:
   ```
   python number_guessing_game.py
   ```

## Game Rules

1. The computer selects a random number between 1 and 100
2. You have 7 attempts to guess the number
3. After each guess, you'll get a hint:
   - "Too low!" if your guess is less than the secret number
   - "Too high!" if your guess is greater than the secret number
   - "Congratulations!" if you guess correctly
4. If you use all 7 attempts without guessing correctly, the game reveals the number
5. You can choose to play again after each game

## Example Gameplay

```
🎮 Number Guessing Game 🎮
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess what it is?
----------------------------------------

Attempt 1/7 - Enter your guess: 50
📉 Too high! Try a lower number.
You have 6 attempt(s) left.

Attempt 2/7 - Enter your guess: 25
📈 Too low! Try a higher number.
You have 5 attempt(s) left.

Attempt 3/7 - Enter your guess: 37
🎉 Congratulations! You guessed it correctly!
The number was 37
You won in 3 attempts!
----------------------------------------
Do you want to play again? (yes/no): no

Thanks for playing! Goodbye! 👋
```

## Code Structure

- `number_guessing_game()`: Main game logic
- `play_again()`: Handles replay functionality
- `main()`: Entry point and game loop
- Input validation and error handling throughout

Enjoy the game! 🎉