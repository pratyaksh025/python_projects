# Random Password Generator & Strength Checker

A simple **Python program** to generate **strong random passwords** and check their strength.

---

## Features
- Generate a **random password** with letters, digits, and symbols.
- Check the **strength of any password** (`Strong`, `Medium`, `Weak`).
- Ensures passwords meet **basic security requirements**:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one symbol (`.,/@_#$&`)

---

## Usage Example

```python
# Generates a random password of length 10
passw = generate_dummy_pass(10)
print(passw)

# Checks the strength of the generated password
print(password_check(passw))
```
**Sample Output:**
```
G7#kP2@wQ!
Strong
```

If a password doesn’t meet all the criteria, the checker gives feedback:
```
hello123
Medium
```

## How It Works

### `generate_dummy_pass(length)`
Generates a random password of the specified length using letters, digits, and symbols.

### `password_check(password)`
Checks if the password meets the following criteria:

- Has at least **8 characters**  
- Contains at least **one uppercase letter**  
- Contains at least **one lowercase letter**  
- Contains at least **one digit**  
- Contains at least **one symbol** (`.,/@_#$&`)

Returns **"Strong"**, **"Medium"**, or **"Weak"** depending on the criteria met.

## Why Use This

- Quickly generate secure passwords for accounts or apps.

- Instantly check if a password is strong enough.

- Helps improve your password hygiene in a simple way.



## Author
Made with ❤️ by Pratyaksh Yadav