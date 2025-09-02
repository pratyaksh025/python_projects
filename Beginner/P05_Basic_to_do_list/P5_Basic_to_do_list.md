# Todo List Manager

A simple **command-line Todo List Manager** built in **Python**.

---

## Features
- Add, view, update, and delete tasks.
- Each task stores:
  - Task name
  - Date
  - Time
  - Status (`active`, `completed`, `pending`)
- Input validation using **regex** for task names, date, and time.
- Ensures proper input and gives informative messages on invalid input.
- Dynamically assigns task indexes.
- Prevents undefined variable issues during updates and deletions.

---

## Usage Example

```
Welcome this is a todo_list
Appropriate Actions must be chosen:
Press 1- Adding a task
Press 2- For Viewing All tasks
Press 3- For updating Task
Press 4- For deleting a task
Type 'return' to exit the list. Once exited, all the tasks will be permanently deleted

Enter Task: BuyGroceries
Enter date (DD/MM/YYYY): 01/09/2025
Enter Time (HH:MM): 10:00
Enter Status (active/completed/pending): active
Task Added

Index Task Date Time Status
1 BuyGroceries 01/09/2025 10:00 active
All Tasks are displayed Successfully
```

**Updating a task:**
```
Enter Task Name to update: BuyGroceries
Enter Field To Update (task/date/time/status): status
Value for status field: completed
Task updated successfully
```


**Deleting a task:**
```
Enter Task Name to delete: BuyGroceries
--Task Removed--
```

## Input Validation Examples

- **Task Name:** Only letters, numbers, dots, and underscores are allowed.
- **Date:** Must be in `DD/MM/YYYY` or `DD-MM-YYYY` format.
- **Time:** Must be in `HH:MM` 12-hour format.
- **Status:** Must be one of `active`, `completed`, `pending`.

**Invalid input example:**
```
Enter Task: Buy#Milk
Invalid task name. Retry...
```
## Code Explanation

**Class `todo` :**  
- Handles all todo operations (`add_task`, `view_tasks`, `update_task`, `delete_task`).  
- Uses a global `todo_list` to store tasks as `[index, task, date, time, status]`.

**Function `main` :**  
- Displays the menu.  
- Calls the appropriate method based on user input.  
- Ensures proper variable scoping for updates and deletions.  
- Exits safely on typing `'return'`.

---

## Author
Made with ❤️ by Pratyaksh Yadav