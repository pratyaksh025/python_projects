# 🗂️ Dictionary Sorter

This Python program allows users to **create a dictionary dynamically** by entering key-value pairs, and then **sort it** by keys or values with an optional reverse order.

---

## 📌 Features
- Input key-value pairs interactively until the user stops.
- Automatically capitalizes keys.
- Sort the dictionary by:
  - **Key** (alphabetically)
  - **Value** (as entered)
- Option to **reverse the sort order**.
- Displays the dictionary before and after sorting.

---

## ⚙️ How It Works
1. The user enters key-value pairs in the format `Key: Value`.
2. Press Enter on an empty line to stop input.
3. The program displays the entered dictionary.
4. User chooses to sort by **key** or **value**.
5. User can opt to reverse the order by entering `R`.
6. Program outputs the **sorted dictionary**.

---

## ▶️ Example Usage

### Input:
```sql
Enter Key: Value - apple: 5
Enter Key: Value - banana: 2
Enter Key: Value - cherry: 7
Enter Key: Value -
```


### Displayed Dictionary:
```sql
Apple: 5
Banana: 2
Cherry: 7
```


### Sorting Input:

```sql
Sort by (key/value): value
Enter to continue R to reverse: r
```

### Output:

```sql
Sorted Dictionary:
{'Cherry': '7', 'Apple': '5', 'Banana': '2'}
```


---

## 🚀 How to Run
1. Save the script as `interactive_dict_sorter.py`.
2. Run using Python:
   ```bash
   python interactive_dict_sorter.py 
   ```
3. Enter key-value pairs as prompted, then choose sorting options.

## 💡 Notes

- Keys are automatically capitalized.
- Press Enter on an empty line to finish dictionary input.

## Author

Made with ❤️ by Pratyaksh Yadav