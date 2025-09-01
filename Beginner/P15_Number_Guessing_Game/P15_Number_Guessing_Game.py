import random
import time

levels = {
    "easy": {"range": 10, "attempts": 7},
    "medium": {"range": 50, "attempts": 5},
    "hard": {"range": 100, "attempts": 3}
}

level_choice = {
    "1": "easy",
    "2": "medium",
    "3": "hard"
}

def game():
    print(": Welcome To Number Guessing Game :")
    while True:
        choice_level = input("""
1 - Easy
2 - Medium
3 - Hard
Press Enter to quit
Your Input: """)

        if choice_level == "":
            print("Thanks for playing!!")
            break

        if choice_level in level_choice:
            get_key = level_choice[choice_level]
            attempts = levels[get_key]["attempts"]
            range_provided = levels[get_key]["range"]

            random_number = random.randint(1, range_provided)
            attempt_used = 0

            while attempt_used < attempts:
                try:
                    user_guess = int(input(f"Your Guess (1-{range_provided}): "))
                except ValueError:
                    print("Please enter a valid number!\n")
                    continue

                if user_guess < 1 or user_guess > range_provided:
                    print(f"Guess out of range! Enter between 1 and {range_provided}.")
                    continue  # don’t count invalid guesses

                attempt_used += 1
                if user_guess < random_number:
                    print("Higher number please!")
                elif user_guess > random_number:
                    print("Lower number please!")
                else:
                    print(f"Amazing! You Won in {attempt_used} attempts!")
                    break

                print(f"Attempts used: {attempt_used}/{attempts}\n")

            else:
                print(f"Out of attempts! The number was {random_number}")

            time.sleep(1)
            replay = input("\nDo you want to play again (y/n)? ").lower()
            if replay != "y":
                print("Thanks for playing!!")
                break

        else:
            print("Invalid choice, please select 1, 2, or 3.\n")

game()
