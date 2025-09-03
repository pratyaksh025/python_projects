# 🔐 Caesar Cipher 

This project is an **encryption and decryption program** based on shifting characters in the ASCII set.  
Unlike the traditional Caesar cipher (A–Z only), this version supports **letters, digits, punctuation, and spaces**.  
It also includes an **interactive mode**, letting you try out encryption with your own messages.

---

## 📌 Features
- Encrypt and decrypt text using a shift (default or custom).
- Works with:
  - Uppercase & lowercase letters
  - Numbers (0–9)
  - Special characters (`!@#$%^&*()...`)
  - Spaces
- Interactive prompt:
  - Enter your own message
  - Choose your shift value (or use default)

---

## 📂 File
- `P20_Caesar_Cipher.py` → Contains the full encryption, decryption, and interactive logic.

---

## ⚙️ How It Works
1. Define a set of ASCII characters (letters, digits, symbols, space).
2. For encryption → shift forward.  
   For decryption → shift backward.
3. Supports both **fixed test case** and **user input mode**.

---

## ▶️ Example (Default Test Case)

```python
text = "Hello, World!"
enc = encrypt(text, shift=9)
dec = decrypt(enc, shift=9)

print("Original:", text)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

## 🖥️ Sample Output
```pgsql
Original: Hello, World!
Encrypted: Qnxxx5&f|axm(
Decrypted: Hello, World!
```

## ▶️ Interactive Mode

When you run the script, it will ask:

```yaml
Would You like to try (y/n)? y
Enter message: Python123!
tell us the skips if nothing entered program will use default value: 5
Encrypted: U~ymts678&
```
If you type `n`, the program exits with:

```rust
thanks for Using program
```

## 🚀 Try It Yourself

- Run the script.

- Enter a message of your choice.

- Provide a shift value (or leave blank for default).

- Get instant encryption!

## 📁 Project Structure
```
python_projects/
│
├── beginner/
│   ├── P20_Caesar_Cipher/
│   │   ├── P20_Caesar_Cipher.py
│   │   └── README.md
```

## Author
Made with ❤️ by Pratyaksh Yadav