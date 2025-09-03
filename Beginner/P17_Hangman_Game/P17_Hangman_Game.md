# Hangman Game 🎮  

This is a simple **Hangman game** built with Python. The program randomly selects a word, and the player has to guess it one letter at a time. The player wins if they guess all the letters before running out of tries.  

---

## How It Works  
1. The game picks a random word from a predefined list:  
   ```python
   ["python", "hangman", "developer", "programming"]
    ```
2. The word is displayed as underscores (`_`), one for each letter.
3. The player guesses one letter at a time.<br> 
   - If the guess is correct, the letter is revealed in its position(s).
   - If the guess is wrong, the number of tries decreases.

4. The player starts with 6 tries.
5. The game ends when:<br>
    - The player successfully guesses all letters (Win 🎉)
    - The tries run out (Lose ❌)

## Example Gameplay
``` yaml
Word:  _ _ _ _ _ _
Tries left: 6
Enter a letter: a

Word:  _ a _ _ _ a _
Tries left: 6
Enter a letter: z
Wrong! Tries left: 5
```

## Features

- Random word selection.<br>
- Input validation (only single letters allowed).<br>
- Prevents duplicate guesses.<br>
- Tracks remaining tries.<br>
- Clear win/lose messages.

## How to Run

1. Make sure Python is installed on your system.

2. Save the script as P17_Hangman_Game.py.

3. Run the file using:
        
    ```
        python P17_Hangman_Game.py
    ```
## Author
Made with ❤️ by Pratyaksh Yadav