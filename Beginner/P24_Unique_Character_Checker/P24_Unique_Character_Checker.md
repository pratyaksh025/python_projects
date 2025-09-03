# 🔤 Unique Character Checker

This Python program checks whether a given string contains **all unique characters**.  
It provides an interactive interface for users to test multiple strings until they decide to quit.

---

## 📌 Features
- Check if a string has all unique characters.
- Interactive mode: continuously allows user input until they press Enter to quit.
- Handles any text including letters, numbers, and symbols.

---

## ⚙️ How It Works
1. The user enters a string.
2. The program iterates through each character and keeps track of seen characters using a **set**.
3. If a character repeats, the program outputs that the string does **not** have all unique characters.
4. Otherwise, it confirms that all characters are unique.
5. Repeat until the user presses Enter without typing a string.

---

## ▶️ Example Usage

```rust
*********************************************************************
This Program Checks if the entered string has all unique character.
*********************************************************************

To Quit Press Enter
Enter Text: hello

Entered text doesn't have all unique text

*********************************************************************
This Program Checks if the entered string has all unique character.
*********************************************************************

To Quit Press Enter
Enter Text: world

Has all unique characters

*********************************************************************
This Program Checks if the entered string has all unique character.
*********************************************************************

To Quit Press Enter
Enter Text:
*********************
Thank You for Using
*********************

```

## 🚀 How to Run
1. Save the script as `unique_char_checker.py`.
2. Run using Python:
   ```bash
   python unique_char_checker.py
   ```
3. Enter any text to check for uniqueness or press Enter to exit.

## 💡 Notes

- Works with letters, numbers, symbols, and spaces.

- Useful for validating passwords or identifying strings with repeated characters.

## Author
Made with ❤️ by Pratyaksh Yadav