# 🔐 Password Strength Checker

A Python program to check the **strength of a password** based on industry-standard rules.  
It uses **regular expressions** to validate different aspects of the password and provides feedback:  
- **Strong Password**
- **Medium Password**
- **Weak Password**

---

## 📌 Features
- Checks password strength based on:
  - Minimum length of **8 characters**  
  - At least **1 uppercase letter**  
  - At least **1 lowercase letter**  
  - At least **1 digit**  
  - At least **1 special character**  
- Uses `getpass` for **hidden password input** (nothing visible while typing).  
- Exits gracefully when the user presses **Enter** without typing.  
- Stops automatically when a **Strong Password** is entered.  

---

## ⚙️ How It Works
1. The user enters a password (input is hidden).
2. The program validates it against multiple rules:
   - ✅ Strong → Meets all rules.  
   - ⚠️ Medium → Meets most rules (length + digits + upper/lower).  
   - ❌ Weak → Anything else.  
3. Displays feedback and continues until:
   - User presses **Enter** → exit.  
   - A **Strong Password** is entered → exit with success message.  

---

## ▶️ Example Usage

### Run the Program
```bash
python password_checker.py
```

## Sample Session

```yml
Password Strength Checker
(Press Enter without typing to exit)

Enter password to check: ********
Strength: Weak Password

Enter password to check: Abcd1234
Strength: Medium Password

Enter password to check: Abcd1234!
Strength: Strong Password
This password is strong!
Thanks for choosing this program.
```

## 🚀 How to Run

1. Save the script as password_checker.py.

2. Open terminal or command prompt in the script’s directory.

3. Run:
   ```bash
   python password_checker.py
   ```

## 🛡️ Notes

- Avoid using easily guessable passwords (like Password123!).

- A strong password should be long, unique, and random.

## Author

Made with ❤️ by Pratyaksh Yadav