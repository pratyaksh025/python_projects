# Prime Number Checker

A simple Python program to check whether a given number is prime.

---

## Features
- Check if a number is prime using an efficient algorithm.
- Handles numbers greater than 1.
- Validates input to ensure only numeric values are accepted.
- Limits number length based on user preference.
- Provides clear messages for invalid input.

---

## Usage Example

```
Enter a number (up to 10 digits): 17
17 is prime

Enter a number (up to 10 digits): 20
20 is not a prime
```


**Invalid Input Example:**
```
Enter a number (up to 10 digits): abc
Please enter digits only.

Enter a number (up to 10 digits): 12345678901
Number too long! Please enter up to 10 digits.
```
## How It Works

### `prime(number)`
- Numbers ≤ 1 are not prime.
- Numbers 2 and 3 are automatically prime.
- Eliminates multiples of 2 and 3 early.
- Uses a loop starting from 5 to check divisibility efficiently using the 6k ± 1 method.
- Returns True if the number is prime, False otherwise.

### `get_number(max_digits)`
- Prompts user input until a valid number is entered.
- Ensures the input consists of digits only.
- Checks that the number does not exceed the maximum allowed digits.
- Returns the number as an integer.

---

## Author
Made with ❤️ by Pratyaksh Yadav
