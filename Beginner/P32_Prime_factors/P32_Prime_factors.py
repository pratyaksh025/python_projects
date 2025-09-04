def prime_factors(n):
    factors = []
    
    if n <= 1:
        return factors

    while n%2==0:
        factors.append(2)
        n=n//2

    i=3
    while (i*i)<=n:
        while n%i==0:
            factors.append(i)
            n//=i
        i+=2

    if n>2:
        factors.append(n)
    return factors


def main():
    print("This Program is to get only Prime Factors of a number")
    while True:
        user_input= input("Enter number: ").strip()

        if user_input.isdigit():
            factors=prime_factors(int(user_input))
            print("Factors Are: ")
            print(",".join(map(str,factors)))
        elif user_input == "":
            print("Thanks For Using the Program!")
            break

        else:
            print("Invalid Number!")


if __name__ == "__main__":
    main()

