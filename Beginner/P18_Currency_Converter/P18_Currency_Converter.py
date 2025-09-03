# Fixed exchange rates (relative to INR)
rates = {
    "INR": 1,
    "USD": 88.05,
    "EUR": 102.37,
    "GBP": 117.64
}

def convert(amount, from_currency, to_currency):
    if from_currency not in rates or to_currency not in rates:
        return None
    
    in_inr = amount * rates[from_currency]
    result = in_inr / rates[to_currency]
    return result


while True:
    print("\nAvailable currencies: INR, USD, EUR, GBP")
    from_currency = input("From: ").upper()
    to_currency = input("To: ").upper()
    amount = float(input("Enter amount: "))

    converted = convert(amount, from_currency, to_currency)
    if converted is None:
        print("Invalid currency!")
    else:
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")

    again = input("Convert again? (y/n): ").lower()
    if again != 'y':
        print("Thanks For Using")
        break
