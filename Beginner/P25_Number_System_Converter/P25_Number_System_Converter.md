# 🔢 Base Converter

This Python program converts a number from one base to **all other common bases**:  
- Decimal  
- Binary  
- Octal  
- Hexadecimal  

It supports user input in **binary, octal, decimal, or hexadecimal** format.

---

## 📌 Features
- Convert numbers between **binary, octal, decimal, and hexadecimal**.
- Interactive mode: continuously allows multiple conversions until the user exits.
- Validates input to ensure it matches the selected base.

---

## ⚙️ How It Works
1. The user enters a number.
2. The user selects the **base of the input number** (`binary`, `oct`, `decimal`, or `hex`).
3. The program converts the number into all other bases.
4. Displays the results neatly.

---

## ▶️ Example Usage

```yml
Enter the number (or 'exit' to quit): 10
From (binary/oct/decimal/hex): decimal

Converted Numbers:
Decimal: 10
Binary: 1010
Octal: 12
Hexadecimal: A

Enter the number (or 'exit' to quit): exit

Enter the number (or 'exit' to quit): 1F
From (binary/oct/decimal/hex): hex

Converted Numbers:
Decimal: 31
Binary: 11111
Octal: 37
Hexadecimal: 1F


```

## 🚀 How to Run
1. Save the script as `base_converter.py`.
2. Run using Python:
   ```bash
   python base_converter.py
   ```
3. Enter numbers and choose the input base for conversion.

4. Type `exit` to quit the program.


## 💡 Notes

- Input is case-insensitive for hexadecimal digits.

- Invalid input for the selected base is handled gracefully.

## Author

Made with ❤️ by Pratyaksh Yadav