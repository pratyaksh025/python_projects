def int_to_roman(num):
    val_sym = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    if num<=0 or num>3999:
        return "Not A Valid Range"
    
    
    else:
        roman =""
        for value,symbol in val_sym:
            while num >= value:
                roman += symbol
                num -= value

    return roman

def roman_to_int(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    total=0
    prev_val=0
    for ch in reversed(roman.upper()):
        value= roman_map.get(ch,0)
        if value<prev_val:
            total-=value
        else:
            total+=value

        prev_val=value
    return total


def main():
    print("--Choose--")
    while True:
        print("""1. To Convert from Int to Roman
2. To Convert from Roman to Int
3. Exit
""")
        
        choice=input("Your Choice: ")
        if choice not in ['1','2','3']:
            print("Invalid Choice")
        
        elif choice == '1':
            roman=int_to_roman(int(input("Enter Value from (1 to 3999): ")))
            print(f"Roman Value: {roman}\n")
        
        elif choice == '2':
            number=roman_to_int(input("Enter Valid Roman Value: ")) 
            print(f"Numeric Value: {number}\n") 

        elif choice == '3':
            print("Thanks For Using The Program") 
            break

if __name__ == "__main__":
    main() 