# Number Guessing Game

A **command-line Number Guessing Game** built in **Python**.  
Players try to guess a randomly generated number within a limited number of attempts based on difficulty levels.

---

## Features
- Three difficulty levels:
  - **Easy**: Number between 1–10, 7 attempts  
  - **Medium**: Number between 1–50, 5 attempts  
  - **Hard**: Number between 1–100, 3 attempts  
- Validates user input and ensures numbers are in the correct range.  
- Provides **hints**: tells if the guessed number should be higher or lower.  
- Tracks the number of attempts used.  
- Option to **replay** after each game.  

---

## Usage Example

```
: Welcome To Number Guessing Game :

1 - Easy
2 - Medium
3 - Hard
Press Enter to quit
Your Input: 1

Your Guess (1-10): 5
Higher number please!
Attempts used: 1/7

Your Guess (1-10): 8
Amazing! You Won in 2 attempts!

Do you want to play again (y/n)? n
Thanks for playing!!

1 - Easy
2 - Medium
3 - Hard
Press Enter to quit
Your Input: 3

Your Guess (1-100): 50
Lower number please!
Attempts used: 1/3
...
Out of attempts! The number was 72
```

## How It Works

1. **Difficulty Levels**:
   - Easy, Medium, and Hard define the **number range** and **maximum attempts**.  

2. **Game Loop**:
   - Prompts the player to select a difficulty.  
   - Generates a random number within the selected range.  
   - Player guesses the number, receiving hints if too high or too low.  
   - Game tracks the number of attempts and ends when:
     - The player guesses correctly, or  
     - Attempts run out.  

3. **Replay Option**:
   - After the game ends, the player can choose to play again or exit.  

---

## Author
Made with ❤️ by Pratyaksh Yadav

