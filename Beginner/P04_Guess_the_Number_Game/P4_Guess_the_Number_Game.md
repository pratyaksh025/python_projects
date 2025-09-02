# Guess the Number Game

A simple **command-line Guess the Number Game** built in **Python**.


## Features
- Takes user input. 
- Ensures correct input format with regex validation.
- generates a random number
- counts the number of attempt used by player
- if number is greater than the number to be guessed game hints the player saying higher number please and vice versa


## Usage Example

```
Welcome to guess the number game
Enter your guess(1-100): 45
Lower Number Please
Enter your guess(1-100): 32

32 was the correct guess in total 2 guesses


```

If user tries to input anything except number:
```
Enter your guess(1-100): A5
A5 is not a valid input!!!
```
and with the message ends the game immediately
## Code Explaination

**Function `game` :**
- Allows user to make a guess
- stores the random number generated for the session
- if user guesses the number correctly returns total gueses and number

```python
def game():
    random_number = random.randint(1,101)
    no_of_guesses=1
    while True:

        if (user_input := input("Enter your guess(1-100): ")) and re.match(r"^[0-9]+$",user_input):
           guess= int(user_input)
        
        else:
            sys.exit(f"{user_input} is not a valid input!!!")

        if guess>random_number:
            print("Lower Number Please")
            no_of_guesses+=1
        
        elif guess<random_number:
            print("Higher Number Please")
            no_of_guesses+=1

        else:
            return guess,no_of_guesses

```
**Function `main` :**
- Displays the welcome message
- Displays the winning message with number of guesses and correct number 

``` python
def main():
    print("Welcome to guess the number game")
    number,guess=game()
    print(f"{number} was the correct guess in total {guess} guesses")
```

## Author:
Made with ❤️ by Pratyaksh Yadav
 