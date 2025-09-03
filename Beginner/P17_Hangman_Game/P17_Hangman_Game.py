import random

words = ["python", "hangman", "developer", "programming"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6
used_letters = []

while tries > 0 and "_" in guessed:
    print("Word: ", " ".join(guessed))
    print("Tries left:", tries)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Try again.")
        continue
    if guess in used_letters:
        print("Already guessed!")
        continue
    
    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        tries -= 1

if "_" not in guessed:
    print("You win! Word was:", word)
else:
    print("You lose! Word was:", word)
