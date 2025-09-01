import math
import sys


def compound_interest(principal, rate, time):
    return principal * math.pow((1+(rate/100)), time) - principal

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def amount(value, principal, rate, time):
    if value == 'SI':
        return principal + simple_interest(principal, rate, time)
    elif value == "CI":
        return principal + compound_interest(principal, rate, time)
    else:
        return None

def rate(value, principal, time, amount=None, interest=None):
    if value == "CI" and amount is not None:
        return (math.pow((amount / principal), (1 / time)) - 1) * 100
    elif value == "SI" and interest is not None:
        return (interest * 100) / (principal * time)
    else:
        return None

def time(value, principal, rate, amount=None, interest=None):
    if value == "CI" and amount is not None:
        return math.log(amount / principal) / math.log(1 + rate/100)
    elif value == "SI" and interest is not None:
        return (interest * 100) / (principal * rate)
    else:
        return None

def principal(value, rate, time, amount=None, interest=None):
    if value == "CI" and amount is not None:
        return amount / math.pow((1 + rate/100), time)
    elif value == "SI" and interest is not None:
        return (interest * 100) / (rate * time)
    else:
        return None


def main():
    print("This is CI and SI Calculator")
    counter = 0
    while True:
        user_choice = input("""
CI or 1 To Calculate Compound Interest
SI or 2 to Calculate Simple Interest
A or 3 to Calculate Amount
P or 4 to Calculate Principal
R or 5 to Calculate Rate
T or 6 to Calculate Time
Press Enter to Exit:
""").strip().upper()
        
        if user_choice == '1' or user_choice == 'CI':
            try:
                CI = round(compound_interest(
                    principal=float(input("Enter Principal: ")),
                    rate=float(input("Enter Rate: ")),
                    time=float(input("Enter Time: "))
                ), 2)
                print("Compound Interest:", CI)
            except Exception as e:
                counter += 1
                print(e)

        elif user_choice == '2' or user_choice == 'SI':
            SI = round(simple_interest(
                principal=float(input("Enter Principal: ")),
                rate=float(input("Enter Rate: ")),
                time=float(input("Enter Time: "))
            ), 2)
            print("Simple Interest:", SI)

        elif user_choice == '3' or user_choice == 'A':
            value = input("1 for CI\n2 for SI: ").strip()
            if value == '1':
                amount_ci = round(amount("CI",
                                   principal=float(input("Enter Principal: ")),
                                   rate=float(input("Enter Rate: ")),
                                   time=float(input("Enter Time: "))), 2)
                print("Amount (CI):", amount_ci)

            elif value == '2':
                amount_si = round(amount("SI",
                                   principal=float(input("Enter Principal: ")),
                                   rate=float(input("Enter Rate: ")),
                                   time=float(input("Enter Time: "))), 2)
                print("Amount (SI):", amount_si)

            else:
                print("Invalid Choice")
                counter += 1

        elif user_choice == '4' or user_choice == 'P':
            value = input("1 for CI\n2 for SI: ").strip()
            if value == '1':
                p_ci = round(principal("CI",
                                 rate=float(input("Enter Rate: ")),
                                 time=float(input("Enter Time: ")),
                                 amount=float(input("Enter Amount: "))), 2)
                print("Principal (CI):", p_ci)

            elif value == '2':
                p_si = round(principal("SI",
                                 rate=float(input("Enter Rate: ")),
                                 time=float(input("Enter Time: ")),
                                 interest=float(input("Enter Interest: "))), 2)
                print("Principal (SI):", p_si)

            else:
                print("Invalid Choice")
                counter += 1

        elif user_choice == '5' or user_choice == 'R':
            value = input("1 for CI\n2 for SI: ").strip()
            if value == '1':
                r_ci = round(rate("CI",
                            principal=float(input("Enter Principal: ")),
                            time=float(input("Enter Time: ")),
                            amount=float(input("Enter Amount: "))), 2)
                print("Rate (CI):", r_ci)

            elif value == '2':
                r_si = round(rate("SI",
                            principal=float(input("Enter Principal: ")),
                            time=float(input("Enter Time: ")),
                            interest=float(input("Enter Interest: "))), 2)
                print("Rate (SI):", r_si)

            else:
                print("Invalid Choice")
                counter += 1

        elif user_choice == '6' or user_choice == 'T':
            value = input("1 for CI\n2 for SI: ").strip()
            if value == '1':
                t_ci = round(time("CI",
                            principal=float(input("Enter Principal: ")),
                            rate=float(input("Enter Rate: ")),
                            amount=float(input("Enter Amount: "))), 2)
                print("Time (CI):", t_ci)

            elif value == '2':
                t_si = round(time("SI",
                            principal=float(input("Enter Principal: ")),
                            rate=float(input("Enter Rate: ")),
                            interest=float(input("Enter Interest: "))), 2)
                print("Time (SI):", t_si)

            else:
                print("Invalid Choice")
                counter += 1

        elif user_choice == "":
            print("Exiting Calculator...")
            break

        else:
            print("Invalid Option")
            counter += 1

        if counter == 4:
            sys.exit("Sorry The program is ending")


if __name__ == "__main__":
    main()
