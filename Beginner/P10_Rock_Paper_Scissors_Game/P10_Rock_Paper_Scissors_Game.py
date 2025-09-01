import secrets

def game():
    list_choice = ["1", "2", "3"]
    choice_dict = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }

    comp_point = 0
    user_point = 0
    no_of_play = 1

    while no_of_play <= 10:
        user_choice = input("""Choose:
1 or Rock
2 or Paper
3 or Scissors
> """)

        
        if user_choice not in choice_dict and user_choice not in ["Rock","Paper","Scissors"]:
            print("Invalid choice! Try again.")
            continue

        
        if user_choice in choice_dict:
            user_choice = choice_dict[user_choice]

        com_choice = choice_dict[secrets.choice(list_choice)]
        print(f"Computer chose: {com_choice}")

        # Logic
        if user_choice == com_choice:
            print("Draw!!")

        elif (user_choice == "Rock" and com_choice == "Scissors") or \
             (user_choice == "Paper" and com_choice == "Rock") or \
             (user_choice == "Scissors" and com_choice == "Paper"):
            print("You Won")
            user_point += 1

        else:
            print("Computer Won")
            comp_point += 1

        no_of_play += 1


    print("\nFinal Result:")
    if user_point > comp_point:
        print("You Won The Game")
    elif user_point < comp_point:
        print("Computer Won The Game")
    else:
        print("The Session Was a Draw!")


game()