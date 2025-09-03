# 📅 Day of the Week Finder

This Python program allows you to **validate a date** in `yyyy/mm/dd` or `yyyy-mm-dd` format and find the **day of the week** for that date.

---

## 📌 Features
- Validates dates with proper format checking using **regex**.
- Supports both `/` and `-` as separators.
- Returns the **full day name** (e.g., Monday) and **short name** (e.g., Mon).
- Handles invalid dates gracefully.

---

## ⚙️ How It Works
1. User inputs a date in `yyyy/mm/dd` or `yyyy-mm-dd` format.
2. The program first checks if the format is valid using a **regular expression**.
3. If valid, it calculates the day of the week using Python’s `datetime` module.
4. If invalid, it displays an error message.

---

## ▶️ Example Usage

### Input:
```sql
  Enter Date(yyyy/mm/dd or yyyy-mm-dd): 2025-09-03
```

### Output:

```yaml
Day: Wednesday
Short: Wed
```

### Input (Invalid):

```sql
Enter Date(yyyy/mm/dd or yyyy-mm-dd): 2025/13/01
```

### Output:

```yml
Invalid date
```
## 🚀 How to Run
1. Save the script as `date_validator.py`.
2. Run using Python:
   ```bash
   python date_validator.py
   ```
3. Enter the date in the supported format to see the result.

## Author
Made with ❤️ by Pratyaksh Yadav