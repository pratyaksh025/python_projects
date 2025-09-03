# 🧮 HCF & LCM Calculator (Enhanced)

This Python program calculates the **HCF (Highest Common Factor)** and **LCM (Least Common Multiple)** of multiple numbers entered by the user.  
It includes input validation and requires at least **two numbers** to perform calculations.

---

## 📌 Features
- Accepts **any number of integers**, including negative numbers.
- Calculates:
  - **HCF** using `math.gcd` and `functools.reduce`.
  - **LCM** using a custom pairwise LCM function.
- Interactive input with validation.
- Notifies the user if input is invalid or if fewer than two numbers are provided.

---

## ⚙️ How It Works
1. User enters numbers one by one.
2. Press Enter on an empty input to stop entering numbers.
3. Program checks:
   - If no numbers were entered → displays a message.
   - If fewer than two numbers → prompts that at least two are required.
4. Calculates **HCF** using `reduce` with `math.gcd`.
5. Calculates **LCM** using a custom `lcm_of_two` function reduced over all numbers.
6. Displays the results neatly.

---

## ▶️ Example Usage

### Input:
```yml
Enter Numbers below when Done press enter to calculate HCF and LCM
number: 5
number: 10
number: 15
number: 
Input Captured
```

### Output:
```yml
 Results
LCM: 30
HCF: 5
```


---

## 🚀 How to Run
1. Save the script as `hcf_lcm_calculator.py`.
2. Run using Python:
   ```bash
   python hcf_lcm_calculator.py
   ```
3. Enter numbers one by one and press Enter when done.


## 💡 Notes

- At least two numbers are required for calculation.

- Handles negative numbers as well.

- Useful for problems related to factors, multiples, and number theory.


## Author

Made with ❤️ by Pratyaksh Yadav