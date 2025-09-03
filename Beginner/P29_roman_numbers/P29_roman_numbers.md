# 🏛️ Roman Numeral Converter

This Python program allows you to **convert between integers and Roman numerals** interactively.  
It supports numbers from **1 to 3999** and validates Roman numeral inputs.

---

## 📌 Features
- Convert **Integer → Roman Numeral** (1–3999).
- Convert **Roman Numeral → Integer**.
- Interactive menu with input validation.
- Handles both uppercase and lowercase Roman numeral inputs.

---

## ⚙️ How It Works
1. User selects an option:
   - **1** → Convert integer to Roman numeral.
   - **2** → Convert Roman numeral to integer.
   - **3** → Exit the program.
2. For integer conversion:
   - Program checks if the number is in the valid range (1–3999).
   - Converts using standard Roman numeral rules.
3. For Roman numeral conversion:
   - Program parses the numeral from right to left.
   - Adds or subtracts values according to Roman numeral rules.
4. Displays the converted value.
5. Continues until the user chooses to exit.

---

## ▶️ Example Usage

### Integer to Roman
```yml
--Choose--
1. To Convert from Int to Roman
2. To Convert from Roman to Int
3. Exit

Your Choice: 1
Enter Value from (1 to 3999): 589
Roman Value: DLXXXIX
```
### Roman to Integer
```yml
1. To Convert from Int to Roman
2. To Convert from Roman to Int
3. Exit

Your Choice: 2
Enter Valid Roman Value: DLXxxIX
Numeric Value: 589
```
### Exit
```yml
1. To Convert from Int to Roman
2. To Convert from Roman to Int
3. Exit

Your Choice: 3
Thanks For Using The Program
```



---

## 🚀 How to Run
1. Save the script as `roman_converter.py`.
2. Run using Python:
   ```bash
   python roman_converter.py
   ```
3. Follow the interactive menu to convert numbers.

## 💡 Notes

- Accepts Roman numerals in uppercase or lowercase.

- Integer inputs must be between 1 and 3999.

- Useful for educational purposes or historical data representation.


## Author

Made with ❤️ by Pratyaksh Yadav