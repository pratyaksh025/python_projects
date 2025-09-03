def unique_char(text):
    seen = set()
    for i in text:
        if i in seen:
            return False
        seen.add(i)
    return True


while True:
    welcome="This Program Checks if the entered string has all unique character."
    print("*"*(len(welcome)+2))
    print(welcome)
    print("*"*(len(welcome)+2))
    thanks="Thank You for Using"

    user=input("\nTo Quit Press Enter\nEnter Text: ")
    if user:
        if unique_char(user):
            print("\nHas all unique characters")
        else:
            print("\nEntered text doesn't have all unique text\n")
    else:
        print("*"*(len(thanks)+2))
        print(thanks)
        print("*"*(len(thanks)+2))
        break

