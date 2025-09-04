# 🔢 Prime Factorization Program

A simple Python program that calculates and displays the **prime factors** of any positive integer.  
This project is great for understanding **loops, conditionals, input validation, and prime factorization logic**.

---

## 📌 Features
- Accepts user input and computes **only prime factors**.
- Handles numbers greater than 1 correctly.
- Allows continuous input until the user presses **Enter** to quit.
- Handles invalid inputs gracefully.

---

## ⚙️ How It Works
1. **`prime_factors(n)`**  
   - Finds all prime factors of `n`.  
   - Uses repeated division by 2, then checks odd numbers up to √n.  
   - Returns a list of prime factors.  

2. **`main()`**  
   - Runs an interactive loop.  
   - Accepts numbers as input, calculates their prime factors, and displays them.  
   - Exits when the user presses Enter.  

---

## ▶️ Example Usage

### Run the Program
```bash
python prime_factors.py
```

## Session Example

### Input

```yml
This Program is to get only Prime Factors of a number
Enter number: 155
```

### Output
```yml
Factors Are: 
5,31
```

## Invalid Number
### Input

```yml
This Program is to get only Prime Factors of a number
Enter number: py5
```

### Output
```yml
Invalid Number!
```

### Input

```yml
This Program is to get only Prime Factors of a number
Enter number: 
```

### Output
```yml
Thanks For Using the Program!
```

## 🧮 Example Prime Factorizations

- 28 → 2 × 2 × 7
- 45 → 3 × 3 × 5
- 97 → 97 (prime itself)

## 🚀 How to Run

1. Save the script as prime_factors.py.

2. Open a terminal or command prompt in the file’s directory.

3. Run:
   ```
    python prime_factors.py
   ```

## Author

Made with ❤️ by Pratyaksh Yadav 