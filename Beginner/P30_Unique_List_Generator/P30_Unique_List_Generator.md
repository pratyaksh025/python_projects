# 🗑️ Duplicate Remover (List Cleaner)

This Python program removes **duplicate values** from a list while keeping the **original order** of elements.

---

## 📌 Features
- Accepts a list of numbers or strings.
- Removes **duplicates** while preserving order.
- Handles **empty input** gracefully (shows `Nothing Was Inserted`).
- Works with both **numeric and text values**.

---

## ⚙️ How It Works
1. User enters values inside `[]` separated by commas.  
   Example:  
    ```yml
    [1, 2, 2, 3, apple, apple, 4]
    ```
2. Program checks if input is empty:
- If empty → prints: `Nothing Was Inserted`.
- Otherwise → processes the list.
3. Removes duplicates while keeping the first occurrence.
4. Displays the cleaned list.

## ▶️ Example Usage

### Case 1: With Values
**Input**

  ```yml
Duplicate Remover
Enter Values in []: [1, 2, 2, 3, apple, apple, 4]
  ```


**Output**

```yml
[1, 2, 3, 'apple', 4]
```

### Case 2: Empty Input
**Input**
```yml
Duplicate Remover
Enter Values in []:
```


**Output**

```yml
Nothing Was Inserted
```


---

## 🚀 How to Run
1. Save the script as `duplicate_remover.py`.
2. Run using Python:
   ```bash
   python duplicate_remover.py
   ```
3. Enter a list when prompted.


## 💡Notes

- Strings must be entered without quotes (e.g., apple, not 'apple').

- Numbers are automatically recognized as integers.

- Order of first occurrence is preserved.

- Empty input is handled with a clear message.

## Author

Made with ❤️ by Pratyaksh Yadav


