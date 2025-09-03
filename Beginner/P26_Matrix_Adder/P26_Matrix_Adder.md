# ➕ Matrix Addition

This Python program performs **addition of two matrices** of the same dimensions.  
The user inputs the number of rows and columns, enters elements for both matrices, and the program outputs their sum.

---

## 📌 Features
- Supports matrices of any size (user-defined rows and columns).
- Validates input to ensure correct number of elements per row.
- Displays the resulting matrix neatly.

---

## ⚙️ How It Works
1. User enters the number of **rows** and **columns**.
2. User inputs elements for **Matrix 1** row by row.
3. User inputs elements for **Matrix 2** row by row.
4. Program adds corresponding elements from both matrices.
5. Prints the resulting matrix.

---

## ▶️ Example Usage

### Input:
```sql
Rows: 2
Comlumns: 3
Enter Elements for Matrix 1:
Row 1: 1 5 6 5 6
Invalid number of elements! Please enter exactly 3 numbers.
Row 1: 5 6 7
Row 2: 54
Invalid number of elements! Please enter exactly 3 numbers.
Row 2: 5 4 9
[[5, 6, 7], [5, 4, 9]]
Enter Elements for Matrix 2
Row 1: 2 5 6
Row 2: 1 23 3
```

### Output
```sql
Result Matrix
7 11 13
6 27 12
```


---

## 🚀 How to Run
1. Save the script as `matrix_addition.py`.
2. Run using Python:
   ```bash
   python matrix_addition.py
   ```
3. Enter the matrix sizes and elements as prompted.
4. View the resulting matrix.

## 💡 Notes

- Both matrices must have the same dimensions.
- Rows are validated to ensure correct number of elements.

## Author

Made with ❤️ by Pratyaksh Yadav