# import random
import re
import sys
import string
import secrets

def generate_dummy_pass(length=12):
    char= string.ascii_letters +string.punctuation+string.digits
    return ''.join(secrets.choice(char) for _ in range(length))


def password_check(password):
    length_check = re.search(r".{8,}",password)
    digit= re.search(r"\d",password)
    upper= re.search(r"[A-Z]",password)
    lower= re.search(r"[a-z]",password)
    symbols = re.search(r"[.,/@_#$&]",password)

    if all([length_check,digit,upper,lower,symbols]):
        return "Strong"
    elif digit or symbols:
        return "Medium"
    else:
        return 'weak'


passw=generate_dummy_pass(10)
print(passw)
print(password_check(passw))
# print()