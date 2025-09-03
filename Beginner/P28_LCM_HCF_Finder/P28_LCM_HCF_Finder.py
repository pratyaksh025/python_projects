import math 
from functools import reduce


def lcm_of_two(a,b):
    return (a*b)// math.gcd(a,b)

numbers=[]

print("Enter Numbers below when Done press enter to calculate HCF and LCM")
while True:
    number=input("number: ")

    if number.strip('-').isnumeric():
        numbers.append(int(number))
    elif number == "":
        print("Input Captured")
        break
    else:
        print("Invalid Input❌")


if not numbers:
    print("No numbers were inserted")

elif len(numbers)<2:
    print("Atleast Two numbers Required")

else:
    hcf= reduce(math.gcd,numbers)
    lcm=reduce(lcm_of_two,numbers)

    print(" Results ")
    print(f"LCM: {lcm}\nHCF: {hcf}")

    