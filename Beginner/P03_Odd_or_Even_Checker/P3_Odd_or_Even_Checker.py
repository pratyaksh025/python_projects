import re
import sys

def odd_or_even(number):
    if number % 2 == 0:
        return True
    
    return False
    
if (user := input("Enter A number to check: ")) and re.match(r"^[0-9.]+$",user):


    if odd_or_even(int(user)):
        print(f"{user} is an Even Number")

    else:
        print(f"{user} is an Odd Number")

else:
    sys.exit(f"Not A Valid Input: {user}")
    