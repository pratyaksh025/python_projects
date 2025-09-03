def convert_all_bases(num_str, from_base):
    try:
        decimal_num = int(num_str, from_base)
        
    except ValueError:
        return None  
    
    return {
        "Decimal": str(decimal_num),
        "Binary": bin(decimal_num)[2:],
        "Octal": oct(decimal_num)[2:],
        "Hexadecimal": hex(decimal_num)[2:].upper()
    }

base_map = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hex": 16
}


while True:
    num_str = input("Enter the number (or 'exit' to quit): ").strip()
    if num_str.lower() == "exit":
        break
    
    from_base_name = input("From (binary/oct/decimal/hex): ").strip().lower()
    if from_base_name not in base_map:
        print("Invalid base! Try again.\n")
        continue
    
    result = convert_all_bases(num_str, base_map[from_base_name])
    if result is None:
        print(f"Invalid number '{num_str}' for base {from_base_name}.\n")
        continue
    
    print("\nConverted Numbers:")
    for base_name, value in result.items():
        print(f"{base_name}: {value}")
    print()
