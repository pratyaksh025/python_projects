import re 
import sys

def prime(number):
    prime_var=False
    if number<=1:
        return prime_var
    if number <=3:
        prime_var=True
        return prime_var
    elif number%2==0 or number % 3 == 0:
        return prime_var
    
    else:
        i=5
        while (i*i)<=number:
            if number%i ==0 or number%(i+2)==0:
                return prime_var
        prime_var=True

    return prime_var

def get_number(max_digits=20):
    """Restrict user input by max digits."""
    while True:
        num_str = input(f"Enter a number (up to {max_digits} digits): ")
        if not num_str.isdigit():
            print("Please enter digits only.")
            continue
        if len(num_str) > max_digits:
            print(f"Number too long! Please enter up to {max_digits} digits.")
            continue
        return int(num_str)

number=get_number(10)
check=prime(number)
if check:
    print(f"{number} is prime")
else:
    print(f"{number} is not a prime")

            
        
    
