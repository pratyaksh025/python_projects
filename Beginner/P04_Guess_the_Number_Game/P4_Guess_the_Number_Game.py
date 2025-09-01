import random
import re 
import sys


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
        
def main():
    print("Welcome to guess the number game")
    number,guess=game()
    print(f"{number} was the correct guess in total {guess} guesses")


if __name__ =="__main__":
    main()
