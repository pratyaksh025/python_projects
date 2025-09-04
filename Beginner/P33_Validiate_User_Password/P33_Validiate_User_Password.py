import re
import getpass

def validate_pass(password):
    length_check = re.search(r".{8,}", password)
    upper_check = re.search(r"[A-Z]", password)
    lower_check = re.search(r"[a-z]", password)
    digit_check = re.search(r"\d", password)
    special_check = re.search(r"[^\w\s]", password)  # any special character

    if all([length_check, upper_check, lower_check, digit_check, special_check]):
        return 'Strong Password'
    elif length_check and (upper_check or lower_check) and digit_check:
        return 'Medium Password'
    else:
        return 'Weak Password'


def main():
    print("Password Strength Checker\n(Press Enter without typing to exit)\n")
    while True:
        # use getpass instead of input()
        user_password = getpass.getpass("Enter password to check: ").strip()

        if user_password == "":
            print("Thank you for using the Password Checker!")
            break

        status = validate_pass(user_password)
        print(f"Strength: {status}\n")

        if status == "Strong Password":
            print("This password is strong!\nThanks for choosing this program.\n")
            break


if __name__ == "__main__":
    main()
